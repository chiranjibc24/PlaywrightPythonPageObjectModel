import allure
import re
from playwright.sync_api import sync_playwright, expect

class homePage:

    def __init__(self,page):
        self.page = page
        self.searchBox = page.locator("input#twotabsearchtextbox")
        self.menuIcon = page.get_by_label("Open All Categories Menu")
        self.accountsndList = page.locator("//span[contains(text(),'Account & Lists')]")

    @allure.step("Wait for the search box to become visible")
    def waitingForSearchBoxToBeVisible(self):
        self.searchBox.wait_for(state="visible", timeout=50000)

    @allure.step("Verify the search box is visible")
    def validateVisibilityOfSeachBox(self):
         self.searchBox.wait_for(state="visible", timeout=60000)

    @allure.step("Verify the Amazon page title")
    def verifyTitle(self):
        expect(self.page).to_have_title(re.compile(r"Amazon.*India|Amazon\.in", re.IGNORECASE), timeout=20000)

    @allure.step("Verify the menu icon is visible")
    def validateTheVisibityOfMenu(self):
        expect(self.menuIcon).to_be_visible()

    @allure.step("Open Account and Lists")
    def clickOnAccountsndList(self):
        self.accountsndList.click()

    @allure.step("Enter a search query")
    def enterSearchText(self, text):
        self.searchBox.fill(text)

    @allure.step("Submit the search")
    def clickOnSearchBtn(self):
        self.searchBox.press("Enter")
    
    