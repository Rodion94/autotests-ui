import pytest

from playwright.sync_api import sync_playwright, Page, Playwright, expect


@pytest.fixture # Объявляем фикстуры, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright) -> Page: # Аннотируем возвращаемое фикстурой значение
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
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    """Заполняем поле Email"""
    email_registration_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_registration_input.fill('user.name@gmail.com')

    """Заполняем поле Username"""
    user_name_registration_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_name_registration_input.fill('username')

    """Заполняем поле Password"""
    password_registration_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_registration_input.fill('password')

    """Нажимаем на кнопку Registration"""
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    """Проверяем наличие надписи Dashboard"""
    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_have_text('Dashboard')

    """Сохраняем состояние браузера"""
    context.storage_state(path="browser-state.json")

    browser.close()

@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright) -> Page:
    """Фикстура для открытия страницы с сохраненным состоянием браузера"""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    # Передаем страницу в тест
    yield page

    # Очистка после теста
    context.close()
    browser.close()
