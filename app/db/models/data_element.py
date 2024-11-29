from datetime import datetime
from beanie import Document

class DataElement(Document):
    title: str
    url: str
    content: str
    type: str
    created_at: datetime
