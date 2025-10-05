from playwright.sync_api import Page
from page.disabled_page import DisabledPage


def test_check_state_exist(page: Page):
    state = DisabledPage(page)
    state.open()
    state.check_state_exist()


def test_button_exist(page: Page):
    button = DisabledPage(page)
    button.open()
    button.check_button_exist()


def test_button_click(page: Page):
    button = DisabledPage(page)
    button.open()
    button.state_choice()
    button.button_click()
    button.check_result_text_('Submitted')
