import allure
from playwright.sync_api import expect

class loginPage:
    def __init__(self, page):
        self.page = page
        self.emailTextBox = page.locator("input#ap_email_login, input#ap_email")
        self.pwTextBox = page.locator("#ap_password")
        self.continueBtn = page.locator('[type="submit"]')
        self.signInHeader = page.get_by_text("Sign-In", exact=False)
        self.emailForm = page.get_by_label("Email or mobile phone number", exact=False)

    @allure.step("waitForSignInPage")
    def waitForSignInPage(self):
        self.signInHeader.wait_for(state="visible", timeout=30000)
        self.emailTextBox.wait_for(state="visible", timeout=30000)

    @allure.step("enterEmailValue")    
    def enterEmailValue(self, email):
        self.emailTextBox.fill(email)

    @allure.step("enterPw")
    def enterPw(self, pw):
        self.pwTextBox.fill(pw)

    @allure.step("clickOnContinueBtn")
    def clickOnContinueBtn(self):
        self.continueBtn.click()
