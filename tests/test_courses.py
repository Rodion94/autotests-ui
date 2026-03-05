import pytest
from playwright.sync_api import sync_playwright, expect

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

    page.wait_for_timeout(3000)
