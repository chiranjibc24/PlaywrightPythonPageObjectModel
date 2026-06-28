from playwright.sync_api import sync_playwright, expect
import pytest

@mark.mark.api
def test_api():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        expect(page).to_have_title("Example Domain")
        browser.close() 