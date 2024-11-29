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
    delay_in_days: int = 7,
):
    time_delay = datetime.datetime.now() - datetime.timedelta(days=delay_in_days)
    return db.query(News).filter(News.created_at >= time_delay).all()
