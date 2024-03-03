from pydantic import BaseModel


class Entity(BaseModel):
    addition: dict = {"additional_info": "Дополнительные сведения", "additional_number": 125}
    important_numbers: list = [42, 87, 15]
    title: str = "Заголовок сущности"
    verified: bool = True


class GetEntity(Entity):
    id: int


class CreteEntityResponse(BaseModel):
    id: int
