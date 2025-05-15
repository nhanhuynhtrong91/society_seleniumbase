from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class FormComponent:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    def submit(self):
        if self.submitBtn:
            self.submitBtn.click()

    def setForm(self, formLocator: str):
        self.form = self.driver.find_element(By.CSS_SELECTOR, formLocator)

    def setSubmitBtn(self, submitBtnLocator: str):
        self.submitBtn = self.driver.find_element(By.CSS_SELECTOR, submitBtnLocator)
        
    def fillForm(self, dataToFill: dict):
        for key, value in dataToFill.items():
            # TODO
            pass
            
# Usage
# form = FormComponent(WebDriver(), "button[type='submit']")
# form.submit()

# form = FormComponent(WebDriver())
# form.setSubmitBtn("button[type='submit']")
# form.submit()
