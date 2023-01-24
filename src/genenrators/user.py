from src.base_classes.builder import BuilderBaseClass
from src.genenrators.test_data_generator import generate_random_string
from random import randint


class User(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_id(self, user_id=randint(1, 1000)):
        self.result['id'] = user_id
        return self

    def set_username(self, username=generate_random_string(5)):
        self.result['username'] = username
        return self

    def set_firstname(self, firstname=generate_random_string(6)):
        self.result['firstName'] = firstname
        return self

    def set_lastname(self, lastname=generate_random_string(7)):
        self.result['lastName'] = lastname
        return self

    def set_email(self, email=generate_random_string(8) + "@test.ru"):
        self.result['email'] = email
        return self

    def set_password(self, password='qwerty12'):
        self.result['password'] = password
        return self

    def set_phone(self, phone=generate_random_string(10)):
        self.result['phone'] = phone
        return self

    def set_status(self, status=1):
        self.result['userStatus'] = status
        return self

    def reset(self):
        self.set_id()
        self.set_username()
        self.set_firstname()
        self.set_lastname()
        self.set_email()
        self.set_password()
        self.set_phone()
        self.set_status()
        return self
