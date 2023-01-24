import pytest
from src.genenrators.user import User
from src.genenrators.order import Order
from src.genenrators.pet import Pet


@pytest.fixture
def get_user_generator():
    return User()


@pytest.fixture
def get_order_generator():
    return Order()


@pytest.fixture
def get_pet_generator():
    return Pet()
