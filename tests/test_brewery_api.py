import pytest
from requests import get
from src.brewery_api.endpoints import BASE_URL, SINGLE_BREWERY, LIST_BREWERIES, RANDOM, SEARCH, SORT_BY_CITY_PARAMETER, \
    FILTER_BY_NAME_PARAMETER, FILTER_BY_TYPE_PARAMETER, FILTER_BY_STATE_PARAMETER, FILTER_BY_DISTANCE_PARAMETER, \
    FILTER_BY_POSTAL_CODE_PARAMETER, OFFSET_OR_PAGE_PARAMETER, PER_PAGE_PARAMETER, QUERY_PARAMETER, AUTOCOMPLETE
from src.brewery_api.schemas import brewery_schema, autocomplete_schema
from src.schema_validation import assert_schema

BREWERY_ID = 'madtree-brewing-cincinnati'
SEARCH_QUERY = 'dog'
AUTOCOMPLETE_QUERY = 'dog'
CITY = 'san_diego'
COORDINATES = '38.8977,77.0365'
NAME = 'cooper'
STATE = 'new_york'
POSTCODE = '44107'
TYPE = 'micro'
OFFSET_OR_PAGE = 15
PER_PAGE = 2

PARAMETERS = [
    (SINGLE_BREWERY + BREWERY_ID, '', '', brewery_schema),
    (RANDOM, '', '', brewery_schema),
    (LIST_BREWERIES, '', '', brewery_schema),
    (SEARCH, QUERY_PARAMETER, SEARCH_QUERY, brewery_schema),
    (AUTOCOMPLETE, QUERY_PARAMETER, AUTOCOMPLETE_QUERY, autocomplete_schema),
    ('', SORT_BY_CITY_PARAMETER, CITY, brewery_schema),
    ('', FILTER_BY_DISTANCE_PARAMETER, COORDINATES, brewery_schema),
    ('', FILTER_BY_NAME_PARAMETER, NAME, brewery_schema),
    ('', FILTER_BY_STATE_PARAMETER, STATE, brewery_schema),
    ('', FILTER_BY_POSTAL_CODE_PARAMETER, POSTCODE, brewery_schema),
    ('', FILTER_BY_TYPE_PARAMETER, TYPE, brewery_schema),
    ('', OFFSET_OR_PAGE_PARAMETER, OFFSET_OR_PAGE, brewery_schema),
    ('', PER_PAGE_PARAMETER, PER_PAGE, brewery_schema)
]

DESCRIPTION_LIST = [
    'Single brewery', 'Random', 'List of breweries', f'Search: {SEARCH_QUERY}',
    f'Autocomplete for: {AUTOCOMPLETE_QUERY}', f'By city: {CITY}', f'By distance from {COORDINATES}',
    f'By name: {NAME}', f'By state: {STATE}', f'By postcode: {POSTCODE}',
    f'By type: {TYPE}', f'Offset or page: {OFFSET_OR_PAGE}', f'Per page: {PER_PAGE}'
]


@pytest.mark.parametrize('endpoint, parameter, value, schema', PARAMETERS, ids=DESCRIPTION_LIST)
def test_successful_status_code(endpoint, parameter, value, schema):
    response = get(BASE_URL + endpoint, params={parameter: value})
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint, parameter, value, schema', PARAMETERS, ids=DESCRIPTION_LIST)
def test_content_type_json(endpoint, parameter, value, schema):
    response = get(BASE_URL + endpoint, params={parameter: value})
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


@pytest.mark.parametrize('endpoint, parameter, value, schema', PARAMETERS, ids=DESCRIPTION_LIST)
def test_valid_response_schema(endpoint, parameter, value, schema, _validator):
    response = get(BASE_URL + endpoint, params={parameter: value})
    assert response.json()
    assert_schema(response=response.json(), schema=schema, validator=_validator)


def test_get_brewery_by_id():
    response = get(BASE_URL + SINGLE_BREWERY + BREWERY_ID)
    assert response.json()['id'] == BREWERY_ID


def test_valid_autocomplete():
    response = get(BASE_URL + AUTOCOMPLETE, params={QUERY_PARAMETER: AUTOCOMPLETE_QUERY})
    assert response.json()
    for brewery in response.json():
        assert AUTOCOMPLETE_QUERY in brewery['id']
        assert AUTOCOMPLETE_QUERY in brewery['name'].lower()
