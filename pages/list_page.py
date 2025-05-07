from pages.base_page import BasePage
from utils.locators import ListPageLocators

class ListPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def click_export_button(self):
        self.click(ListPageLocators.EXPORT_BUTTON)

    def click_add_button(self):
        self.click(ListPageLocators.ADD_BUTTON)

    def get_data_table(self):
        return self.find_element(ListPageLocators.DATA_TABLE)

    def assert_item_in_table(self, item_name):
        self.assert_text(item_name, ListPageLocators.DATA_TABLE)
        
    