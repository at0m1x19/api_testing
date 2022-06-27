from requests import get


def test_status_code(url, expected_status_code):
    response = get(url)
    assert response.status_code == expected_status_code
