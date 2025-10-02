from playwright.sync_api import Page
from page.like_a_button import LikeButton


def test_like_button_exist(page: Page):
    like_button = LikeButton(page)
    like_button.open()
    like_button.check_button_exist()


def test_like_button_click(page: Page):
    like_button = LikeButton(page)
    like_button.open()
    like_button.button_click()
    like_button.check_result_text_('Submitted')
