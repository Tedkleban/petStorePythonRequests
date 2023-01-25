import pytest
import json
from src.enums.order_status import OrderStatus
from src.base_classes.response import Response
from src.backend_steps import store_steps
from src.responses_dict.resp_dict import RespDicts


@pytest.mark.parametrize("status", OrderStatus.list())
def test_create_order(status, get_order_generator):
    order_data = get_order_generator.set_status(status).build()
    order_data_dict: dict = json.loads(order_data)

    response = Response(store_steps.create_order(order_data))

    response.assert_status_code(200)
    response.check_response_scheme(RespDicts.ORDER)
    response.check_response_values(order_data_dict)


def test_find_order_by_order_id(make_order_data):
    order_id = make_order_data.get('id')

    response = Response(store_steps.get_order_by_orderid(order_id))
    response.assert_status_code(200)
    response.check_response_scheme(make_order_data)
    response.check_response_values(make_order_data)


def test_delete_order_by_order_id(make_order_data):
    order_id = make_order_data.get('id')

    response_delete = Response(store_steps.delete_order_by_orderid(order_id))
    response_delete.assert_status_code(200)
    response_delete.check_response_scheme(RespDicts.SUCCESS)
    response_delete.check_value_in_json('code', 200)

    response_get = Response(store_steps.get_order_by_orderid(order_id))
    response_get.assert_status_code(404)
    response_get.check_response_scheme(RespDicts.ORDER_NOT_FOUND)
    response_get.check_value_in_json('code', 1)
    response_get.check_value_in_json('type', 'error')
    response_get.check_value_in_json('message', 'Order not found')


def test_get_store_inventory():
    Response(store_steps.get_inventory_status()) \
        .assert_status_code(200) \
        .check_json_is_not_empty()
