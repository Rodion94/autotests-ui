import pytest
from playwright.sync_api import sync_playwright, expect
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

@pytest.mark.courses # Добавили маркировку Courses
@pytest.mark.regression # Добавили маркировку Regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state


    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    """Проверяем наличие и текст заголовка "Courses"""
    courses_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text('Courses')

    """Проверяем наличие и видимость иконки пустого блока"""
    empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_block_icon).to_be_visible()

    """Проверяем наличие и текст блока "There is no results"""
    no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_visible()
    expect(no_results_text).to_have_text('There is no results')

    """Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"""
    block_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_description_text).to_be_visible()
    expect(block_description_text).to_have_text('Results from the load test pipeline will be displayed here')

@pytest.mark.courses # Добавили маркировку Courses
@pytest.mark.regression # Добавили маркировку Regression
def test_create_course(courses_list_page: CoursesListPage,create_courses_page: CreateCoursePage):
    courses_list_page.visit(' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    # Проверяем наличие заголовка "Create course"
    create_courses_page.check_visible_create_course_title()
    # Проверяем, что кнопка создания курса недоступна для нажатия
    create_courses_page.check_disabled_create_course_button()
    # Проверяем, что отображается пустой блок для просмотра изображения
    create_courses_page.check_visible_image_preview_empty_view()
    # Проверяем, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_courses_page.check_visible_image_upload_view()
    # Проверяем, что форма создания курса отображается и содержит значения по умолчанию
    create_courses_page.check_visible_create_course_form(title='', description='', estimated_time='', max_score='0', min_score='0')
    # Проверяем, наличие заголовка "Exercises"
    create_courses_page.check_visible_exercises_title()
    # Проверяем, наличие кнопки создания задания
    create_courses_page.check_visible_create_exercise_button()
    # Проверяем, что отображается блок с пустыми заданиями
    create_courses_page.check_visible_exercises_empty_view()
    # Загружаем изображение для превью курса
    create_courses_page.upload_preview_image('./testdata/files/image.png')
    # Проверяем, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_courses_page.check_visible_image_upload_view(is_image_uploaded=True)
    # Заполняем форму создания курса
    create_courses_page.fill_create_course_form(title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10')
    # Кликаем на кнопку создания курса
    create_courses_page.click_create_course_button()
    # Проверяем наличие заголовка "Courses"
    courses_list_page.check_visible_courses_title()
    # Проверяем наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    # Проверяем корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(index=0, title='Playwright', estimated_time='2 weeks', max_score='100', min_score='10')


