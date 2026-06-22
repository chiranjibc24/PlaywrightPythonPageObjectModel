from playwright.sync_api import Page, expect
import pytest
import allure
from pages.home import homePage
from pages.results import resultsPage

@pytest.mark.results
@pytest.mark.amazon
def test_validatingCartCount(page: Page, navigateAmazon ):
    homePageObj = homePage(page)
    resultsPageObj = resultsPage(page)
    homePageObj.enterSearchText("iphone 17")
    homePageObj.clickOnSearchBtn()
    resultsPageObj.wait_for_results_loaded()
    count_beforeAdding = resultsPageObj.getCartCount()
    resultsPageObj.addAnItmeToCart("iPhone 17")
    resultsPageObj.wait_for_cart_count_change(count_beforeAdding)
    count_AfterAdding = resultsPageObj.getCartCount()
    @allure.step("assertingCount")
    def assertingCount():
        assert int(count_AfterAdding) == int(count_beforeAdding) + 1
    assertingCount()
    