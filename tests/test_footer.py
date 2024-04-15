import allure
import pytest

import data

from elements.footer_element import FooterElement


@allure.title('Footer: what we do')
@pytest.mark.footer
def test_footer_what_we_do(driver):
    footer_element = FooterElement(driver)
    footer_element.open(data.DOMEN)

    footer_element.assert_footer_what_we_do_visible()


@allure.title('Footer: who we serve')
@pytest.mark.footer
def test_footer_who_we_serve_visible(driver):
    footer_element = FooterElement(driver)
    footer_element.open(data.DOMEN)

    footer_element.assert_footer_who_we_serve_visible()


@allure.title('Footer: about us')
@pytest.mark.footer
def test_footer_about_us_visible(driver):
    footer_element = FooterElement(driver)
    footer_element.open(data.DOMEN)

    footer_element.assert_footer_about_us_visible()


@allure.title('Footer: contact')
@pytest.mark.footer
def test_footer_contact_visible(driver):
    footer_element = FooterElement(driver)
    footer_element.open(data.DOMEN)

    footer_element.assert_footer_contact_visible()


@allure.title('Social media')
@pytest.mark.media
@pytest.mark.parametrize("link,url", [
    (FooterElement.FACEBOOK_ICON, data.FACEBOOK_URL),
    (FooterElement.LINKEDIN_ICON, data.LINKEDIN_URL),
    (FooterElement.TWITTER_ICON, data.TWITTER_URL),
    (FooterElement.INSTAGRAM_ICON, data.INSTAGRAM_URL),
    (FooterElement.YOUTUBE_ICON, data.YOUTUBE_URL),
])
def test_social_media(driver, link, url):
    footer_element = FooterElement(driver)
    footer_element.open_page()
    # footer_element.click_on_accept_cookie()

    footer_element.click_on_social_media_icon(link)
    footer_element.switch_to_new_tab()

    footer_element.assert_social_media_open(url)
    footer_element.close_current_tab()
    footer_element.switch_to_main_tab()

    driver.refresh()
