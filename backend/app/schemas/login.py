from pydantic import BaseModel, Field, field_validator


class LoginRequest(BaseModel):
    employee_id: str = Field(..., description="社員ID (e + 数字1〜5桁、最大6文字)", example="e024")
    password: str = Field(..., description="共通パスワード", example="normal_user")

    @field_validator('employee_id')
    def check_employee_id(cls, v):
        import re
        if not re.fullmatch(r"^e\d{1,5}$", v):
            raise ValueError('社員IDはeに続く数字1〜5桁でなければなりません')
        return v


class LoginResponse(BaseModel):
    employee_id: str = Field(..., description="社員ID", example="e024")
    role: str = Field(..., description="権限（user または admin）", example="user")
