import allure
import pytest

from pages.get_started_page import GetStartedPage
from elements.header_element import HeaderElement


@allure.title('Fill form')
@pytest.mark.skip
def test_fill_form_request_demo(driver):
    header_page = HeaderElement(driver)
    header_page.open_page()
    header_page.click_on_get_started()

    get_started_page = GetStartedPage(driver)
    get_started_page.scroll_to_form()
    get_started_page.fill_first_name('Teresa')
    get_started_page.fill_last_name('Millman')
    get_started_page.fill_email('testeres.user@gmail.com')
    get_started_page.fill_job_function('teacher')
    get_started_page.fill_comments('test')
    get_started_page.click_on_request_a_demo()
    get_started_page.assert_text_on_request_demo()
