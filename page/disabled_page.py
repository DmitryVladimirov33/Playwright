from playwright.sync_api import expect
from page.base_page import BasePage

SELECT_STATE = '#id_select_state'
BUTTON = '#submit-id-submit'
RESULT = '#result-text'


class DisabledPage(BasePage):
    url = 'https://www.qa-practice.com/elements/button/disabled'

    def check_state_exist(self):
        elem = self.page.locator(SELECT_STATE)
        expect(elem).to_be_visible()

    def state_choice(self):
        button = self.page.locator(SELECT_STATE)
        button.select_option("Enabled")

    def check_button_exist(self):
        button = self.page.locator(BUTTON)
        expect(button).to_be_visible()

    def button_click(self):
        button = self.page.locator(BUTTON)
        button.click()

    def check_result_text_(self, text):
        res = self.page.locator(RESULT)
        expect(res).to_have_text(text)

