import allure

from data import DOMEN
from elements.footer_element import FooterElement


@allure.title('Footer: what we do')
def test_footer_what_we_do(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_footer_what_we_do_visible()


@allure.title('Footer: who we serve')
def test_footer_who_we_serve_visible(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_footer_what_we_do_visible()


@allure.title('Footer: about us')
def test_footer_about_us_visible(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_footer_about_us_visible()


@allure.title('Footer: contact')
def test_footer_contact_visible(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_footer_contact_visible()
