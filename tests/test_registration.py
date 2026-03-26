import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage,):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.check_visible()
    registration_page.registration_form.fill_form('test@gmail.com', 'test_user', 'password')
    registration_page.registration_form.check_visible(email= 'test@gmail.com', username= 'test_user', password= 'password' )
    registration_page.click_registration_button()

    dashboard_page.toolbar_view.check_visible()
