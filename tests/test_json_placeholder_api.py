import pytest
import requests
from src.json_placeholder_api.schemas import schema
from src.schema_validation import assert_schema

BASE_POSTS_URL = 'https://jsonplaceholder.typicode.com/posts'
RESOURCE_ID = 1
CREATE_RESOURCE_BODY = {"title": "foo", "body": "bar", "userId": 101}
UPDATE_RESOURCE_BODY = {"title": "foo", "body": "bar", "userId": 1}
PATCH_RESOURCE_BODY = {"title": "boo"}

PARAMETERS = [
    (f'/{RESOURCE_ID}', 'get', {}),
    ('', 'get', {}),
    ('', 'post', CREATE_RESOURCE_BODY),
    (f'/{RESOURCE_ID}', 'put', UPDATE_RESOURCE_BODY),
    (f'/{RESOURCE_ID}', 'patch', PATCH_RESOURCE_BODY),
    (f'/{RESOURCE_ID}', 'delete', {})
]

DESCRIPTION_LIST = [f'Getting a resource by id: {RESOURCE_ID}', 'Listing all resources', 'Creating a resource',
                    'Updating a resource', 'Patching a resource', 'Deleting a resource']


@pytest.mark.parametrize('endpoint, method, body', PARAMETERS, ids=DESCRIPTION_LIST)
def test_successful_status_code(endpoint, method, body):
    response = requests.request(method, BASE_POSTS_URL + endpoint, json=body)
    assert response.ok


@pytest.mark.parametrize('endpoint, method, body', PARAMETERS, ids=DESCRIPTION_LIST)
def test_valid_response_schema(endpoint, method, body, _validator):
    response = requests.request(method, BASE_POSTS_URL + endpoint, json=body)
    assert_schema(response.json(), schema, _validator)


def test_resource_creation():
    response = requests.post(BASE_POSTS_URL, json=CREATE_RESOURCE_BODY)
    assert response.json()
    assert response.json()['title'] == CREATE_RESOURCE_BODY['title']
    assert response.json()['body'] == CREATE_RESOURCE_BODY['body']
    assert response.json()['userId'] == CREATE_RESOURCE_BODY['userId']


def test_resource_getting():
    response = requests.get(BASE_POSTS_URL + f'/{RESOURCE_ID}')
    assert response.json()['id'] == RESOURCE_ID


def test_resource_updating():
    response = requests.put(BASE_POSTS_URL + f'/{RESOURCE_ID}', json=UPDATE_RESOURCE_BODY)
    assert response.json()
    assert response.json()['id'] == RESOURCE_ID
    assert response.json()['title'] == UPDATE_RESOURCE_BODY['title']
    assert response.json()['body'] == UPDATE_RESOURCE_BODY['body']
    assert response.json()['userId'] == UPDATE_RESOURCE_BODY['userId']
