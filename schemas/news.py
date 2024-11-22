import datetime
from pydantic import BaseModel


class NewsBase(BaseModel):
    title: str
    url: str
    content: str


class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
