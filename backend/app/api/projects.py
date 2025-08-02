from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models import Project
from app.schemas import ProjectRead

router = APIRouter()

@router.get("/projects", response_model=List[ProjectRead])
def get_projects(
    db: Session = Depends(get_db),
):
    projects = db.query(Project).all()
    return projects
