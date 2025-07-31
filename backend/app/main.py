import logging

from fastapi import FastAPI
from pydantic import BaseModel

from app.config.logging_config import setup_logging

setup_logging()
log = logging.getLogger(__name__)
app = FastAPI()

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
