from fastapi import APIRouter
from apis.routes import route_news

api_router = APIRouter()

api_router.include_router(route_news.router, tags=["news"], prefix="/news")
