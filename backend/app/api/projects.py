from typing import Optional

from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from app.api.deps import require_employee_id, require_role
from app.db.deps import get_db
from app.schemas import (
    PaginatedResponse,
    ProjectCreate,
    ProjectDetailRead,
    ProjectRead,
    ProjectUpdate,
)
from app.services.project_service import (
    create_project,
    delete_project_by_id,
    get_project_detail_by_id,
    get_projects_with_pagination,
    update_project,
)

router = APIRouter(tags=["Project"],dependencies=[Depends(require_employee_id), Depends(require_role)],)

@router.get(
    "/projects/{project_id}",
    response_model=ProjectDetailRead,
    summary="プロジェクト詳細取得",
    description="プロジェクトIDで詳細取得",
    operation_id="getProjectDetail",
)
def get_project_detail(
    project_id: int = Path(..., description="プロジェクトID"),
    db: Session = Depends(get_db),
):
    return get_project_detail_by_id(db, project_id)

@router.get(
    "/projects",
    response_model=PaginatedResponse[ProjectRead],
    summary="プロジェクト一覧取得",
    description="プロジェクトIDや名前で絞り込み・ページング対応",
    operation_id="getProjects",
)
def get_projects(
    project_id: Optional[int] = Query(None),
    project_name: Optional[str] = Query(None),
    page_number: int = Query(1, ge=1),
    page_size: int = Query(30, ge=10, le=100),
    db: Session = Depends(get_db),
):
    return get_projects_with_pagination(db, project_id, project_name, page_number, page_size)

@router.post(
    "/projects",
    response_model=ProjectRead,
    status_code=status.HTTP_201_CREATED,
    summary="プロジェクト作成",
    description="新しいプロジェクトを登録する",
    operation_id="createProject",
)
def create_new_project(
    project_in: ProjectCreate = Body(...),
    db: Session = Depends(get_db),
):
    project = create_project(db, project_in)
    return project

@router.put(
    "/projects/{project_id}",
    response_model=ProjectRead,
    summary="プロジェクト更新",
    description="指定IDのプロジェクトを更新する",
    operation_id="updateProject",
)
def update_existing_project(
    project_id: int = Path(..., description="プロジェクトID"),
    project_in: ProjectUpdate = Body(...),
    db: Session = Depends(get_db),
):
    try:
        updated_project = update_project(db, project_id, project_in)
        return updated_project
    except HTTPException as e:
        raise e

@router.delete(
    "/projects/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="プロジェクト削除",
    description="指定IDのプロジェクトを削除します。update_keyが一致しない場合はエラーになります。",
    operation_id="deleteProject",
)
def delete_project(
    project_id: int = Path(..., description="プロジェクトID"),
    update_key: int = Query(..., description="更新キー（0〜9999）"),
    db: Session = Depends(get_db),
):
    try:
        delete_project_by_id(db, project_id, update_key)
    except HTTPException as e:
        raise e
