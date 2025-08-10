from datetime import datetime, time
from typing import Annotated, Optional

from pydantic import BaseModel, Field, conint, constr, model_validator

from app.schemas.project_excel_format import ProjectExcelFormatRead

# validation conditions
ProjectName = Annotated[str, constr(min_length=1, max_length=255)]
UpdateKey = Annotated[int, conint(ge=0, le=9999)]
UserName = Annotated[str, constr(min_length=1, max_length=20)]


class ProjectRead(BaseModel):
    """プロジェクト情報"""
    project_id: int = Field(..., description="プロジェクトID", example=1)
    project_name: str = Field(..., description="プロジェクト名", example="Test Project")
    project_description: Optional[str] = Field(None, description="プロジェクト説明", example="詳細説明")
    start_time: time = Field(..., description="開始時間", example="09:00:00")
    end_time: time = Field(..., description="終了時間", example="18:00:00")
    start_break_time: time = Field(..., description="休憩開始時間", example="12:00:00")
    end_break_time: time = Field(..., description="休憩終了時間", example="13:00:00")
    update_key: int = Field(..., description="更新キー（0〜9999）", example=1234)
    created_at: datetime = Field(..., description="作成日時", example="2025-08-10T09:00:00")
    created_by: str = Field(..., description="作成者", example="e024")
    updated_at: datetime = Field(..., description="更新日時", example="2025-08-10T10:00:00")
    updated_by: str = Field(..., description="更新者", example="e024")

    model_config = {
        "from_attributes": True,
    }

class ProjectDetailRead(BaseModel):
    """Project詳細(Excelフォーマット情報を含む)"""
    project_id: int = Field(..., description="プロジェクトID", example=1)
    project_name: str = Field(..., description="プロジェクト名", example="Test Project")
    project_description: Optional[str] = Field(None, description="プロジェクト説明", example="詳細説明")
    start_time: time = Field(..., description="開始時間", example="09:00:00")
    end_time: time = Field(..., description="終了時間", example="18:00:00")
    start_break_time: time = Field(..., description="休憩開始時間", example="12:00:00")
    end_break_time: time = Field(..., description="休憩終了時間", example="13:00:00")
    update_key: int = Field(..., description="更新キー（0〜9999）", example=1234)
    created_at: datetime = Field(..., description="作成日時", example="2025-08-10T09:00:00")
    created_by: str = Field(..., description="作成者", example="e024")
    updated_at: datetime = Field(..., description="更新日時", example="2025-08-10T10:00:00")
    updated_by: str = Field(..., description="更新者", example="e024")
    excel_format: Optional[ProjectExcelFormatRead] = Field(None, description="Excelフォーマット情報")

    model_config = {
        "from_attributes": True,
    }

class ProjectCreate(BaseModel):
    """プロジェクト作成"""
    project_name: ProjectName = Field(
        ...,
        min_length=1,
        max_length=255,
        description="プロジェクト名",
        example="Test Project",
    )
    project_description: Optional[str] = Field(None, description="プロジェクト説明", example="詳細説明")
    start_time: str = Field(..., description="開始時間 (HH:mm)", example="09:00")
    end_time: str = Field(..., description="終了時間 (HH:mm)", example="18:00")
    start_break_time: str = Field(..., description="休憩開始時間 (HH:mm)", example="12:00")
    end_break_time: str = Field(..., description="休憩終了時間 (HH:mm)", example="13:00")
    update_key: UpdateKey = Field(..., description="更新キー（0〜9999）", example=1234)
    created_by: UserName = Field(..., description="作成者", example="e024")
    updated_by: UserName = Field(..., description="更新者", example="e024")

    @model_validator(mode='before')
    def check_time_order(cls, values):
        start = values.get('start_time')
        end = values.get('end_time')
        start_break = values.get('start_break_time')
        end_break = values.get('end_break_time')

        if start is not None and end is not None and end <= start:
            raise ValueError('end_time must be after start_time')

        if start_break is not None and end_break is not None and end_break <= start_break:
            raise ValueError('end_break_time must be after start_break_time')

        return values
    
class ProjectUpdate(BaseModel):
    """プロジェクト更新（PUT）用スキーマ。全項目必須で更新します。"""

    project_name: ProjectName = Field(
        ..., description="プロジェクト名", example="Updated Project"
    )
    project_description: Optional[str] = Field(
        None, description="プロジェクト説明", example="更新された説明"
    )
    start_time: str = Field(..., description="開始時間 (HH:mm)", example="09:00")
    end_time: str = Field(..., description="終了時間 (HH:mm)", example="18:00")
    start_break_time: str = Field(..., description="休憩開始時間 (HH:mm)", example="12:00")
    end_break_time: str = Field(..., description="休憩終了時間 (HH:mm)", example="13:00")
    update_key: UpdateKey = Field(..., description="更新キー（0〜9999）", example=1234)
    updated_by: UserName = Field(..., description="更新者", example="e024")

    @model_validator(mode='before')
    def check_time_order(cls, values):
        start = values.get('start_time')
        end = values.get('end_time')
        start_break = values.get('start_break_time')
        end_break = values.get('end_break_time')

        if start is not None and end is not None and end <= start:
            raise ValueError('end_time must be after start_time')

        if start_break is not None and end_break is not None and end_break <= start_break:
            raise ValueError('end_break_time must be after start_break_time')

        return values    
