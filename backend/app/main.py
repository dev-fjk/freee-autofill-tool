import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.projects import router as projects_router
from app.config.logging import request_id_ctx_var, request_info_ctx_var, setup_logging

setup_logging()
log = logging.getLogger(__name__)
app = FastAPI()

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

app.include_router(projects_router)
