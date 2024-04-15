import allure

from data import DOMEN
from helpers.base_page import BasePage


class FooterElement(BasePage):
    FOOTER_WHAT_WE_DO = '//*[contains(@class, "gap-y-3")]//*[text()="{footer_what_we_do}"]'
    FOOTER_WHO_WE_SERVE = '//*[contains(@class, "gap-y-3")]//*[text()="{footer_who_we_serve}"]'
    FOOTER_ABOUT_US = '//*[contains(@class, "gap-y-3")]//*[text()="{footer_about_us}"]'
    FOOTER_CONTACT = '//*[contains(@class, "gap-y-3")]//*[text()="{footer_contact}"]'
    FACEBOOK_ICON = '//*[@aria-label="Connect on Facebook"]'
    LINKEDIN_ICON = '//*[@aria-label="Connect on LinkedIn"]'
    TWITTER_ICON = '//*[@aria-label="Connect on Twitter"]'
    INSTAGRAM_ICON = '//*[@aria-label="Connect on Instagram"]'
    YOUTUBE_ICON = '//*[@aria-label="Connect on Youtube"]'
    COOKIE_CLOSE = '//*[contains(@class, "onetrust-close-btn-ui")]'
    COOKIE_ACCEPT = '//button[text()="I Understand"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.open(DOMEN)

    def click_on_cookie_close(self):
        self.wait_and_click(self.COOKIE_CLOSE)

    def click_on_accept_cookie(self):
        self.wait_and_click(self.COOKIE_ACCEPT)

    def click_on_social_media_icon(self, locator):
        self.force_click(locator)

    @allure.step("Assert footer what we do is visible")
    def assert_footer_what_we_do_visible(self):
        self.wait_for(self.FOOTER_WHAT_WE_DO.format(footer_what_we_do='Human Capital Management'))
        self.wait_for(self.FOOTER_WHAT_WE_DO.format(footer_what_we_do='Student Management'))
        self.wait_for(self.FOOTER_WHAT_WE_DO.format(footer_what_we_do='Business Operations'))
        self.wait_for(self.FOOTER_WHAT_WE_DO.format(footer_what_we_do='Analytics'))

    @allure.step("Assert footer who we serve is visible")
    def assert_footer_who_we_serve_visible(self):
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Curriculum & Instruction'))
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Human Resources'))
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Nurse Director'))
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Principals'))
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Finance / Business Office'))
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Special Ed Directors'))
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Superintendents'))
        self.wait_for(self.FOOTER_WHO_WE_SERVE.format(footer_who_we_serve='Technology Directors'))

    @allure.step("Assert footer about us is visible")
    def assert_footer_about_us_visible(self):
        self.wait_for(self.FOOTER_ABOUT_US.format(footer_about_us='About Us'))
        self.wait_for(self.FOOTER_ABOUT_US.format(footer_about_us='Team'))
        self.wait_for(self.FOOTER_ABOUT_US.format(footer_about_us='News'))
        self.wait_for(self.FOOTER_ABOUT_US.format(footer_about_us='Commitment to Security'))
        self.wait_for(self.FOOTER_ABOUT_US.format(footer_about_us='Careers'))
        self.wait_for(self.FOOTER_ABOUT_US.format(footer_about_us='Partners'))
        self.wait_for(self.FOOTER_ABOUT_US.format(footer_about_us='Contact'))

    @allure.step("Assert footer contact us is visible")
    def assert_footer_contact_visible(self):
        self.wait_for(self.FOOTER_CONTACT.format(footer_contact='Get Started'))
        self.wait_for(self.FOOTER_CONTACT.format(footer_contact='Schedule a Demo'))

    @allure.step("Assert social media open")
    def assert_social_media_open(self, media_url):
        assert self.driver.current_url == media_url
