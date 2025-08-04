from datetime import datetime, time
from typing import Optional

from pydantic import BaseModel

from app.schemas.project_excel_format import ProjectExcelFormatRead


class ProjectRead(BaseModel):
    """プロジェクト情報"""
    project_id: int
    project_name: str
    project_description: Optional[str] = None
    start_time: time
    end_time: time
    start_break_time: time
    end_break_time: time
    update_key: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    model_config = {
        "from_attributes": True,
    }

class ProjectDetailRead(BaseModel):
    """Project詳細(Excelフォーマット情報を含む)"""
    project_id: int
    project_name: str
    project_description: Optional[str]
    start_time: time
    end_time: time
    start_break_time: time
    end_break_time: time
    update_key: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str
    excel_format: Optional[ProjectExcelFormatRead]

    model_config = {
        "from_attributes": True,
    }
