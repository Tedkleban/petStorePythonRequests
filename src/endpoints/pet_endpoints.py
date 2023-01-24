class PetEndpoint(str):
    PET_ENDPOINT: str = "/pet"
    GET_PET_BY_STATUS_ENDPOINT = "/pet/findByStatus?status="
    GET_PET_BY_TAG_ENDPOINT = "/pet/findByTags?tags="
    UPLOAD_PET_IMAGE_ENDPOINT = "/pet/uploadImage"
