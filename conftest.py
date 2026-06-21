import allure
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture()
def navigateAmazon(page):
    page.goto("http://www.amazon.in")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            allure.attach(page.screenshot(), name="Failed page ss", attachment_type=allure.attachment_type.PNG)

