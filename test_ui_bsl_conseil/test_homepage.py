import pytest
from pom.page_acceuil import HomePage
from playwright.sync_api import Playwright

@pytest.mark.regression
def test_homepage_element(setup):
    # Given

    page = setup
    homepage = HomePage(page)

    # When

    # Then
    homepage.check_homepage_elements()


@pytest.mark.regression
def test_homepage_menu(setup):
    # Given
    page = setup
    homepage = HomePage(page)

    # Then
    homepage.check_homepage_menu_elements()


