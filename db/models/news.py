from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Integer
from db.base_class import Base


class News(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
