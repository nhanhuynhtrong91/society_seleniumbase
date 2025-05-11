# pages/base_page.py
from utils.locators import LogoutPageLocators
from dataclasses import dataclass
from utils.environment import Environment

@dataclass
class BasePage(object):
    def __init__(self, driver, autoOpen = True):
        self.driver = driver
        if autoOpen:
            self.open(self.page_url)

    @property
    def env(self):
        return Environment()
    
    @property
    def page_url(self):
        if hasattr(self, 'page_uri'):
            return self.env.get_url() + "/" + self.page_uri
        return ""
    
    def open(self, url):
        self.driver.open(url)

    def click(self, locator):
        self.driver.click(locator)

    def type(self, locator, text):
        self.driver.type(locator, text)

    def wait(self, seconds):
        self.driver.sleep(seconds)
    
    def find_element(self, locator):
        return self.driver.find_element(locator)
        
    def find_elements(self, locator):
        return self.driver.find_elements(locator)

    def assert_element_visible(self, locator):
        self.driver.assert_element_visible(locator)
        
    def logout(self):
        self.driver.click(LogoutPageLocators.MENU_BAR)
        self.driver.click(LogoutPageLocators.LOGOUT_BUTTON)
        
    def get_page_url(self):
        return self.driver.get_current_url()
    