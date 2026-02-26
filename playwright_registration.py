from playwright.sync_api import sync_playwright, expect


"""Запускаем Playwright в синхронном режиме"""
with sync_playwright() as playwright:
    """Открываем новую вкладку в брузере"""
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
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

    page.wait_for_timeout(5000)


