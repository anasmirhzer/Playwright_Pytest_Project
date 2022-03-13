# Config and common fixtures to all tests

import pytest
from playwright.sync_api import Playwright

base_url = {
    "LOCAL": "http://localhost:8081",
    "PRD": "https://bslconseiletprevention.fr",
}


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="PRD", help="Environment: LOCAL or PRD"
    )

@pytest.fixture
def get_environment(request):
    return request.config.getoption("--env")


@pytest.fixture
def setup(page, get_environment):
    page.goto(f"{base_url[get_environment]}")
    yield page
    page.close()

