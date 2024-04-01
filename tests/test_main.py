import allure
import pytest

from pages import MainPage
from pages.locators import MainLocators


@allure.title('Check tab attribute')
def test_tab_attribute(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.scroll_to_buttons_group()

    main_page.assert_tab_is_active()


@allure.title('Text')
@pytest.mark.parametrize("suit,title,text", [
    [MainLocators.BUTTON_1, MainLocators.TEXT_1, 'compliant, and growing'],
    [MainLocators.BUTTON_2, MainLocators.TEXT_2, 'impact on education'],
    [MainLocators.BUTTON_3, MainLocators.TEXT_3, 'budgeting, and more.'],
    [MainLocators.BUTTON_4, MainLocators.TEXT_4, 'from the ground up'],
])
def test_text(driver, suit, title, text):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.scroll_to_buttons_group()
    main_page.wait_and_click(suit)

    main_page.assert_text_on_main_page(title, text)
