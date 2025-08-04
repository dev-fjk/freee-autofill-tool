from __future__ import annotations

from typing import Optional

from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.converter import convert_excel_format_to_read_model
from app.models import Project, ProjectExcelFormat
from app.schemas import PaginatedResponse, Pagination, ProjectDetailRead, ProjectRead


def get_project_detail_by_id(
    db: Session,
    project_id: int
) -> ProjectDetailRead:
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
