import allure

from helpers.base_page import BasePage

from pages.locators import WhoWeServeLocators


class WhoWeServePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = WhoWeServeLocators()

    @allure.step("Assert who we serve page is open")
    def assert_that_who_we_serve_page_open(self):
        self.wait_for(self.main_locators.WHO_WE_SERVE_TITLE)

