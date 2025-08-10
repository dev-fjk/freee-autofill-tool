from __future__ import annotations

from datetime import datetime
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.config.clock import now_jst
from app.converter import convert_excel_format_to_read_model
from app.models import Project, ProjectExcelFormat
from app.schemas import PaginatedResponse, Pagination, ProjectCreate, ProjectDetailRead, ProjectRead, ProjectUpdate


def get_project_detail_by_id(
    db: Session,
    project_id: int
) -> ProjectDetailRead:
    """ ID指定でprohect詳細情報を取得
    Args:
        db (Session): DB Session
        project_id (int): Project ID
    Raises:
        HTTPException: Projectが見つからない場合: 404
    Returns:
        ProjectDetailRead: Projectの詳細情報
    """

    # Projectを取得
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # ExcelFormatを取得
    excel_format = db.query(ProjectExcelFormat).filter(
        ProjectExcelFormat.project_id == project_id
    ).first()

    excel_format_read = convert_excel_format_to_read_model(excel_format) if excel_format else None    

    # Pydanticに詰める
    return ProjectDetailRead(
        project_id=project.project_id,
        project_name=project.project_name,
        project_description=project.project_description,
        start_time=project.start_time,
        end_time=project.end_time,
        start_break_time=project.start_break_time,
        end_break_time=project.end_break_time,
        update_key=project.update_key,
        created_at=project.created_at,
        created_by=project.created_by,
        updated_at=project.updated_at,
        updated_by=project.updated_by,
        excel_format=excel_format_read,
    )

def get_projects_with_pagination(
    db: Session,
    project_id: Optional[int],
    project_name: Optional[str],
    page_number: int,
    page_size: int,
) -> PaginatedResponse[ProjectRead]:
    """ Projectsをページングして取得する

    Args:
        db (Session): データベースセッション
        project_id (Optional[int]): Project ID
        project_name (Optional[str]): Project名(部分一致)
        page_number (int): ページ番号
        page_size (int): ページ件数

    Returns:
        PaginatedResponse[ProjectRead]: ページングされたProjectのレスポンス
    """
    query = db.query(Project)
    query = query.order_by(Project.project_id.asc())

    filters = []
    if project_id is not None:
        filters.append(Project.project_id == project_id)
    if project_name is not None:
        filters.append(Project.project_name.ilike(f"%{project_name}%"))
    if filters:
        query = query.filter(and_(*filters))

    total_items = query.count()
    total_pages = (total_items + page_size - 1) // page_size

    offset = (page_number - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    items_read = [ProjectRead.model_validate(item) for item in items]

    return PaginatedResponse[ProjectRead](
        pagination=Pagination(
            page_number=page_number,
            page_size=page_size,
            total=total_items,
            item_count=len(items),
            total_pages=total_pages,
        ),
        items=items_read,
    )

def create_project(db: Session, project_in: ProjectCreate) -> Project:
    """
    新規プロジェクトを作成しDBに保存する。

    Args:
        db (Session): SQLAlchemyのDBセッション
        project_in (ProjectCreate): プロジェクト作成用のPydanticモデル

    Returns:
        Project: 作成されたProjectのORMモデルインスタンス
    """
        
    # 文字列からtime型に変換
    start_time = datetime.strptime(project_in.start_time, '%H:%M').time()
    end_time = datetime.strptime(project_in.end_time, '%H:%M').time()
    start_break_time = datetime.strptime(project_in.start_break_time, '%H:%M').time()
    end_break_time = datetime.strptime(project_in.end_break_time, '%H:%M').time()

    project = Project(
        project_name=project_in.project_name,
        project_description=project_in.project_description,
        start_time=start_time,
        end_time=end_time,
        start_break_time=start_break_time,
        end_break_time=end_break_time,
        update_key=project_in.update_key,
        created_by=project_in.created_by,
        updated_by=project_in.updated_by,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def update_project(db: Session, project_id: int, project_update: ProjectUpdate) -> ProjectRead:
    """
    プロジェクト情報を更新する。

    Args:
        db (Session): DBセッション
        project_id (int): 更新対象のプロジェクトID
        project_update (ProjectUpdate): 更新データ（update_keyは更新不可）

    Returns:
        ProjectRead: 更新後のプロジェクト情報

    Raises:
        HTTPException: update_keyが不一致の場合（409 Conflict）
        HTTPException: プロジェクトが存在しない場合（404 Not Found）
    """
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # update_keyの整合性チェック
    if project.update_key != project_update.update_key:
        raise HTTPException(status_code=409, detail="update_key mismatch")

    # 更新処理
    project.project_name = project_update.project_name
    project.project_description = project_update.project_description
    project.start_time = datetime.strptime(project_update.start_time, "%H:%M").time()
    project.end_time = datetime.strptime(project_update.end_time, "%H:%M").time()
    project.start_break_time = datetime.strptime(project_update.start_break_time, "%H:%M").time()
    project.end_break_time = datetime.strptime(project_update.end_break_time, "%H:%M").time()
    # update_keyは変更しない

    project.updated_at = now_jst()
    project.updated_by = project_update.updated_by

    db.add(project)
    db.commit()
    db.refresh(project)

    # 返却用にPydanticモデルに変換
    return ProjectRead.model_validate(project)

def delete_project_by_id(db: Session, project_id: int, update_key: int) -> None:
    """
    指定されたproject_idのプロジェクトをupdate_keyの一致確認後に削除する。

    Args:
        db (Session): DBセッション
        project_id (int): 削除対象プロジェクトID
        update_key (int): クライアントが送信した更新キー

    Raises:
        HTTPException: プロジェクトが存在しない場合404
        HTTPException: update_keyが一致しない場合409

    Returns:
        None: 削除成功時は特に返さない（204 No Content相当）
    """
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="プロジェクトが見つかりません。")

    if project.update_key != update_key:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="更新キーが一致しません。")

    db.delete(project)
    db.commit()
