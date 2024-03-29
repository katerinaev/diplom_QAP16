from data import DOMEN
from helpers.base_page import BasePage
from pages.locators import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = MainLocators()

    def open_page(self):
        self.open(DOMEN)

    def click_on_find_your_frontline(self):
        self.wait_and_click(self.main_locators.FIND_YOUR_FRONTLINE)
