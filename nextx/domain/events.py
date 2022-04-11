from pydantic import BaseModel


class Event(BaseModel):
    class Config:
        orm_mode = True
