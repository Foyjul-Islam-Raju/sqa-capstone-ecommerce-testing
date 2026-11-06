"""Shopping cart actions."""
from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage


class CartPage(BasePage):
    ITEM_NAMES = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    CHECKOUT = (By.CSS_SELECTOR, '[data-test="checkout"]')
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, '[data-test="continue-shopping"]')

    def names(self):
        return [item.text for item in self.driver.find_elements(*self.ITEM_NAMES)]

    def checkout(self):
        self.click(self.CHECKOUT)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)
