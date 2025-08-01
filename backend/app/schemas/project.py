from datetime import datetime, time

from pydantic import BaseModel


class ProjectSchema(BaseModel):
    project_id: int
    project_name: str
    start_time: time
    end_time: time
    start_break_time: time
    end_break_time: time
    update_key: int
    created_at: datetime
    created_by: str | None = None
    updated_at: datetime
    updated_by: str | None = None

    class Config:
        orm_mode = True
