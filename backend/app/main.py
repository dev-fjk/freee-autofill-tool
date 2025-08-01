import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

@app.get("/")
def read_root():
    log.info("Root endpoint accessed")
    return {"message": "Hello from /"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
