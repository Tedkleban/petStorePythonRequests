from src.enums.pet_status import PetStatus
from src.genenrators.pet import Pet
from requests import get, post, put, delete
from conf import PetUrls


def get_pet_by_status(status: PetStatus):
    response = get(PetUrls.get_pet_by_status_url(status),
                   headers={'Accept': 'application/json'})
    return response


def get_pet_by_tags(tags: str):
    response = get(PetUrls.get_pet_by_tags_url(tags),
                   headers={'Accept': 'application/json'})
    return response


def update_pet(pet: Pet):
    response = put(PetUrls.PET_URL,
                   headers={'Content-Type': 'application/json',
                            'Accept': 'application/json'},
                   data=pet)
    return response


def update_pet_with_form_data(pet_id: str, name='nisimollit', status=PetStatus.AVAILABLE.value):
    response = post(PetUrls.get_pet_url_with_pet_id(pet_id),
                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                    data=f'name={name}&status={status}')
    return response


def add_pet_to_the_store(pet: Pet):
    response = post(PetUrls.PET_URL,
                    headers={
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    data=pet)
    return response


def upload_pet_image(pet_id: str):
    response = post(PetUrls.get_upload_image_with_pet_id_url(pet_id),
                    headers={
                        'Content-Type': 'multipart/form-data',
                        'Accept': 'application/json'
                    },
                    data={'additionalMetadata': 'voluptate dolor'},
                    files=[
                        ('file', ('file', open('/path/to/file', 'rb'), 'application/octet-stream'))
                    ])
    return response


def delete_pet(pet_id: str):
    response = delete(PetUrls.get_pet_url_with_pet_id(pet_id),
                      headers={
                          'api_key': 'special-key'
                      })
    return response


def find_pet_by_id(pet_id: str):
    response = get(PetUrls.get_pet_url_with_pet_id(pet_id),
                   headers={
                       'Accept': 'application/xml',
                       'api_key': 'special-key'
                   })
    return response
