import allure
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture()
def navigateAmazon(page):
    page.goto("https://www.amazon.in")

    continue_btn = page.get_by_role("button", name="Continue shopping")

    try:
        continue_btn.wait_for(timeout=5000)
        continue_btn.click()
    except:
        pass

    page.wait_for_load_state("networkidle")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            allure.attach(page.screenshot(), name="Failed page ss", attachment_type=allure.attachment_type.PNG)

