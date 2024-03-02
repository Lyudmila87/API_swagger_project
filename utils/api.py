from data.schema import GetEntity, CreteEntityResponse, Entity
from utils.htttp_methods import HttpMethods

BASE_URL = "http://localhost:8081/"


class EntityApi:
    @staticmethod
    def create_new_entity(body: Entity) -> tuple[CreteEntityResponse, int]:
        post_url = BASE_URL + "api/create"
        response_body = HttpMethods.post(post_url, body.model_dump())
        return CreteEntityResponse(id=response_body.text), response_body.status_code

    @staticmethod
    def get_entity_by_id(entity_id: int) -> tuple[GetEntity, int]:
        get_url = BASE_URL + f"api/get/{entity_id}"
        response_body = HttpMethods.get(get_url)
        return GetEntity(**response_body.json()), response_body.status_code

    @staticmethod
    def get_entities() -> list[GetEntity]:
        get_url = BASE_URL + "api/getAll"
        response_body = HttpMethods.get(get_url)
        entities = [GetEntity(**entity) for entity in response_body.json().get("entity")]
        return entities

    @staticmethod
    def patch_entity_by_id(entity_id: int, body: Entity) -> int:
        patch_url = BASE_URL + f"api/patch/{entity_id}"
        response_body = HttpMethods.patch(patch_url, body.model_dump())
        return response_body.status_code

    @staticmethod
    def delete_entity_by_id(entity_id: int) -> int:
        delete_url = BASE_URL + f"api/delete/{entity_id}"
        response_body = HttpMethods.delete(delete_url, entity_id)
        return response_body.status_code
