import allure
import pytest
from allure_commons.types import Severity

from config import settings

from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.courses # Добавили маркировку Courses
@pytest.mark.regression # Добавили маркировку Regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        # Проверяем отображение компонента Navbar
        courses_list_page.navbar.check_visible(settings.test_user.username)
        # Проверяем отображение компонента Sidebar
        courses_list_page.sidebar.check_visible()

        # Проверяем отображение заголовка "Courses"
        courses_list_page.toolbar_view.check_visible()
        # Проверяем отображение пустого блока с текстом "There is no results"
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_courses_page: CreateCoursePage):
        courses_list_page.visit(AppRoute.COURSES_CREATE)

        # Проверяем наличие Navbar
        create_courses_page.navbar.check_visible(settings.test_user.username)

        # Проверяем наличие заголовка "Create course"
        # Проверяем, что кнопка создания курса недоступна для нажатия
        create_courses_page.create_course_toolbar_view.check_visible()

        # Проверяем, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
        create_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)

        # Проверяем, что форма создания курса отображается и содержит значения по умолчанию
        create_courses_page.create_course_form.check_visible()

        # Проверяем, наличие заголовка "Exercises"
        # Проверяем, наличие кнопки создания задания
        create_courses_page.create_exercise_toolbar_view.check_visible()

        # Проверяем, что отображается блок с пустыми заданиями
        create_courses_page.check_visible_exercises_empty_view()

        # Загружаем изображение для превью курса
        create_courses_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        # Проверяем, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # Заполняем форму создания курса
        create_courses_page.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        # Проверяем корректность данных
        create_courses_page.create_course_form.check_visible(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )

        # Проверяем, что кнопка Create Course доступна для нажатия
        create_courses_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
        # Кликаем на кнопку создания курса
        create_courses_page.create_course_toolbar_view.click_create_course_button()

        # Проверяем наличие заголовка "Courses"
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.toolbar_view.check_visible_create_course_button()
        # Проверяем корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_courses_page: CreateCoursePage):
        courses_list_page.visit(AppRoute.COURSES_CREATE)

        # Загружаем изображение для превью курса
        create_courses_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        # Заполняем форму создания курса
        create_courses_page.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        # Кликаем на кнопку создания курса
        create_courses_page.create_course_toolbar_view.click_create_course_button()
        # Проверяем корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )
        # Кликаем на кнопку Edit
        courses_list_page.course_view_menu.click_edit(index=0)

        # Заполняем форму редактирования курса новыми данными
        create_courses_page.create_course_form.fill(
            title='Edit Test',
            estimated_time='1 week',
            description='Edit Test',
            max_score='110',
            min_score='20'
        )

        # Кликаем на кнопку сохранения изменений
        create_courses_page.create_course_toolbar_view.click_create_course_button()
        # Проверяем корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0,
            title='Edit Test',
            max_score='110',
            min_score='20',
            estimated_time='1 week'
        )


