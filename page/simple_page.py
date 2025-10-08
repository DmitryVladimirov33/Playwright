from playwright.sync_api import expect
from page.base_page import BasePage
from page import locators


class SimplePage(BasePage):
    url = 'https://www.qa-practice.com/elements/button/simple'

    def check_button_exist(self):
        button = self.page.locator(locators.SIMPLE_PAGE_BUTTON)
        expect(button).to_be_visible()

    def button_click(self):
        button = self.page.locator(locators.SIMPLE_PAGE_BUTTON)
        button.click()

    def check_result_text_(self, text):
        res = self.page.locator(locators.SIMPLE_PAGE_RESULT)
        expect(res).to_have_text(text)
