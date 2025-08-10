from typing import Optional

from fastapi import APIRouter, Body, Depends, Path, Query, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas import (
    PaginatedResponse,
    ProjectCreate,
    ProjectDetailRead,
    ProjectRead,
)
from app.services.project_service import (
    create_project,
    get_project_detail_by_id,
    get_projects_with_pagination,
)

router = APIRouter(tags=["ProjectAPI"])

@router.get(
    "/projects/{project_id}",
    response_model=ProjectDetailRead,
    summary="プロジェクト詳細取得",
    description="プロジェクトIDで詳細取得",
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
)
def create_new_project(
    project_in: ProjectCreate = Body(...),
    db: Session = Depends(get_db),
):
    project = create_project(db, project_in)
    return project
