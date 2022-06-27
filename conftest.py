import pytest
import cerberus


@pytest.fixture(scope='session')
def _validator():
    validator = cerberus.Validator()
    yield validator
    del validator


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def expected_status_code(request):
    return request.config.getoption("--status_code")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        type=str,
        default="https://ya.ru",
        help="An URL to check status"
    )

    parser.addoption(
        "--status_code",
        type=int,
        default=200,
        help="Expected status code"
    )
