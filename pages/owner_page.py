# pages/owner_page.py
from pages.list_page_with_filter import ListPageWithFilter
from utils.locators import OwnerPageLocators
from utils.locators import BaseLocators

class OwnerPage(ListPageWithFilter):
    page_uri = "owners"
    filter_section_key = "owner-management"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def click_create_owner_button(self):
        self.click(OwnerPageLocators.CREATE_OWNER_BUTTON)

    def fill_owner_form(self, owner):
        self.type(OwnerPageLocators.FIRST_NAME_INPUT, owner.first_name)
        self.type(OwnerPageLocators.LAST_NAME_INPUT, owner.last_name)
        self.type(OwnerPageLocators.EMAIL_INPUT, owner.email)
        self.type(OwnerPageLocators.PHONE_INPUT, owner.phone)

    def click_save_button(self):
        self.click(BaseLocators.SAVE_BUTTON)

    def create_owner(self, owner):
        self.click_create_owner_button()
        self.fill_owner_form(owner)
        self.click_save_button()

    def assert_owner_created(self, owner):
        self.assert_text(owner.first_name, OwnerPageLocators.OWNER_TABLE)

    def verify_error_message(self):
        self.assert_element_visible(BaseLocators.ERROR_MESSAGE)
