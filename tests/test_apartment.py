
from pages.apartment_page import ApartmentPage
from pages.login_page import LoginPage
from utils.environment import Environment
import pytest
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from utils.locators import FiltersSection

class ApartmentTests(BaseCase):

    def test_apartment_page(self):
        
        login_page = LoginPage(self.driver)
        login_page.login("admin")
        self.assert_url_contains("dashboard") 
        
        apartment_page = ApartmentPage(self.driver)
        self.assert_url_contains("apartment")
        if not self.is_element_present(FiltersSection.FILTERS_SECTION):
            self.click('[wire\:key="apartment-management"] .items-center form + button')
        apartment_page.getFilters()
        apartment_page.getOptionsByFilter("filterStatuses")
        valueToFilter = "Rented"
        if apartment_page.selectOption(valueToFilter):
            results = self.find_elements("table tbody tr")
            matchRows = 0
            for element in results:
                element = self.driver.find_element(By.XPATH, '//span[normalize-space(text())="On Rent"]')
                if element and element.text == "On Rent":
                    matchRows += 1
                
            self.assert_equal(matchRows, len(results))
        