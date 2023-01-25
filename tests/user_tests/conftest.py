import pytest
import json
from src.backend_steps import user_steps
from src.base_classes.response import Response
from src.genenrators.user import User


@pytest.fixture
def get_user_data():
    user_data = User().build()
    Response(user_steps.create_user(user_data))\
        .assert_status_code(200)
    return json.loads(user_data)
