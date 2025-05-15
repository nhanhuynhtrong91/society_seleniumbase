from pages.base_page import BasePage
from utils.locators import AssetDetailsPageLocators
from pages.components.modal import ModalComponent


class AssetDetailsPage(BasePage):
    page_uri = "user/assets"
    def __init__(self, driver, contextId: str):
        super().__init__(driver)
        self.driver = driver
        self.page_uri += f"/{contextId}"
        self.addApartmentModal = ModalComponent(self.driver).withForm()
        self.addIssueModal = ModalComponent(self.driver).withForm()
        
        self.addApartmentModal.form.setForm(AssetDetailsPageLocators.APARTMENT_FORM)
        self.addApartmentModal.form.setSubmitBtn(AssetDetailsPageLocators.SAVE_APARTMENT_BUTTON)
        self.addIssueModal.form.setForm(AssetDetailsPageLocators.ISSUE_FORM)
        self.addIssueModal.form.setSubmitBtn(AssetDetailsPageLocators.SAVE_ISSUE_BUTTON)
        
    def createApartmentModal(self, apartmentData):
        # TODO tạo tab component và navigate tới tab mong muốn
        self.addApartmentModal.open(AssetDetailsPageLocators.ADD_APARTMENT_BUTTON)
        self.addApartmentModal.form.fillForm(apartmentData)
        self.addApartmentModal.submit()
        
