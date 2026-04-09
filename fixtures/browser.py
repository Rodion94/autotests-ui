import pytest
from playwright.sync_api import Page, Playwright

from fixtures.pages import registration_page
from pages.authentication.registration_page import RegistrationPage


@pytest.fixture # Объявляем фикстуры, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page: # Аннотируем возвращаемое фикстурой значение
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # Передаем страницу для использования в тесте
    yield browser.new_page()
    # Закрываем браузер после выполнения теста
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    """Создаем новый контекст браузера (новая сессия, которая изолирована от других)"""
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    """Сохраняем состояние браузера"""
    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright) -> Page:
    """Фикстура для открытия страницы с сохраненным состоянием браузера"""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    # Передаем страницу в тест
    yield context.new_page()
    browser.close()
