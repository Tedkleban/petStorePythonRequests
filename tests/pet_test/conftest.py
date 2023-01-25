import pytest
from src.base_classes.response import Response
from src.backend_steps import pet_steps
from src.genenrators.pet import Pet


@pytest.fixture
def make_pet_data():
    response = Response(pet_steps.add_pet_to_the_store(Pet().build()))\
        .assert_status_code(200)
    return response.response_json
