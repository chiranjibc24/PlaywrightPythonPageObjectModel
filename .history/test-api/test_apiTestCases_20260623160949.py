import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.api
def test_api(playwright):
    context=playwright.request.new_context()
    response=