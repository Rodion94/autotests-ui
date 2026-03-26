import email

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')



    # Метод для заполнения формы авторизации
    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)


    def check_visible(self, email: str = None, password: str = None):
        expect(self.email_input).to_be_visible()
        if email is not None:
            expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        if password is not None:
            expect(self.password_input).to_have_value(password)
