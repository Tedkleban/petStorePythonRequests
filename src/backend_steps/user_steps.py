from src.genenrators.user import User
from conf import UserUrls
from requests import get, put, delete, post


def get_user(username: str):
    response = get(UserUrls.get_user_url_with_username(username),
                   headers={'Accept': 'application/xml'})
    return response


def update_user(username: str, user: User):
    response = put(UserUrls.get_user_url_with_username(username),
                   headers={
                       'Content-Type': 'application/json',
                       'api_key': '<API Key>'
                   },
                   data=user)
    return response


def delete_user(username: str):
    response = delete(UserUrls.get_user_url_with_username(username),
                      headers={'api_key': 'special-key'})
    return response


def create_user(user: User):
    response = post(UserUrls.USER_URL,
                    headers={
                        'Content-Type': 'application/json',
                        'api_key': 'special-key'
                    },
                    data=user)
    return response


def create_list_users_with_array():
    payload = [
        User().build(),
        User().build()
    ]

    response = post(UserUrls.CREATE_WITH_ARRAY_URL,
                    headers={
                        'Content-Type': 'application/json',
                        'api_key': 'special-key'
                    },
                    data=payload)
    return response


def create_list_users_with_list():
    payload = [
        User().build(),
        User().build()
    ]

    response = post(UserUrls.CREATE_WITH_LIST_URL,
                    headers={
                        'Content-Type': 'application/json',
                        'api_key': 'special-key'
                    },
                    data=payload)
    return response


def login(username: str, password: str):
    response = get(UserUrls.get_login_url(username, password),
                   headers={'Accept': 'application/json'})
    return response


def logout():
    response = get(UserUrls.LOGOUT_URL,
                   headers={'api_key': 'special-key'})
    return response
