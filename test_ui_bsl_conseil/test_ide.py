import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.mark.xfail(reason="url not ready")
def test_run_fail(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://bslconseiletprevention.fr/
    page.goto("https://bslconseiletprevention.fr/")

    # Act - When/And
    # Click text=☰ Menu
    page.locator("text=☰ Menu").click()

    # Assert - Then
    # Click #mySidepanel >> text=Prévention
    assert page.is_visible("#mySidepanel >> text=Prévention")
    page.locator("#mySidepanel >> text=Prévention").click(timeout=8000)

    # assert page.url == "https://bslconseiletprevention.fr/prevention.html"
    # Click text=> Votre Document Unique est-il à jour ?
    page.locator("text=> Votre Document Unique est-il à jour ?").click()

    # Click text=> En savoir plus sur la démarche ?
    page.locator("text=> En savoir plus sur la démarche ?").click()

    # Click text=> En savoir plus sur la démarche ?
    page.locator("text=> En savoir plus sur la démarche ?").click()

    # Click text=Réalisation du plan d’actions et suivi des actions d’amélioration
    page.locator("text=Réalisation du plan d’actions et suivi des actions d’amélioration").click()

    # ---------------------
    context.close()
    browser.close()


@pytest.mark.skip(reason="old fashion test")
def test_run(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://bslconseiletprevention.fr/
    page.goto("https://bslconseiletprevention.fr/")

    # Act - When/And
    # Click text=☰ Menu
    page.locator("text=☰ Menu").click()

    # Assert - Then
    # Click #mySidepanel >> text=Prévention
    assert page.is_visible("#mySidepanel >> text=Prévention")
    page.locator("#mySidepanel >> text=Prévention").click(timeout=8000)

    # assert page.url == "https://bslconseiletprevention.fr/prevention.html"
    # Click text=> Votre Document Unique est-il à jour ?
    page.locator("text=> Votre Document Unique est-il à jour ?").click()

    # Click text=> En savoir plus sur la démarche ?
    page.locator("text=> En savoir plus sur la démarche ?").click()

    # Click text=> En savoir plus sur la démarche ?
    page.locator("text=> En savoir plus sur la démarche ?").click()

    # Click text=Réalisation du plan d’actions et suivi des actions d’amélioration
    page.locator("text=Réalisation du plan d’actions et suivi des actions d’amélioration").click()

    # ---------------------
    context.close()
    browser.close()


@pytest.mark.legacy(reason="old framework")
def test_run_old(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://bslconseiletprevention.fr/
    page.goto("https://bslconseiletprevention.fr/")

    # Act - When/And
    # Click text=☰ Menu
    page.locator("text=☰ Menu").click()

    # Assert - Then
    # Click #mySidepanel >> text=Prévention
    assert page.is_visible("#mySidepanel >> text=Prévention")
    page.locator("#mySidepanel >> text=Prévention").click(timeout=8000)

    # assert page.url == "https://bslconseiletprevention.fr/prevention.html"
    # Click text=> Votre Document Unique est-il à jour ?
    page.locator("text=> Votre Document Unique est-il à jour ?").click()

    # Click text=> En savoir plus sur la démarche ?
    page.locator("text=> En savoir plus sur la démarche ?").click()

    # Click text=> En savoir plus sur la démarche ?
    page.locator("text=> En savoir plus sur la démarche ?").click()

    # Click text=Réalisation du plan d’actions et suivi des actions d’amélioration
    page.locator("text=Réalisation du plan d’actions et suivi des actions d’amélioration").click()

    # ---------------------
    context.close()
    browser.close()