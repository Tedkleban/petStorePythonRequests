from src.endpoints.pet_endpoints import PetEndpoint
from src.endpoints.store_endpoints import StoreEndpoints
from src.endpoints.user_endpoints import UserEndpoints

PETSHOP_BASE_URL = "https://petstore.swagger.io/v2"


class PetUrls(str):
    PET_URL = PETSHOP_BASE_URL + PetEndpoint.PET_ENDPOINT
    GET_PET_BY_STATUS_URL = PETSHOP_BASE_URL + PetEndpoint.GET_PET_BY_STATUS_ENDPOINT
    GET_PET_BY_TAGS_URL = PETSHOP_BASE_URL + PetEndpoint.GET_PET_BY_TAG_ENDPOINT

    @staticmethod
    def get_upload_image_with_pet_id_url(pet_id: str):
        return PetUrls.PET_URL + f"/{pet_id}" + PetEndpoint.UPLOAD_PET_IMAGE_ENDPOINT

    @staticmethod
    def get_pet_url_with_pet_id(pet_id: str):
        return PetUrls.PET_URL + f"/{pet_id}"

    @staticmethod
    def get_pet_by_status_url(status: str):
        return PetUrls.GET_PET_BY_STATUS_URL + f"{status}"

    @staticmethod
    def get_pet_by_tags_url(tags: str):
        return PetUrls.GET_PET_BY_TAGS_URL + f"{tags}"


class StoreUrls(str):
    STORE_URL = PETSHOP_BASE_URL + StoreEndpoints.STORE_ENDPOINT
    INVENTORY_URL = PETSHOP_BASE_URL + StoreEndpoints.INVENTORY_ENDPOINT

    @staticmethod
    def get_store_url_with_order_id(order_id: str):
        return StoreUrls.STORE_URL + f"/{order_id}"


class UserUrls(str):
    USER_URL = PETSHOP_BASE_URL + UserEndpoints.USER_ENDPOINT
    LOGIN_URL = PETSHOP_BASE_URL + UserEndpoints.LOGIN_ENDPOINT
    LOGOUT_URL = PETSHOP_BASE_URL + UserEndpoints.LOGOUT_ENDPOINT
    CREATE_WITH_ARRAY_URL = PETSHOP_BASE_URL + UserEndpoints.CREATE_WITH_ARRAY_ENDPOINT
    CREATE_WITH_LIST_URL = PETSHOP_BASE_URL + UserEndpoints.CREATE_WITH_LIST_ENDPOINT

    @staticmethod
    def get_user_url_with_username(username: str):
        return UserUrls.USER_URL + f"/{username}"

    @staticmethod
    def get_login_url(username: str, password: str):
        return UserUrls.LOGIN_URL + f"?username={username}&password={password}"
