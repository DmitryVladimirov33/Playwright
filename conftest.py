import pytest


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
