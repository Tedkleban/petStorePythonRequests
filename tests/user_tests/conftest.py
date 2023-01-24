import pytest
from src.backend_steps import user_steps
from src.base_classes.response import Response
from src.genenrators.user import User


@pytest.fixture
def get_username():
    user_data: dict = User().build()
    username = user_data.get('username')
    password = user_data.get('password')
    Response(user_steps.create_user(user_data))
    return username, password
