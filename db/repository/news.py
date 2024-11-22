import datetime
from sqlalchemy.orm import Session
from schemas.news import NewsCreate

from db.models.news import News


def save_news(news: NewsCreate, db: Session):
    news = News(
        title=news.title,
        url=news.url,
        content=news.content,
        created_at=datetime.datetime.now(),
    )
    db.add(news)
    db.commit()
    db.refresh(news)
    return news


def retrieve_last_news(
    db: Session,
):
    return db.query(News).all()
