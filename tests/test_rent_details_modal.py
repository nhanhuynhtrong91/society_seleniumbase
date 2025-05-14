from seleniumbase import BaseCase
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.locators import DashboardLocators
from selenium.webdriver.common.by import By

class TestDashboard(BaseCase): 
    def testOpenRentDetailModal(self):
        loginPage = LoginPage(self.driver)
        loginPage.login()
        dashboardPage = DashboardPage(self.driver)
        dashboardPage.openRentDetailModal()
        self.sleep(2)
        modalTitle = dashboardPage.rent_detail_modal.get_title((By.CSS_SELECTOR, DashboardLocators.RENT_DETAILS + " " + DashboardLocators.MODAL_TITLE))
        self.assert_equal(modalTitle, "View Rent Details")
        # dashboardPage.closeRentDetailModal(DashboardLocators.RENT_DETAILS + " " + DashboardLocators.CANCEL_BUTTON)
        # self.sleep(2)