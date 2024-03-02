import pytest

from data.schema import Entity
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
    create_entity_response, _ = EntityApi.create_new_entity(create_entity_data)
    delete_entity.append(create_entity_response.id)
    return create_entity_data, create_entity_response.id
