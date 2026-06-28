import pytest
from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.api
def test_api(playwright):
    context=playwright.req