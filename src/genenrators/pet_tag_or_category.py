from src.base_classes.builder import BuilderBaseClass
from src.genenrators.test_data_generator import generate_random_string
from random import randint


class TagOrCategory(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_tag_id(self, tag_id=randint(1, 1000)):
        self.result['id'] = tag_id
        return self

    def set_name(self, name=generate_random_string(10)):
        self.result['name'] = name
        return self

    def reset(self):
        self.set_tag_id()
        self.set_name()
        return self
