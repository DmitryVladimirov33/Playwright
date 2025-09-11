from playwright.sync_api import sync_playwright


def test_run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    search_box = page.get_by_placeholder('Username')
    search_box.fill("standard_user")
    search_box = page.get_by_placeholder('Password')
    search_box.fill("secret_sauce")

    page.locator('[data-test="login-button"]').click()

    page.wait_for_timeout(2000)
    browser.close()

# with sync_playwright() as playwright:
#     test_run(playwright)
