from src.base_classes.response import Response
from src.responses_dict.resp_dict import RespDicts
from src.backend_steps import pet_steps
from src.enums.pet_status import PetStatus
import json
import pytest


@pytest.mark.parametrize("status", PetStatus.list())
def test_add_pet_and_pet_by_pet_id(status, get_pet_generator):
    pet_data = get_pet_generator.set_status(status).build()
    pet_data_dict: dict = json.loads(pet_data)
    pet_id = pet_data_dict.get('id')

    response_add = Response(pet_steps.add_pet_to_the_store(pet_data))

    response_add.assert_status_code(200)
    response_add.check_response_scheme(RespDicts.PET)
    response_add.check_response_values(pet_data_dict)

    response_get = Response(pet_steps.find_pet_by_id(pet_id))

    response_get.assert_status_code(200)
    response_get.check_response_scheme(RespDicts.PET)
    response_add.check_response_values(pet_data_dict)
