import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def driver_firefox(headless):
    options = webdriver.FirefoxOptions()
    if headless == 'yes':
        options.add_argument('--headless')
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)


def driver_chrome(headless):
    chrome_options = webdriver.ChromeOptions()
    if headless == 'yes':
        chrome_options.add_argument('--headless')

    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)


# @pytest.fixture(scope="function", autouse=False)
# def driver():
#     web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     web_driver.implicitly_wait(5)
#     web_driver.maximize_window()
#
#     yield web_driver
#
#     web_driver.quit()


@pytest.fixture(scope="session", autouse=False)
def driver(request):
    print('Start driver\n')

    headless = request.config.getoption('--headless')
    browser = request.config.getoption('--browser')
    driver = None
    if browser == 'chrome':
        driver = driver_chrome(headless)
    if browser == 'firefox':
        driver = driver_firefox(headless)

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()
    print('Finish driver\n')
def pytest_addoption(parser):
    parser.addoption(
        '--headless',
        action='store',
        default='yes',
        help='Run browser in headless mode',
    )
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Type of browser',
    )
