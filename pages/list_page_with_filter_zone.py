from pages.list_page_with_filter import ListPageWithFilter
from utils.locators import FiltersSection
from selenium.webdriver.common.by import By

class ListPageWithFilterZone(ListPageWithFilter):
    def clickFilterButtonByLabel(self, labelText):
        filterButtons = self.find_elements(FiltersSection.FILTER_ZONE + " " + FiltersSection.FILTER_OPTION_BUTTON)
        for button in filterButtons:
            if button.text == labelText:
                button.click()
                break