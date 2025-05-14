from seleniumbase import BaseCase
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.locators import DashboardLocators
from selenium.webdriver.common.by import By

class TestDashboard(BaseCase):
    def testOpenBookingModal(self):        
        loginPage = LoginPage(self.driver)
        loginPage.login()
        dashboardPage = DashboardPage(self.driver)
        dashboardPage.openBookingModal()
        self.wait_for_element(DashboardLocators.BOOKING_MODAL + " " + DashboardLocators.MODAL_TITLE, timeout=10)
        modalTitle = dashboardPage.booking_modal.get_title((By.CSS_SELECTOR, DashboardLocators.BOOKING_MODAL + " " + DashboardLocators.MODAL_TITLE))
        self.assert_equal(modalTitle, "Amenity Booking Details")
        dashboardPage.closeBookingModal(DashboardLocators.BOOKING_MODAL + " " + DashboardLocators.CANCEL_BUTTON)
        self.sleep(2)
        
