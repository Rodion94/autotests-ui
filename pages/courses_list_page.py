from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolBarViewComponent
from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Пустой блок при отсутствии курсов
        self.empty_view = EmptyViewComponent(page, 'courses-list')

        self.course_view = CourseViewComponent(page)

        # Добавляем компонент SidebarComponent
        self.sidebar = SidebarComponent(page)
        # Добавляем компонент NavbarComponent
        self.navbar = NavbarComponent(page)

        self.toolbar_view = CoursesListToolBarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )


