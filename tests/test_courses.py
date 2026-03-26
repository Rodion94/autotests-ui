import pytest
from playwright.sync_api import sync_playwright, expect
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

@pytest.mark.courses # Добавили маркировку Courses
@pytest.mark.regression # Добавили маркировку Regression
def test_empty_courses_list(courses_list_page: CoursesListPage):

    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем отображение компонента Navbar
    courses_list_page.navbar.check_visible('username')
    # Проверяем отображение компонента Sidebar
    courses_list_page.sidebar.check_visible()

    # Проверяем отображение заголовка "Courses"
    courses_list_page.toolbar_view.check_visible()
    # Проверяем отображение пустого блока с текстом "There is no results"
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses # Добавили маркировку Courses
@pytest.mark.regression # Добавили маркировку Regression
def test_create_course(courses_list_page: CoursesListPage,create_courses_page: CreateCoursePage):
    courses_list_page.visit(' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    # Проверяем наличие Navbar
    create_courses_page.navbar.check_visible('username')

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
    create_courses_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    # Проверяем, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # Заполняем форму создания курса
    create_courses_page.create_course_form.fill(title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10')
    # Проверяем корректность данных
    create_courses_page.create_course_form.check_visible(title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10')

    # Проверяем, что кнопка Create Course доступна для нажатия
    create_courses_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
    # Кликаем на кнопку создания курса
    create_courses_page.create_course_toolbar_view.click_create_course_button()

    # Проверяем наличие заголовка "Courses"
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.toolbar_view.check_visible_create_course_button()
    # Проверяем корректность отображаемых данных на карточке курса
    courses_list_page.course_view.check_visible_course_card(index=0, title='Playwright', estimated_time='2 weeks', max_score='100', min_score='10')


