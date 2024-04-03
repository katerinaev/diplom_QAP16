import allure

from helpers.base_page import BasePage

from pages.locators import GetStartedLocators


class GetStartedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = GetStartedLocators()

    def scroll_to_form(self):
        self.scroll_to_element(self.main_locators.FIRST_NAME)

    def fill_first_name(self, first_name):
        self.fill(self.main_locators.FIRST_NAME, first_name)

    def fill_last_name(self, last_name):
        self.fill(self.main_locators.LAST_NAME, last_name)

    def fill_email(self, email):
        self.fill(self.main_locators.EMAIL, email)

    def fill_job_function(self, job_function):
        self.fill(self.main_locators.JOB_FUNCTION, job_function)

    def fill_comments(self, comments):
        self.fill(self.main_locators.COMMENTS, comments)

    def click_on_request_a_demo(self):
        self.force_click(self.main_locators.BUTTON_REQUEST)

    @allure.step("Assert text on request demo")
    def assert_text_on_request_demo(self):
        assert "Thanks for your interest" in self.get_text(self.main_locators.REPLY_TO_REQUEST)
