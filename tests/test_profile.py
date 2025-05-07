from pages.login_page import LoginPage
from seleniumbase import BaseCase
from pages.profile_page import ProfilePage
from utils.locators import ProfilePageLocators

##login page -> login with admin  -> assert url
##tạo mới profile page -> fill form update (gọi hàm trong page) -> assert flash text -> assert profile updated

class ProfileTest(BaseCase):
    def test_update_profile(self):
        login_page = LoginPage(self.driver)
        login_page.login("admin")        
        self.assert_url_contains("dashboard")
        profile_page = ProfilePage(self.driver)
        profile_page.update_profile()
        self.assert_element(ProfilePageLocators.PROFILE_UPDATED_MESSAGE)
        self.click(ProfilePageLocators.MENU_BAR)
        self.assert_text("hoang", "#dropdown-2")
        self.assert_text("hoang@test.com", "#dropdown-2")
        
        
        
        
        
        