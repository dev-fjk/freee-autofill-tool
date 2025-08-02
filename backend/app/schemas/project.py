from datetime import datetime, time

from pydantic import BaseModel


class ProjectRead(BaseModel):
    project_id: int
    project_name: str
    project_description: str | None = None  # 追加
    start_time: time
    end_time: time
    start_break_time: time
    end_break_time: time
    update_key: int
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

    class Config:
        orm_mode = True
