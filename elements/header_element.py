from data import DOMEN
from helpers.base_page import BasePage
from pages.main_page import MainPage
from elements.locators import HeaderLocators


class HeaderElement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = HeaderLocators()

    def open_page(self):
        self.open(DOMEN)

    def click_on_search_icon(self):
        self.wait_and_click(self.main_locators.SEARCH_ICON)

    def click_on_search_field(self):
        self.wait_and_click(self.main_locators.SEARCH_INPUT)

    def search_text(self, text):
        self.fill(self.main_locators.SEARCH_INPUT, text)
        self.wait_and_click(self.main_locators.SUBMIT)

    def click_on_who_we_serve(self):
        self.wait_and_click(self.main_locators.HEADER_WHO_WE_SERVE)

    def click_on_get_started(self):
        self.wait_and_click(self.main_locators.BUTTON_GET_STARTED)
