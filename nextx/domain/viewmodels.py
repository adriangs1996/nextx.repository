from typing import Generic, Optional, Sequence, TypeVar
from pydantic.generics import GenericModel
from fastapi import status
from bson import ObjectId


T = TypeVar("T")


class DataResponse(GenericModel, Generic[T]):
    data: Optional[T] = None
    status_code: Optional[int] = status.HTTP_200_OK
    message: Optional[str] = "Success"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        orm_mode = True
        json_encoders = {ObjectId: str}


class Page(GenericModel, Generic[T]):
    items: Sequence[T]
    records: int = 0
    total: int = 0
