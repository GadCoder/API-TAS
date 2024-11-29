import datetime
from app.schemas.data_element import DataElementCreate
from app.db.models.data_element import DataElement


async def save_data_element(element: DataElementCreate):
    print(f"Element: {element}")
    data_element = DataElement(
        title=element.title,
        url=element.url,
        content=element.content,
        type=element.type,
        created_at=datetime.datetime.now(),
    )
    await data_element.create()
    return data_element

def retrieve_last_elements_from_type(
    type: str,
    delay_in_days: int = 7,
):
    time_delay = datetime.datetime.now() - datetime.timedelta(days=delay_in_days)
    return DataElement.find(DataElement.type == type, DataElement.created_at >= time_delay).to_list()

