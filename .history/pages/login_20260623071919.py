import allure
from playwright.sync_api import expect

class loginPage:
    def __init__(self, page):
        self.page = page
        self.emailTextBox = page.locator("input#ap_email_login, input#ap_email")
        self.pwTextBox = page.locator("#ap_password")
        self.continueBtn = page.locator('[type="submit"]')
        self.signInHeader = page.locator('h1:has-text("Sign-In"), h1:has-text("Sign in"), h2:has-text("Sign-In"), h2:has-text("Sign in")')
        self.emailForm = page.get_by_label("Email or mobile phone number", exact=False)

    @allure.step("Wait for the sign-in page to load")
    def waitForSignInPage(self):
        self.emailTextBox.wait_for(state="visible", timeout=30000)

    @allure.step("Enter the email address")    
    def enterEmailValue(self, email):
        self.emailTextBox.fill(email)

    @allure.step("Enter the password")
    def enterPw(self, pw):
        self.pwTextBox.fill(pw)

    @allure.step("Click Continue")
    def clickOnContinueBtn(self):
        self.continueBtn.click()
