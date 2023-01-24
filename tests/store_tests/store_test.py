import pytest
from src.enums.order_status import OrderStatus
from src.base_classes.response import Response
from src.backend_steps import store_steps


@pytest.mark.parametrize("status", OrderStatus.list())
def test_create_order(status, get_order_generator):
    playload = get_order_generator.set_status(status).build()
    request = store_steps.create_order(playload)
    print(request.json())
    Response(request).assert_status_code(200).check_json_is_not_empty()


def test_find_order_by_order_id(make_order_id):
    Response(store_steps.get_order_by_orderid(make_order_id)) \
        .assert_status_code(200) \
        .check_json_is_not_empty()


def test_delete_order_by_order_id(make_order_id):
    Response(store_steps.delete_order_by_orderid(make_order_id)) \
        .assert_status_code(200) \
        .check_json_is_not_empty()


def test_get_store_inventory():
    dictio: tuple[str, str, str] = 'sold', 'available', 'pending'

    Response(store_steps.get_inventory_status()) \
        .assert_status_code(200) \
        .check_json_is_not_empty() \
        .validate_json_scheme(dictio)
