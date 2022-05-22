import pytest
from requests import get
from src.dog_api.schemas import list_all_breeds_schema, random_image_schema, by_breed_schema, list_all_sub_breed_schema
from src.dog_api.endpoints import BASE_URL, LIST_ALL_BREEDS, RANDOM_IMAGE, get_by_breed_endpoint, \
    get_list_sub_breed_endpoint

HOUND_BREED = 'hound'
HOUND_SUB_BREED_LIST = ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]
BY_BREED_HOUND = get_by_breed_endpoint(HOUND_BREED)
LIST_ALL_SUB_BREEDS_HOUND = get_list_sub_breed_endpoint(HOUND_BREED)

endpoints_list = [LIST_ALL_BREEDS, RANDOM_IMAGE, BY_BREED_HOUND, LIST_ALL_SUB_BREEDS_HOUND]
description_list = ['List of all breeds', 'Random image', 'By breed', 'List all sub breed']


@pytest.mark.parametrize('endpoint', endpoints_list, ids=description_list)
def test_successful_status_code(endpoint):
    response = get(BASE_URL + endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint', endpoints_list, ids=description_list)
def test_content_type_json(endpoint):
    response = get(BASE_URL + endpoint)
    assert response.headers['Content-Type'] == 'application/json'


@pytest.mark.parametrize('endpoint, schema', [
    (LIST_ALL_BREEDS, list_all_breeds_schema),
    (RANDOM_IMAGE, random_image_schema),
    (BY_BREED_HOUND, by_breed_schema),
    (LIST_ALL_SUB_BREEDS_HOUND, list_all_sub_breed_schema)
], ids=description_list)
def test_valid_response_schema(endpoint, schema, _validator):
    response = get(BASE_URL + endpoint)
    assert _validator.validate(response.json(), schema)


@pytest.mark.parametrize('endpoint', endpoints_list, ids=description_list)
def test_status_field_success(endpoint):
    response = get(BASE_URL + endpoint)
    assert response.json()['status'] == 'success'


def test_retrieve_list_sub_breeds():
    response = get(BASE_URL + LIST_ALL_SUB_BREEDS_HOUND)
    assert response.json()['message'] == HOUND_SUB_BREED_LIST
