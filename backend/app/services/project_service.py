from __future__ import annotations

from typing import Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models import Project
from app.schemas import PaginatedResponse, Pagination, ProjectRead


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
