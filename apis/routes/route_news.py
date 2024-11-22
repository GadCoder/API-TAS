from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi import Depends

from db.session import get_db
from schemas.news import NewsCreate, News
from db.repository.news import save_news, retrieve_last_news


router = APIRouter()


@router.post("/create-news/", response_model=News)
def create_new_news(news: NewsCreate, db: Session = Depends(get_db)):
    news = save_news(news, db)
    return news


@router.get("/get-latest-news/", response_model=list[News])
def get_latest_news(db: Session = Depends(get_db)):
    news = retrieve_last_news(db)
    return news
