
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas import PaginatedResponse, ProjectRead
from app.services.project_service import get_projects_with_pagination

router = APIRouter(tags=["ProjectAPI"])

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
