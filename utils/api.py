from requests import Response

from data.schema import Entity
from utils.http_methods import HttpMethods
from data.config import BASE_URL


class EntityApi:

    create_endpoint = "api/create"
    get_endpoint = "api/get/{}"
    get_all_endpoint = "api/getAll"
    patch_endpoint = "api/patch/{}"
    delete_endpoint = "api/delete/{}"

    @staticmethod
    def create_new_entity(body: Entity) -> Response:
        post_url = BASE_URL + EntityApi.create_endpoint
        return HttpMethods.post(post_url, body.model_dump())

    @staticmethod
    def get_entity_by_id(entity_id: int) -> Response:
        get_url = BASE_URL + EntityApi.get_endpoint.format(entity_id)
        return HttpMethods.get(get_url)

    @staticmethod
    def get_entities() -> Response:
        get_url = BASE_URL + EntityApi.get_all_endpoint
        return HttpMethods.get(get_url)

    @staticmethod
    def patch_entity_by_id(entity_id: int, body: Entity) -> Response:
        patch_url = BASE_URL + EntityApi.patch_endpoint.format(entity_id)
        return HttpMethods.patch(patch_url, body.model_dump())

    @staticmethod
    def delete_entity_by_id(entity_id: int) -> Response:
        delete_url = BASE_URL + EntityApi.delete_endpoint.format(entity_id)
        return HttpMethods.delete(delete_url, entity_id)
