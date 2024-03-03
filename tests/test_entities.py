import allure

from utils.checking import Checking
from data.schema import Entity, CreteEntityResponse, GetEntity
from utils.api import EntityApi


class TestEntity:
    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Создание сущности")
    def test_create_entity(self, delete_entity):
        with allure.step("Создание сущности"):
            create_entity_data = Entity()
            create_entity_response = EntityApi.create_new_entity(create_entity_data)
            serialized_post_response = CreteEntityResponse(id=create_entity_response.text)

        with allure.step("Проверка создания сущности"):
            assert create_entity_response.status_code == 200, "Статус-код не соответствует"
            check_create_entity = EntityApi.get_entity_by_id(serialized_post_response.id)
            serialized_get_response = GetEntity(**check_create_entity.json())
            assert serialized_get_response.id == serialized_post_response.id, "Сущности по такому ID не существует"
            Checking.assert_entity_response_data(serialized_get_response, create_entity_data)
        delete_entity.append(create_entity_response.text)

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Удаление сущности")
    def test_delete_entity(self, create_entity):
        with allure.step("Удаление сущности по ID"):
            create_entity_data, entity_id = create_entity
            delete_entity_response = EntityApi.delete_entity_by_id(entity_id)

        with allure.step("Проверка удаления сущности"):
            assert delete_entity_response.status_code == 204, "Сущность не удалена"

        with allure.step("Проверка отсутствия ID сущности в списке сущностей"):
            get_entities_response = EntityApi.get_entities()
            serialized_get_entities_response = [GetEntity(**entity) for entity in get_entities_response.json().get("entity")]
            entity_id_list = [entity.id for entity in serialized_get_entities_response]
            assert entity_id not in entity_id_list, "Созданная сущность с таким ID включена в список"

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Получение сущности")
    def test_get_entity(self, create_entity):
        with allure.step("Получение сущности"):
            create_entity_data, entity_id = create_entity
            get_entity_response = EntityApi.get_entity_by_id(entity_id)
            serialized_get_response = GetEntity(**get_entity_response.json())

        with allure.step("Проверка валидности сущности"):
            assert get_entity_response.status_code == 200, "Статус код не соответствует"
            Checking.assert_entity_response_data(serialized_get_response, create_entity_data)
            assert serialized_get_response.id == entity_id, "ID сущности не соответствует"

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Получение всех сущностей")
    def test_get_entities(self, create_entity):
        with allure.step("Получение списка сущностей"):
            create_entity_data, entity_id = create_entity
            get_entities_response = EntityApi.get_entities()
            serialized_get_entities_response = [GetEntity(**entity) for entity in
                                                get_entities_response.json().get("entity")]

        with allure.step("Проверка наличия ID сущности в полученному списке"):
            entity_id_list = [entity.id for entity in serialized_get_entities_response]
            assert entity_id in entity_id_list, "Созданная сущность с таким ID не включена в список"

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Обновление сущности")
    def test_update_entity(self, create_entity):
        with allure.step("Обновление сущности"):
            create_entity_data, entity_id = create_entity
            update_entity_data = create_entity_data.model_copy(update={"important_numbers": [26, 11, 1987]})
            patch_entity_response = EntityApi.patch_entity_by_id(entity_id, update_entity_data)

        with allure.step("Проверка изменения сущности"):
            assert patch_entity_response.status_code == 204, "Код ответа не соответсвует"
            update_entity_response = EntityApi.get_entity_by_id(entity_id)
            serialized_get_response = GetEntity(**update_entity_response.json())
            assert entity_id == serialized_get_response.id, "ID сущности изменился"
            Checking.assert_entity_response_data(serialized_get_response, update_entity_data)
