from pydantic import BaseModel


class Command(BaseModel):
    class Config:
        orm_mode = True
