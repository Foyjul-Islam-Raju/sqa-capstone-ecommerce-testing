"""Checkout form, overview, and completion actions."""
from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    CONTINUE = (By.CSS_SELECTOR, '[data-test="continue"]')
    CANCEL = (By.CSS_SELECTOR, '[data-test="cancel"]')
    ERROR = (By.CSS_SELECTOR, '[data-test="error"]')
    FINISH = (By.CSS_SELECTOR, '[data-test="finish"]')
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')
    SUBTOTAL = (By.CSS_SELECTOR, '[data-test="subtotal-label"]')
    TOTAL = (By.CSS_SELECTOR, '[data-test="total-label"]')

    def fill_information(self, first, last, postal):
        self.type_text(self.FIRST, first)
        self.type_text(self.LAST, last)
        self.type_text(self.POSTAL, postal)

    def continue_to_overview(self):
        self.click(self.CONTINUE)

    def error_message(self):
        return self.text(self.ERROR)

    def subtotal(self):
        return self.text(self.SUBTOTAL)

    def total(self):
        return self.text(self.TOTAL)

    def finish(self):
        self.click(self.FINISH)

    def confirmation(self):
        return self.text(self.COMPLETE_HEADER)

    def cancel(self):
        self.click(self.CANCEL)
