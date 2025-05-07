from seleniumbase import BaseCase
from pages.login_page import LoginPage
from pages.service_management_page import ServiceManagementPage
from utils.locators import Table
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestServiceManagement(BaseCase):
    def testFilterFunction(self):
        labelText = "Pet Walker"
        serviceIdxCol = 3
        
        loginPage = LoginPage(self.driver)
        loginPage.login()
        serviceManagementPage = ServiceManagementPage(self.driver)
        serviceManagementPage.clickFilterButtonByLabel(labelText)
        
        self.sleep(2)
        
        result = self.find_elements(Table.ROW)
        match = 0
        
        self.find_element("body").send_keys(Keys.END)
        self.sleep(2)
        
        for row in result:
            cell = row.find_element(By.CSS_SELECTOR, Table.CELL + ":nth-child(" + str(serviceIdxCol) + ")")
            if cell and cell.text == labelText:
                match += 1
                
        self.assert_equal(match, len(result))