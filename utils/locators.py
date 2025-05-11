from selenium.webdriver.common.by import By

class BaseLocators:
    # Locator cho header
    HEADER = ("#header")
    # Locator cho footer
    FOOTER = ("#footer")
    # Locator cho sidebar
    SIDEBAR = ("#sidebar")
    # Locator cho nút "Save" dùng chung
    SAVE_BUTTON = ("#save-button")
    # Locator cho thông báo lỗi dùng chung.
    ERROR_MESSAGE = (".error-message")
    #... Thêm các locator chung khác

class LoginPageLocators:
    EMAIL_INPUT = ("#email")
    PASSWORD_INPUT = ("#password")
    LOGIN_BUTTON = ("[type=\"submit\"]")
    LOGIN_FAILED = (".w-full > .mb-4")

class OwnerPageLocators:
    CREATE_OWNER_BUTTON = ("#create-owner-button")
    FIRST_NAME_INPUT = ("#first-name-input")
    LAST_NAME_INPUT = ("#last-name-input")
    EMAIL_INPUT = ("#email-input")
    PHONE_INPUT = ("#phone-input")
    SAVE_BUTTON = ("#save-button")
    OWNER_CREATED_MESSAGE = ("#owner-created-message")
    OWNER_TABLE = ("#owner-table")
    FILTER_SECTION= ('#main-content .w-full .items-center')
    
class ListPageLocators:
    DATATABLE = ("table.min-w-full")
    
class FilterLocators:
    FILTER_SECTION = ("main .h-screen .items-center + div .flex.w-full")
    CLEAR_BUTTON = ("button.bg-red-600")
    HIDE_BUTTON = ("button.bg-white")
    
class LogoutPageLocators:
    MENU_BAR = ("#user-menu-button-2")
    LOGOUT_BUTTON = ("li form")
    
class ProfilePageLocators:
    MENU_BAR = ("#user-menu-button-2")
    PROFILE_BUTTON = "[href='https://societypro.froid.works/user/profile']"
    NAME_INPUT = ("#name")
    EMAIL_INPUT = ("#email")
    SAVE_BUTTON = ('[wire\:submit="updateProfileInformation"] button')
    PROFILE_UPDATED_MESSAGE = "[wire\\:submit=\"updateProfileInformation\"] .flex div [wire\\:submit=\"updateProfileInformation\"] .flex div[wire\\:submit=\"updateProfileInformation\"] .flex div[wire\\:submit=\"updateProfileInformation\"] .flex div[wire\\:submit=\"updateProfileInformation\"] .flex div[wire\\:submit=\"updateProfileInformation\"] .flex div"
    
class AmenitiesPageLocators:
    FILTER_SECTION= ('#main-content .w-full .items-center')
    
class ApartmentPageLocators:
    FILTER_SECTION= ('#main-content .w-full .items-center')
    
class FiltersSection:
    FILTERS_SECTION = (".h-screen[wire\:key] > .items-center + div div.w-full.flex")
    FILTER_ZONE = (".h-screen[wire\:key] > .items-center + div > .flex:not(.items-center)")
    FILTER_OPTION_BUTTON = ("a")
    
class Table:
    TABLE = ("table")
    ROW = ("table tbody tr")
    CELL = ("td")
    
class DashboardLocators:
    BOOKING_BTN = ("[wire\:click=\"showBookAmenityDetail(1)\"]")
    BOOKING_MODAL = (".jetstream-modal[x-data*=Book]")
    MODAL_TITLE = (".text-lg")