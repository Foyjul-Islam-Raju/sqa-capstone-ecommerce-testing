"""Login page object."""
from selenium.webdriver.common.by import By

from automation.config import BASE_URL
from automation.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-test="password"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR = (By.CSS_SELECTOR, '[data-test="error"]')

    def open(self):
        self.driver.get(BASE_URL)
        self.visible(self.USERNAME)
        return self

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def error_message(self):
        return self.text(self.ERROR)
