import logging
import uuid

from fastapi import Depends, FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.projects import router as projects_router
from app.config.context import employee_id_ctx_var, request_id_ctx_var, request_info_ctx_var
from app.config.logging import setup_logging


def employee_id_header(x_employee_id: str = Header(default=None)):
    return x_employee_id

app = FastAPI(dependencies=[Depends(employee_id_header)])

setup_logging()
log = logging.getLogger(__name__)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_request_id_middleware(request: Request, call_next):
    # request_id
    request_id = str(uuid.uuid4())
    request_id_ctx_var.set(request_id)

    # リクエスト情報
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
async def add_employee_id_middleware(request: Request, call_next):
    employee_id = request.headers.get("X-Employee-Id")
    employee_id_ctx_var.set(employee_id)
    response = await call_next(request)
    return response


app.include_router(projects_router)
