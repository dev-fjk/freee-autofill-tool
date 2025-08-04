from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProjectExcelFormatRead(BaseModel):
    """Excelフォーマット情報"""
    project_id: int
    date_type: int
    start_line: int
    date_col: str
    date_format: Optional[str]
    start_date_col: str
    end_date_col: str
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    model_config = {
        "from_attributes": True,
    }    
