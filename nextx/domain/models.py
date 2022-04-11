from pydantic import BaseModel
from beanie import PydanticObjectId


class Entity(BaseModel):
    id: PydanticObjectId

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}
        orm_mode = True

    def __hash__(self):
        return hash(self.id)


class PagingModel:
    def __init__(self, limit: int = 1000, skip: int = 0) -> None:
        self.limit = limit
        self.skip = skip
