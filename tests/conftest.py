import pytest

from data.schema import Entity, CreteEntityResponse
from utils.api import EntityApi


@pytest.fixture()
def delete_entity() -> list:
    entities = []
    yield entities
    for id_entity in entities:
        EntityApi.delete_entity_by_id(id_entity)


@pytest.fixture
def create_entity(delete_entity) -> tuple[Entity, int]:
    create_entity_data = Entity()
    create_entity_response = EntityApi.create_new_entity(create_entity_data)
    serialized_post_response = CreteEntityResponse(id=create_entity_response.text)
    delete_entity.append(serialized_post_response.id)
    return create_entity_data, serialized_post_response.id
