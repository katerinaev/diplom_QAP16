import allure
import pytest

from data import DOMEN
from pages import MainPage
from elements.header_element import HeaderElement


@allure.title('Search')
@pytest.mark.search
@pytest.mark.parametrize("input,expected", [
    ('school', 'The Complete Guide To K-12 School Device Management'),
    ('       ', 'Modules'),
    ('', 'Modules'),
    ('school administration', 'Deciding on school administration software for human resources just got easier.'),
    ('!@#$%', 'Your search generated no results.'),
])
def test_search(driver, input, expected):
    header_element = HeaderElement(driver)
    header_element.open_page()
    header_element.click_on_search_icon()
    header_element.search_text(input)
    header_element.assert_text(expected)
