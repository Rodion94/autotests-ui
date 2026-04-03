from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы элементов страницы
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration Button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login Link')

        # Добавляем компонент проверки отображения формы регистрации
        self.registration_form = RegistrationFormComponent(page)

    # Метод для нажатия на кнопку "Login"
    def click_registration_button(self):
        self.registration_button.click()

    # Метод для нажатия на ссылку "Login"
    def click_login_link(self):
        self.login_link.click()



