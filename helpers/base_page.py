import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(By.XPATH, locator)
        return element.get_attribute(attribute)

    def get_text(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element.text

    def wait_for(self, locator, time_out=15):
        try:
            return WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
        except TimeoutException:
            assert False, f'Element {locator} doesnt found'

    def expect_not_visible(self, locator, time_out=10):
        try:
            return WebDriverWait(self.driver, time_out).until(
                EC.invisibility_of_element((By.XPATH, locator))
            )
        except TimeoutException:
            assert False, f'Element {locator} doesnt found'

    def wait_and_click(self, locator, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element.click()
            return element
        except TimeoutException:
            assert False, f'Element {locator} doesnt found'

    def force_click(self, locator):
        return self.driver.execute_script("arguments[0].click();", self.get_element(locator))

    def open(self, url):
        self.driver.get(url)

    @allure.step("Fill input {locator} {text}")
    def fill(self, locator, text):
        element = self.wait_for(locator)
        element.send_keys(text)

    @allure.step("Clear input {locator}")
    def clear_input(self, locator):
        element = self.wait_for(locator)
        element.clear()

    @allure.step("Select by {value}")
    def select_by_value(self, locator, value):
        select = Select(self.wait_for(locator))
        select.select_by_value(value)

    @allure.step("Select by {text}")
    def select_by_text(self, locator, text):
        select = Select(self.wait_for(locator))
        select.select_by_visible_text(text)

    @allure.step("Press enter")
    def press_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)

    @allure.step("Assert text is visible")
    def assert_text(self, text):
        assert self.wait_for(f'//*[contains(text(), "{text}")]'), "Text is not visible"

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def close_alert(self):
        alert = self.driver.switch_to_alert
        print(alert.text)
        alert.accept()

    def switch_to_frame(self, locator):
        iframe = self.get_element(locator)
        self.driver.switch_to.frame(iframe)

    def exit_from_frame(self):
        self.driver.switch_to.default_content()

    def switch_to_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

    def close_current_tab(self):
        self.driver.close()

    def switch_to_main_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])
