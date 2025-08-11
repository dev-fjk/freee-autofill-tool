import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.login import router as login_router
from app.api.projects import router as projects_router
from app.config.context import employee_id_ctx_var, request_id_ctx_var, request_info_ctx_var, role_ctx_var
from app.config.logging import setup_logging

app = FastAPI()

setup_logging()
log = logging.getLogger(__name__)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_request_id_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request_id_ctx_var.set(request_id)

    info = {
        "method": request.method,
        "url": str(request.url),
        "client_ip": request.client.host if request.client else "unknown",
    }
    request_info_ctx_var.set(info)

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


@app.middleware("http")
async def add_auth_headers_middleware(request: Request, call_next):
    # 認証スキップ対象パス
    open_paths = ["/login", "/docs", "/openapi.json", "/redoc"]

    if request.url.path in open_paths:
        return await call_next(request)

    employee_id = request.headers.get("X-Employee-Id")
    role = request.headers.get("X-Role")

    if not employee_id or not role:
        return JSONResponse(status_code=400, content={"detail": "Missing required auth headers"})

    employee_id_ctx_var.set(employee_id)
    role_ctx_var.set(role)

    response = await call_next(request)
    return response


app.include_router(login_router)
app.include_router(projects_router)
