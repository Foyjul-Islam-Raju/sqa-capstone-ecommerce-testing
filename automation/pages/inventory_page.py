"""Inventory listing and product detail actions."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from automation.pages.base_page import BasePage


class InventoryPage(BasePage):
    ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    ITEM_NAMES = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    SORT = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    CART_LINK = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')

    def wait_loaded(self):
        self.visible(self.ITEMS)
        return self

    def item_count(self):
        return len(self.all(self.ITEMS))

    def names(self):
        return [item.text for item in self.all(self.ITEM_NAMES)]

    def sort_by(self, value):
        Select(self.visible(self.SORT)).select_by_value(value)

    def _item(self, name):
        return next(item for item in self.all(self.ITEMS)
                    if item.find_element(*self.ITEM_NAMES).text == name)

    def add_item(self, name):
        self._item(name).find_element(
            By.CSS_SELECTOR, 'button[data-test^="add-to-cart"]'
        ).click()

    def remove_item(self, name):
        self._item(name).find_element(
            By.CSS_SELECTOR, 'button[data-test^="remove"]'
        ).click()

    def open_item(self, name):
        self._item(name).find_element(*self.ITEM_NAMES).click()

    def cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return badges[0].text if badges else None

    def open_cart(self):
        self.click(self.CART_LINK)
