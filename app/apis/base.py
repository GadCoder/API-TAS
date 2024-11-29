from fastapi import APIRouter
from app.apis.routes import data_element

api_router = APIRouter()

api_router.include_router(data_element.router, tags=["data-element"], prefix="/data-element")
