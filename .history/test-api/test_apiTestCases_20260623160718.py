import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.api
def test_api(playwright):
    context=playwright.reqquest.new_context()
    