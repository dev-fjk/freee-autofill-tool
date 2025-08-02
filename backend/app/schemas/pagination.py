from __future__ import annotations

from typing import Generic, List, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")

class Pagination(BaseModel):
    page_number: int
    page_size: int
    total: int
    item_count: int
    total_pages: int

class PaginatedResponse(GenericModel, Generic[T]):
    pagination: Pagination
    items: List[T]
