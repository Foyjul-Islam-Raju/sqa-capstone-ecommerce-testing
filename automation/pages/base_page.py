"""Shared Selenium page actions with explicit waits."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from automation.config import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.clickable(locator).click()

    def type_text(self, locator, value):
        field = self.visible(locator)
        field.clear()
        field.send_keys(value)

    def text(self, locator):
        return self.visible(locator).text

    def all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
