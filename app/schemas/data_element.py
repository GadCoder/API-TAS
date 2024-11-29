import datetime
from pydantic import BaseModel


class DataElementBase(BaseModel):
    title: str
    url: str
    content: str
    type: str


class DataElementCreate(DataElementBase):
    pass


class DataElement(DataElementBase):
    created_at: datetime.datetime
    pass