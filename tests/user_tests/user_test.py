from src.backend_steps import user_steps
from src.base_classes.response import Response
from src.responses_dict.resp_dict import RespDicts
import json


def test_create_user(get_user_generator):
    response = Response(user_steps.create_user(get_user_generator.build()))

    response.assert_status_code(200)
    response.check_response_scheme(RespDicts.SUCCESS)
    response.check_value_in_json('code', 200)


def test_get_user_by_username(get_user_data):
    username = get_user_data.get('username')
    requested_values: dict = get_user_data

    response = Response(user_steps.get_user(username))

    response.assert_status_code(200)
    response.check_response_scheme(RespDicts.USER_DATA)
    response.check_response_values(requested_values)


def test_update_user(get_user_data, get_user_generator):
    actual_data = get_user_data
    username = actual_data.get('username')
    update_data = get_user_generator.set_username(username).build()
    update_data_dict: dict = json.loads(update_data)

    response_update = Response(user_steps.update_user(username, update_data))

    response_update.assert_status_code(200)
    response_update.check_response_scheme(RespDicts.SUCCESS)

    response_get = Response(user_steps.get_user(username))

    response_get.assert_status_code(200)
    response_get.check_response_scheme(RespDicts.USER_DATA)
    response_get.check_response_values(update_data_dict)


def test_delete_user(get_user_data):
    username = get_user_data.get('username')

    response_delete = Response(user_steps.delete_user(username))

    response_delete.assert_status_code(200)
    response_delete.check_response_scheme(RespDicts.SUCCESS)
    response_delete.check_value_in_json('code', 200)

    response_get = Response(user_steps.get_user(username))

    response_get.assert_status_code(404)
    response_get.check_response_scheme(RespDicts.USER_NOT_FOUND)
    response_get.check_value_in_json('code', 1)
    response_get.check_value_in_json('type', 'error')
    response_get.check_value_in_json('message', 'User not found')


def test_user_login(get_user_data):
    username = get_user_data.get('username')
    password = get_user_data.get('password')

    response = Response(user_steps.login(username, password))

    response.assert_status_code(200)
    response.check_response_scheme(RespDicts.SUCCESS)
    response.check_value_in_json('code', 200)
