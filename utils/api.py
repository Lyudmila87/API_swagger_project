from requests import Response

from data.schema import Entity
from utils.http_methods import HttpMethods
from data.config import BASE_URL


class EntityApi:

    CREATE_URL = BASE_URL + "api/create"
    GET_URL = BASE_URL + "api/get/{}"
    GET_ALL_URL = BASE_URL + "api/getAll"
    PATCH_URL = BASE_URL + "api/patch/{}"
    DELETE_URL = BASE_URL + "api/delete/{}"

    @staticmethod
    def create_new_entity(body: Entity) -> Response:
        return HttpMethods.post(EntityApi.CREATE_URL, body.model_dump())

    @staticmethod
    def get_entity_by_id(entity_id: int) -> Response:
        return HttpMethods.get(EntityApi.GET_URL.format(entity_id))

    @staticmethod
    def get_entities() -> Response:
        return HttpMethods.get(EntityApi.GET_ALL_URL)

    @staticmethod
    def patch_entity_by_id(entity_id: int, body: Entity) -> Response:
        return HttpMethods.patch(EntityApi.PATCH_URL.format(entity_id), body.model_dump())

    @staticmethod
    def delete_entity_by_id(entity_id: int) -> Response:
        return HttpMethods.delete(EntityApi.DELETE_URL.format(entity_id), entity_id)
