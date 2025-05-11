from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ModalComponent:
    def __init__(self, driver: WebDriver, modal_locator: tuple):
        self.driver = driver
        self.modal_element = self.driver.find_element(*modal_locator)

    def is_displayed(self) -> bool:
        return self.modal_element.is_displayed()

    def get_title(self, title_locator: tuple) -> str:
        title_element = self.modal_element.find_element(*title_locator)
        return title_element.text

    def get_body_text(self, body_locator: tuple) -> str:
        body_element = self.modal_element.find_element(*body_locator)
        return body_element.text

    def click_button(self, button_locator: tuple):
        button_element = self.modal_element.find_element(*button_locator)
        button_element.click()

    def close(self, close_button_locator: tuple):
        close_button = self.modal_element.find_element(*close_button_locator)
        close_button.click()

