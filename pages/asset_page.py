from pages.base_page import BasePage
from utils.locators import ProfilePageLocators

class AssertPage(BasePage):
    page_uri = "user/assets"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def update_profile(self):
        self.open(self.page_url)
        self.type(ProfilePageLocators.NAME_INPUT, "hoang")
        self.type(ProfilePageLocators.EMAIL_INPUT, "hoang@test.com")
        self.click(ProfilePageLocators.SAVE_BUTTON)
        

        
   
        
    
    
    