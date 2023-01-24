from src.base_classes.builder import BuilderBaseClass
from src.enums.pet_status import PetStatus
from src.genenrators.test_data_generator import generate_random_string
from src.genenrators.pet_tag_or_category import TagOrCategory
from random import randint


class Pet(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_name(self, name=generate_random_string(10)):
        self.result['name'] = name
        return self

    def set_photo_urls(self, photo_urls=None):
        if photo_urls is None:
            photo_urls = [generate_random_string(15), generate_random_string(12)]
        self.result['photoUrls'] = photo_urls
        return self

    def set_pet_id(self, pet_id=randint(1, 1000)):
        self.result['id'] = pet_id
        return self

    def set_status(self, status=PetStatus.AVAILABLE.value):
        self.result['status'] = status
        return self

    def reset(self):
        self.set_name()
        self.set_photo_urls()
        self.set_pet_id()
        self.result['category'] = {
            'id': 1321234,
            'name': "asdfasf"
        }
        self.result['tags'] = [
            {
                'id': 1321234,
                'name': "asdfasf"
            },
            {
                'id': 12424124,
                'name': "asdfsdfsasf"
            }
        ]
        self.set_status()
        return self
