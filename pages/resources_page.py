import allure

from data.urls import RESOURCES
from helpers.base_page import BasePage

from pages.locators import ResourcesLocators


class ResourcesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = ResourcesLocators()

    def open_page(self):
        self.open(RESOURCES)

    def scroll_to_dropdown(self):
        self.scroll_to_element(self.main_locators.DROPDOWNS)

    def click_on_content_type(self):
        self.wait_and_click(self.main_locators.CONTENT_TYPE)

    def select_case_study_in_content_type(self):
        self.select_by_value(self.main_locators.CONTENT_TYPE_DROPDOWN, 'case-study')

    def select_case_study_in_content_type_by_text(self):
        self.select_by_text(self.main_locators.CONTENT_TYPE_DROPDOWN, 'Case Study')

    def click_on_option(self, locator):
        self.wait_and_click(locator)

    @allure.step("Assert option is selected")
    def assert_option_is_selected(self, locator):
        assert '' in self.get_attribute(locator, 'selected')
