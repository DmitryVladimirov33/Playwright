from playwright.sync_api import Playwright
import re


# def test_expert_ui(playwright: Playwright) -> None:
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
#
#     context.close()
#     browser.close()
#

def test_mrt(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://msk.mrtexpert.ru/about")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Да, верно").click()
    page.get_by_role("navigation").get_by_role("link", name="Цены").click()
    page.get_by_role("textbox", name="Поиск по названию").click()
    page.get_by_role("textbox", name="Поиск по названию").fill("мрт")
    page.get_by_role("button", name="box icon").first.click()
    page.get_by_role("listitem").filter(
        has_text="Магнитно-резонансная томография головного мозга топометрическая/Детальное тонкос").get_by_role(
        "link").click()
    page.get_by_role("link", name="Подготовка Подготовка").click()
    page.locator("section").filter(
        has_text="Запишитесь на приём Магнитно-резонансная томография головного мозга топометричес").get_by_role(
        "link").click()
    form = page.locator("body > div.bg-gray-75 > div > div > form > main > section:nth-child(2) > div > div")
    res = form.is_visible()
    if res:
        form.click()
        page.locator("div").filter(has_text=re.compile(r"^На Киевской$")).nth(1).click()

    context.close()
    browser.close()
