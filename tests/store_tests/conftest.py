import pytest
from src.base_classes.response import Response
from src.backend_steps import store_steps
from src.genenrators.order import Order


@pytest.fixture
def make_order_data():
    response = Response(store_steps.create_order(Order().build()))
    return response.response_json
