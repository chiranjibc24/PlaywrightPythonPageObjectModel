import allure
import re
from playwright.sync_api import sync_playwright, expect

class homePage:

    def __init__(self,page):
        self.page = page
        self.searchBox = page.locator("input#twotabsearchtextbox")
        self.menuIcon = page.get_by_label("Open All Categories Menu")
        self.accountsndList = page.locator("//span[contains(text(),'Account & Lists')]")

    @allure.step("waitingForSearchBoxToBeVisible")
    def waitingForSearchBoxToBeVisible(self):
        self.searchBox.wait_for(state="visible", timeout=50000)

    @allure.step("validateVisibilityOfSeachBox")
    def validateVisibilityOfSeachBox(self):
         self.searchBox.wait_for(state="visible", timeout=60000)

    @allure.step("verifyTitle")
    def verifyTitle(self):
        expect(self.page).to_have_title(re.compile(r"Amazon.*India|Amazon\.in", re.IGNORECASE), timeout=20000)

    @allure.step("validateThevisibityOfMenu")
    def validateTheVisibityOfMenu(self):
        expect(self.menuIcon).to_be_visible()

    @allure.step("clickOnAccountsndList")
    def clickOnAccountsndList(self):
        self.accountsndList.click()

    @allure.step("enterSearchText")
    def enterSearchText(self, text):
        self.searchBox.fill(text)

    @allure.step("clickOnSearchBtn")
    def clickOnSearchBtn(self):
        self.searchBox.press("Enter")
    
    