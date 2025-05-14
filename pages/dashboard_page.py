# pages/owner_page.py
from pages.base_page import BasePage
from utils.locators import DashboardLocators
# from utils.locators import BaseLocators
from pages.components.modal import ModalComponent
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    page_uri = "dashboard"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modal Today's Bookings
        self.booking_button = self.find_element(DashboardLocators.BOOKING_BTN)
        self.booking_modal = ModalComponent(self.driver, (By.CSS_SELECTOR, DashboardLocators.BOOKING_MODAL))
        self.rent_detail_button = self.find_element(DashboardLocators.RENT_DETAILS_BTN)
        self.rent_detail_modal = ModalComponent(self.driver, (By.CSS_SELECTOR, DashboardLocators.RENT_DETAILS))
        

    def openBookingModal(self):
        self.booking_button.click()
        
    def closeBookingModal(self):
        self.find_element(DashboardLocators.BOOKING_MODAL + " " + DashboardLocators.CANCEL_BUTTON).click()
        
    def openRentDetailModal(self):
        self.rent_detail_button.click()
        
    def closeRentDetailModal(self):
        self.find_element(DashboardLocators.RENT_DETAILS + " " + DashboardLocators.CANCEL_BUTTON).click()
        
    
