from requests import get, post, delete
from conf import StoreUrls
from src.genenrators.order import Order


def get_order_by_orderid(order_id: str):
    response = get(url=StoreUrls.get_store_url_with_order_id(order_id),
                   headers={
                       'Accept': 'application/json'
                   })
    return response


def delete_order_by_orderid(order_id: str):
    response = delete(url=StoreUrls.get_store_url_with_order_id(order_id))
    return response


def create_order(order: Order):
    response = post(url=StoreUrls.STORE_URL,
                    headers={
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    data=order)
    return response


def get_inventory_status():
    response = get(StoreUrls.INVENTORY_URL,
                   headers={
                       'Accept': 'application/json',
                       'api_key': 'special-key'
                   })
    return response
