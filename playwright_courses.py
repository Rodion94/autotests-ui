from playwright.sync_api import sync_playwright, expect


"""Запускаем Playwright в синхронном режиме"""
with sync_playwright() as playwright:
    """Открываем новую вкладку в брузере"""
    browser = playwright.chromium.launch(headless=False)

    """Создаем новый контекст браузера (новая сессия, которая изолирована от других)"""
    context = browser.new_context()

    """Открываем новую страницу в рамках контекста"""
    page = context.new_page()

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

    """Сохраняем состояние браузера"""
    context.storage_state(path="browser-state.json")



with sync_playwright() as playwright:
    """Открываем новую вкладку в брузере"""
    browser = playwright.chromium.launch(headless=False)

    """Создаем новый контекст браузера (новая сессия, которая изолирована от других)"""
    context = browser.new_context(storage_state="browser-state.json")

    """Открываем новую страницу в рамках контекста"""
    page = context.new_page()
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
