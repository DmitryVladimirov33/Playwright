from playwright.sync_api import Playwright


def test_expert_ui(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://msk.mrtexpert.ru/about")
    with page.expect_popup() as page1_info:
        page.get_by_role("banner").get_by_role("link", name="Онлайн-консультация").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="Продолжить").click()
    page1.goto("https://app.telemedex.ru/telemedex/patient/login")
    page1.set_default_navigation_timeout(60)
    page1.get_by_role("button", name="Зарегистрироваться").click()
    page1.get_by_role("button", name="Вход в личный кабинет").click()

    context.close()
    browser.close()


def test_expert(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://msk.mrtexpert.ru/about")
    with page.expect_popup() as page1_info:
        page.get_by_role("banner").get_by_role("link", name="Онлайн-консультация").click()

    context.close()
    browser.close()
