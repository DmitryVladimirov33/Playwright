from playwright.sync_api import Playwright


def test_expert_ui(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://msk.mrtexpert.ru/about")
    page.wait_for_load_state("networkidle")
    page.locator("a.button-sm.button-border-gray-650[href='https://www.telemedex.ru']").click()
    page.goto("https://www.telemedex.ru/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Продолжить").click()
    page.goto("https://app.telemedex.ru/telemedex/patient/login")
    page.wait_for_load_state("networkidle")
    page.set_default_navigation_timeout(60)
    page.get_by_role("button", name="Зарегистрироваться").click()
    page.get_by_role("button", name="Вход в личный кабинет").click()

    context.close()
    browser.close()


# def test_expert_ui_1(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://msk.mrtexpert.ru/about")
#     page.wait_for_load_state("networkidle")
#     with page.expect_popup() as page1_info:
#         page.locator("a.button-sm.button-border-gray-650[href='https://www.telemedex.ru']").click()
#     page1 = page1_info.value
#     page1.wait_for_url('https://www.telemedex.ru/')
#     page1.get_by_role("link", name="Продолжить").click()
#     page1.goto("https://app.telemedex.ru/telemedex/patient/login")
#     page1.set_default_navigation_timeout(60)
#     page1.get_by_role("button", name="Зарегистрироваться").click()
#     page1.get_by_role("button", name="Вход в личный кабинет").click()

    context.close()
    browser.close()
