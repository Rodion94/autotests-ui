from playwright.sync_api import sync_playwright, expect


def test_wrong_email_or_password_authorization():
    """Запускаем Playwright в синхронном режиме"""
    with sync_playwright() as playwright:
        """Открываем новую вкладку в брузере"""
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        """Заполняем поле Email"""
        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill("user@gmail.com")

        """Заполняем поле Password"""
        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill("password")

        """Нажимаем на кнопку Login"""
        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        """Проверяем, что появляется сообщение об ошибке"""
        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

        """Добавляем паузу"""
        page.wait_for_timeout(5000)
