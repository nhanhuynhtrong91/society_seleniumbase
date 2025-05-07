from pages.list_page import ListPage
from utils.locators import ListPageLocators
from selenium.webdriver.common.by import By

class ListPageWithFilter(ListPage):
    def filter_by(self, filter_text):
        self.type(ListPageLocators.FILTER_INPUT, filter_text)
        
    def getFilters(self):
        self.filters = self.find_elements('[wire\\:key="' + self.filter_section_key + '"] > div:not(.block) div.relative')
        
    def getOptionsByFilter(self, filter_text):
        self.target = None
        self.options = []
        
        for filter in self.filters:
            # Tìm tất cả phần tử con có thuộc tính wire:model.live
            children = filter.find_elements(By.CSS_SELECTOR, '[wire\\:model\\.live]')
            for child in children:
                value = child.get_attribute('wire:model.live')
                #tuơng đương với selector [wire\:model\.live="$filter_text"]
                if value == filter_text:
                    if self.target is None:
                        self.target = filter
                        
                    self.options.append(child)
                               
            if self.target:
                break
    
    def selectOption(self, option):
        if self.target:
            self.target.click()
            valueToFilter = "Yes"
            
            self.options[1].click()
            
            self.wait(2)
            
            return True
        return False