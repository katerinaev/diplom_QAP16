import allure

from pages import MainPage
from pages.who_we_serve_page import WhoWeServePage
from elements.header_element import HeaderElement


@allure.title('Open who we serve page')
def test_open_who_we_serve_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_on_find_your_frontline()

    who_we_serve_page = WhoWeServePage(driver)
    who_we_serve_page.assert_that_who_we_serve_page_open()


@allure.title('Text on who we serve page')
def test_text_on_who_we_serve_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    header_page = HeaderElement(driver)
    header_page.click_on_who_we_serve()

    who_we_serve_page = WhoWeServePage(driver)
    who_we_serve_page.assert_text_on_who_we_serve_page()
