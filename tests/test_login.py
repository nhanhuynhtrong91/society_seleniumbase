from pages.login_page import LoginPage
from seleniumbase import BaseCase

class LoginTest(BaseCase):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("admin")        
        self.assert_url_contains("dashboard") 
        login_page.logout()
        self.assert_url_contains("login")
        
        
        