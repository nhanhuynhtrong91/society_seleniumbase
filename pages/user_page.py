from list_page_with_filter import ListPageWithFilter
from utils.locators import UserLocators

class UserPage(ListPageWithFilter):
    def filter_by(self, filter_text):
        self.type(UserLocators.FILTER_INPUT, filter_text)
        self.click(UserLocators.FILTER_BUTTON)