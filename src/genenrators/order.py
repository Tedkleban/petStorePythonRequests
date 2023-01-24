from src.base_classes.builder import BuilderBaseClass
from src.enums.order_status import OrderStatus
from random import randint


class Order(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_order_id(self, order_id=randint(1, 1000)):
        self.result['id'] = order_id
        return self

    def set_pet_id(self, pet_id=randint(1, 1000)):
        self.result['petId'] = pet_id
        return self

    def set_quantity(self, quantity=randint(1, 1000)):
        self.result['quantity'] = quantity
        return self

    def set_date(self, ship_date="1998-11-12T15:35:39.098Z"):
        self.result['shipDate'] = ship_date
        return self

    def set_status(self, status=OrderStatus.APPROVED.value):
        self.result['status'] = status
        return self

    def set_complete(self, complete=False):
        self.result['complete'] = complete
        return self

    def reset(self):
        self.set_order_id()
        self.set_pet_id()
        self.set_quantity()
        self.set_date()
        self.set_status()
        self.set_complete()
        return self
