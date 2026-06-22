import allure
from playwright.sync_api import sync_playwright, TimeoutError
import pytest

@pytest.fixture(autouse=True)
def default_page_timeouts(page):
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(60000)
    return page

@pytest.fixture()
def navigateAmazon(page):
    page.goto("https://www.amazon.in", wait_until="domcontentloaded")

    continue_btn = page.get_by_role("button", name="Continue shopping")

    try:
        continue_btn.wait_for(state="visible", timeout=5000)
        continue_btn.click()
    except TimeoutError:
        pass

    page.wait_for_load_state("load")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            allure.attach(page.screenshot(), name="Failed page ss", attachment_type=allure.attachment_type.PNG)

