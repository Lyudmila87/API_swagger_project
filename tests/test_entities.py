import allure

from utils.checking import Checking
from data.schema import Entity
from utils.api import EntityApi


class TestEntity:
    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Создание сущности")
    def test_create_entity(self, delete_entity):
        with allure.step("Создание сущности"):
            create_entity_data = Entity()
            create_entity_response, status_code = EntityApi.create_new_entity(create_entity_data)

        with allure.step("Проверка создания сущности"):
            assert status_code == 200, "Статус-код не соответствует"
            check_create_entity, _ = EntityApi.get_entity_by_id(create_entity_response.id)
            assert check_create_entity.id == create_entity_response.id, "Сущности по такому ID не существует"
            Checking.assert_entity_response_data(check_create_entity, create_entity_data)
        delete_entity.append(create_entity_response.id)

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Удаление сущности")
    def test_delete_entity(self, create_entity):
        with allure.step("Удаление сущности по ID"):
            create_entity_data, entity_id = create_entity
            delete_entity_status_code = EntityApi.delete_entity_by_id(entity_id)

        with allure.step("Проверка удаления сущности"):
            assert delete_entity_status_code == 204, "Сущность не удалена"

        with allure.step("Проверка отсутствия ID сущности в списке сущностей"):
            get_entities_response = EntityApi.get_entities()
            entity_id_list = [entity.id for entity in get_entities_response]
            assert entity_id not in entity_id_list, "Созданная сущность с таким ID включена в список"

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Получение сущности")
    def test_get_entity(self, create_entity):
        with allure.step("Получение сущности"):
            create_entity_data, entity_id = create_entity
            get_entity_response, status_code = EntityApi.get_entity_by_id(entity_id)

        with allure.step("Проверка валидности сущности"):
            assert status_code == 200, "Статус код не соответствует"
            Checking.assert_entity_response_data(get_entity_response, create_entity_data)
            assert get_entity_response.id == entity_id, "ID сущности не соответствует"

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Получение всех сущностей")
    def test_get_entities(self, create_entity):
        with allure.step("Получение списка сущностей"):
            create_entity_data, entity_id = create_entity
            get_entities_response = EntityApi.get_entities()
        with allure.step("Проверка наличия ID сущности в полученному списке"):
            entity_id_list = [entity.id for entity in get_entities_response]
            assert entity_id in entity_id_list, "Созданная сущность с таким ID не включена в список"

    @allure.feature("Entity")
    @allure.story("API")
    @allure.title("Обновление сущности")
    def test_update_entity(self, create_entity):
        with allure.step("Обновление сущности"):
            create_entity_data, entity_id = create_entity
            update_entity_data = create_entity_data.model_copy(update={"important_numbers": [26, 11, 1987]})
            patch_entity_status_code = EntityApi.patch_entity_by_id(entity_id, update_entity_data)

        with allure.step("Проверка изменения сущности"):
            assert patch_entity_status_code == 204, "Код ответа не соответсвует"
            update_entity_response, _ = EntityApi.get_entity_by_id(entity_id)
            assert entity_id == update_entity_response.id, "ID сущности изменился"
            Checking.assert_entity_response_data(update_entity_response, update_entity_data)
