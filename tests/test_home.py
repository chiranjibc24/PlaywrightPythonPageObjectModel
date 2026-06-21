
from playwright.sync_api import sync_playwright, expect
import pytest
from pages.home import homePage

@pytest.mark.home
@pytest.mark.amazon
def test_titleCheck(page,navigateAmazon):
    homePageObj = homePage(page)
    homePageObj.waitingForSearchBoxToBeVisible()
    homePageObj.verifyTitle()
    

@pytest.mark.home
@pytest.mark.amazon
def test_validate_UI_elements(page,navigateAmazon):
    homePageObj = homePage(page)
    homePageObj.validateTheVisibityOfMenu()
    homePageObj.validateVisibilityOfSeachBox()