
from pages.list_page_with_filter import ListPageWithFilter
from utils.locators import AmenitiesPageLocators
from utils.locators import BaseLocators

class AmenityPage(ListPageWithFilter):
    page_uri = "amenities"
    filter_section_key = "amenities-management"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def click_create_amenity_button(self):
        self.click(AmenitiesPageLocators.CREATE_OWNER_BUTTON)

    def fill_amenity_form(self, amenity):
        self.type(AmenitiesPageLocators.FIRST_NAME_INPUT, amenity.first_name)
        self.type(AmenitiesPageLocators.LAST_NAME_INPUT, amenity.last_name)
        self.type(AmenitiesPageLocators.EMAIL_INPUT, amenity.email)
        self.type(AmenitiesPageLocators.PHONE_INPUT, amenity.phone)

    def click_save_button(self):
        self.click(BaseLocators.SAVE_BUTTON)

    def create_amenity(self, amenity):
        self.click_create_amenity_button()
        self.fill_amenity_form(amenity)
        self.click_save_button()

    def assert_amenity_created(self, amenity):
        self.assert_text(amenity.first_name, AmenitiesPageLocators.amenity_TABLE)

    def verify_error_message(self):
        self.assert_element_visible(BaseLocators.ERROR_MESSAGE)
