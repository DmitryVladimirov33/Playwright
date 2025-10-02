from playwright.sync_api import Page
from page.simple_page import SimplePage


def test_simple_submit(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.check_button_exist()


def test_simple_click(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.button_click()
    simple_page.check_result_text_('Submitted')
