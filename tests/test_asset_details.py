from seleniumbase import BaseCase
from pages.asset_details_page import AssetDetailsPage
from pages.login_page import LoginPage

class TestAssetDetails(BaseCase):
    def test_create_apartment(self):
        loginPage = LoginPage(self.driver)
        loginPage.login()
        
        assetDetailsPage = AssetDetailsPage(self.driver, "1")
        assetDetailsPage.open()
        assetDetailsPage.createApartmentModal({
            "name": "test",
            "code": "test",
            "floor": "1",
            "size": "100",
            "bedroom": "2",
            "bathroom": "2",
            "rent_fee": "1000",
            "rent_frequency": "monthly",
            "deposit": "1000",
            "deposit_frequency": "monthly",
            "status": "available",
            "type": "apartment",
        })
