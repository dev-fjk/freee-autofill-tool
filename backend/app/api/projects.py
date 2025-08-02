from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models import Project
from app.schemas import ProjectRead

router = APIRouter(tags=["ProjectAPI"])

@router.get(    
    "/projects",
    response_model=List[ProjectRead],
    summary="プロジェクト一覧取得",
    description="プロジェクト一覧を取得する")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects
