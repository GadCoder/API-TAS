from fastapi import APIRouter
from fastapi import Depends

from app.db.repository.data_element import save_data_element, retrieve_last_elements_from_type
from app.schemas.data_element import DataElementCreate, DataElement

router = APIRouter()


@router.post("/create-data/", response_model=DataElement)
async def create_new_data_element(data_element: DataElementCreate):
    data_element = await save_data_element(element=data_element)
    return data_element


@router.get("/get-latest-elements-from-type/", response_model=list[DataElement])
async def get_latest_elements_from_type(type: str, delay_in_days: int = 7):
    latest_elements = await retrieve_last_elements_from_type(type=type, delay_in_days=delay_in_days)
    return latest_elements
