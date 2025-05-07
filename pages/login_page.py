from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from utils.locators import LogoutPageLocators

class LoginPage(BasePage):
    page_uri = "login"
    def login(self, role = "admin"):
        self.open(self.page_url)
        self.type(LoginPageLocators.EMAIL_INPUT, self.env.get_username(role))
        self.type(LoginPageLocators.PASSWORD_INPUT, self.env.get_password(role))
        print(self.env.get_username(role))
        print(self.env.get_password(role))
        self.click(LoginPageLocators.LOGIN_BUTTON)
        
    def forgetPassword():
        pass
    
    def logout(self):
        self.click(LogoutPageLocators.MENU_BAR)
        self.click(LogoutPageLocators.LOGOUT_BUTTON)