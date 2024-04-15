import time

import allure
import pytest

from pages.resources_page import ResourcesPage


@allure.title('Select content type')
@pytest.mark.select
def test_select_content_type(driver, point, option):
    resources_page = ResourcesPage(driver)
    resources_page.open_page()
    resources_page.scroll_to_dropdown()
    resources_page.click_on_content_type()
    # resources_page.select_case_study_in_content_type_by_text()
    resources_page.click_on_option(point)
    resources_page.assert_option_is_selected(option)

@allure.title('Resources Content type')
@pytest.mark.content
@pytest.mark.parametrize("point,option", [
    ('//*[@class="fs-option-label"][contains(text(),"Case Study")]', '//option[@value="case-study"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Video")]', '//option[@value="video-resource"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Guide")]', '//option[@value="guide"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Blog Post")]', '//option[@value="blog-post"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Interactive")]', '//option[@value="quiz"]'),
    ('//*[@class="fs-option-label"][contains(text(),"eBook")]', '//option[@value="ebook"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Thought Leadership")]', '//option[@value="thought-leadership"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Infographic")]', '//option[@value="infographic"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Report")]', '//option[@value="report"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Podcast")]', '//option[@value="podcast"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Template")]', '//option[@value="template"]'),
    ('//*[@class="fs-option-label"][contains(text(),"Webinar")]', '//option[@value="webinar"]'),
])
def test_select_content_type(driver, point, option):
    resources_page = ResourcesPage(driver)
    resources_page.open_page()
    resources_page.scroll_to_dropdown()
    resources_page.click_on_content_type()
    resources_page.click_on_option(point)
    resources_page.assert_option_is_selected(option)

