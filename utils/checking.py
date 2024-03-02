from data.schema import Entity, GetEntity


class Checking:
    @staticmethod
    def assert_entity_response_data(entity_response: GetEntity, create_entity: Entity):
        assert entity_response.verified == create_entity.verified, "Атрибут verifed не соответствует"
        assert entity_response.title == create_entity.title, "Атрибут title не соответствует"
        assert entity_response.important_numbers == create_entity.important_numbers, \
            "Атрибут important_numbers не соответствует"
        for key, value in create_entity.addition.items():
            assert value == entity_response.addition.get(key), \
                f"Значение ключа {key} атрибута addition не соответствует"
