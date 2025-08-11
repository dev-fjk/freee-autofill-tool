from fastapi import APIRouter, Body, HTTPException, status

from app.config.settings import settings
from app.schemas import (
    LoginRequest,
    LoginResponse,
)

router = APIRouter(tags=["Auth"])


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="ログイン",
    description="社員IDと共通パスワードでログイン。成功時は社員IDを返す。",
    operation_id="login",
)
def login(
    login_data: LoginRequest = Body(...),
):
    if login_data.password == settings.normal_user_password:
        role = "user"
    elif login_data.password == settings.admin_user_password:
        role = "admin"
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    return LoginResponse(employee_id=login_data.employee_id, role=role)
