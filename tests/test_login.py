import pytest

from pages.home import homePage
from pages.login import loginPage

@pytest.mark.login
@pytest.mark.amazon
def test_positiveLogin(page, navigateAmazon):
    homePageObj = homePage(page)
    loginPageObj = loginPage(page)

    homePageObj.clickOnAccountsndList()
    loginPageObj.waitForSignInPage()
    assert loginPageObj.emailTextBox.is_visible()
    assert loginPageObj.continueBtn.is_enabled()