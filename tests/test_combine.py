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
        dashboardPage.closeBookingModal()
        self.sleep(2)
        self.assert_false(dashboardPage.booking_modal.is_displayed())
        dashboardPage.openRentDetailModal()
        self.sleep(2)
        #print(dashboardPage.rent_detail_modal.is_displayed())
        modalTitle = dashboardPage.rent_detail_modal.get_title((By.CSS_SELECTOR, DashboardLocators.RENT_DETAILS + " " + DashboardLocators.MODAL_TITLE))
        self.assert_equal(modalTitle, "View Rent Details")
        dashboardPage.closeRentDetailModal()
        self.sleep(2)
        #print(dashboardPage.rent_detail_modal.is_displayed())
        self.assert_false(dashboardPage.rent_detail_modal.is_displayed())