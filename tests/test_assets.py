# tests/test_owner.py
from pages.amenities_page import AmenityPage
from pages.login_page import LoginPage
#from utils.database import DatabaseManager
#from utils.data import Owner
#from utils.locators import LoginPageLocators
#from utils.locators import OwnerPageLocators
#from utils.environment import Environment
import pytest
#from selenium import webdriver
import math
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from datetime import datetime

#driver = webdriver.Chrome()

class AssetsTest(BaseCase):
# ### Test case cho việc tạo owner từ database

# # def test_login_and_create_owner_from_database(driver):
# #     # Login
# #     env = Environment()
# #     login_page = LoginPage(driver)
# #     login_page.open(env.get_url())
# #     login_page.type_slowly("#username", env.get_username("admin"))
# #     login_page.type_slowly("#password", env.get_password("admin"))
# #     login_page.click("#login-button")

# #     # Tạo bảng và chèn dữ liệu owners
# #     db_manager = DatabaseManager()
# #     db_manager.create_table(
# #         table_name='owners',
# #         columns=['first_name', 'last_name', 'email', 'phone'],
# #     )
# #     db_manager.insert_data_from_csv(
# #         csv_file='data/owners.csv',
# #         table_name='owners',
# #     )

# #     # Lấy dữ liệu owner từ database và tạo đối tượng Owner
# #     owner_record = db_manager.select_data(table_name='owners')
# #     owner = Owner.from_database_record(owner_record)

# #     # Tạo owner trên trang web
# #     owner_page = OwnerPage(driver) # đây là class có gốc từ BaseCase của seleniumbase
# #     owner_page.create_owner(owner)

# #     # Kiểm tra thành công hay không
# #     owner_page.assert_element_visible(OwnerPageLocators.OWNER_CREATED_MESSAGE)
    
    
#     def test_login_with_owner(self):
#         login_page = LoginPage(self.driver)
#         login_page.login("admin")        
#         self.assert_url_contains("dashboard")
#         self.go_to("https://societypro.froid.works/owners")
#         self.assert_url_contains("owners")
#         span_elements = self.find_elements('span[wire\\:key^="paginator-page-page"]')
#         count = len(span_elements)
#         self.assert_element('[wire\:key="paginator-page-page1"] .cursor-default')
#         spans = self.find_elements('p span.font-medium')
#         val_1 = spans[0].text   # -> "1"
#         val_10 = spans[1].text  # -> "10"
#         C = int(spans[2].text)  # -> "11"
#         PageSize = 10
#         A = 1
#         if C < PageSize:
#             B = C
#         else:
#             B = 10
#         self.assert_equal(int(val_1), A)
#         self.assert_equal(int(val_10), B)
#         if count > 1:
#             self.click('[wire\:key="paginator-page-page2"]')
#             self.assert_element('[wire\:key="paginator-page-page2"] .cursor-default')
#             spans = self.find_elements('p span.font-medium')
#             val_A_page2 = spans[0].text   # -> "11"
#             val_B_page2 = spans[1].text  # -> "11"
#             val_C_page2 = spans[2].text  # -> "11"
#             self.assert_equal(int(val_A_page2), (math.ceil(C/PageSize)-1)*PageSize+1)
#             self.assert_equal(int(val_B_page2), C)
#             self.assert_equal(int(val_C_page2), C)

        
        
    def test_login_with_owner_2(self):
        login_page = LoginPage(self.driver)
        login_page.login("admin")        
        self.assert_url_contains("dashboard")     
        
        self.open("https://societypro.froid.works/assets/1")
        
        self.click("#profile-tabs-content button[wire\\:target][wire\\:click]")
        self.sleep(2)

        datepicker_input_id = "maintenance_date"
        self.click(f"#{datepicker_input_id}")

        target_date = datetime(2022, 6, 15)
        target_month = target_date.strftime("%B")
        target_year = str(target_date.year)
        target_day = str(target_date.day)

        while True:
            current_label = self.find_elements(".pika-single:not(.is-hidden) .pika-label [selected]")
            
            current_month = current_label[0].text
            current_year = current_label[1].text

            if current_month == target_month and current_year == target_year:
                try:
                    self.click(f'.pika-single:not(.is-hidden) button[data-pika-day="{target_day}"]')
                    break
                except Exception:
                    self.fail(f"Không tìm thấy ngày {target_day} trong tháng {target_month} năm {target_year}")
            elif datetime.strptime(current_month + ' ' + current_year, '%B %Y') < target_date:
                self.click(".pika-single:not(.is-hidden) .pika-next")
            else:
                self.click(".pika-single:not(.is-hidden) .pika-prev")

        expected_date_format = target_date.strftime("%B %d, %Y")
        selected_value = self.get_attribute(f"#{datepicker_input_id}", "value")
        self.assert_equal(selected_value, expected_date_format)
            
