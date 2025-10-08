from playwright.sync_api import expect
from page.base_page import BasePage
from page import locators


class LikeButton(BasePage):
    url = 'https://www.qa-practice.com/elements/button/like_a_button'

    def check_button_exist(self):
        button = self.page.locator(locators.LIKE_A_BUTTON)
        expect(button).to_be_visible()

    def button_click(self):
        button = self.page.locator(locators.LIKE_A_BUTTON)
        button.click()

    def check_result_text_(self, text):
        res = self.page.locator(locators.LIKE_A_RESULT)
        expect(res).to_have_text(text)
