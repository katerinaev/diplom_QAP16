import allure

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

    def click_on_active_tab(self):
        self.wait_and_click(self.main_locators.ACTIVE_TAB)

    # @allure.step("Assert tab is active")
    # def assert_tab_is_active(self):
    #     assert 'active' == self.get_attribute(self.main_locators.ACTIVE_TAB, 'class')

    # def assert_tab_is_active(self):
    #     element_classes = self.get_attribute(self.main_locators.ACTIVE_TAB, 'class')
    #     assert 'active' in element_classes.split(), \
    #         f"Expected 'active' class not found in element classes: {element_classes}"
    def scroll_to_buttons_group(self):
        self.scroll_to_element(self.main_locators.GROUP_BUTTONS)

    @allure.step("Assert tab is active")
    def assert_tab_is_active(self, buttons=None):
        if buttons is None:
            buttons = [self.main_locators.BUTTON_1, self.main_locators.BUTTON_2,
                       self.main_locators.BUTTON_3, self.main_locators.BUTTON_4]
        for button_locator in buttons:
            self.wait_and_click(button_locator)
            element_classes = self.get_attribute(button_locator, 'class')
            assert 'active' in element_classes.split(), f"Expected 'active' class not found in element classes: {element_classes}"

    @allure.step("Assert text on main page")
    def assert_text_on_main_page(self, locator, text):
        assert text in self.get_text(locator)
