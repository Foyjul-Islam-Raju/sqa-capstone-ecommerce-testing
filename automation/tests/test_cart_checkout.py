"""Cart and checkout end-to-end journeys."""
import pytest
from automation.config import PASSWORD, USERNAME
from automation.pages.cart_page import CartPage
from automation.pages.checkout_page import CheckoutPage
from automation.pages.inventory_page import InventoryPage
from automation.pages.login_page import LoginPage


@pytest.fixture
def signed_in_inventory(driver):
    LoginPage(driver).open().login(USERNAME, PASSWORD)
    return InventoryPage(driver).wait_loaded()


@pytest.mark.smoke
def test_add_and_remove_item_updates_badge(signed_in_inventory):
    signed_in_inventory.add_item("Sauce Labs Backpack")
    assert signed_in_inventory.cart_count() == "1"
    signed_in_inventory.remove_item("Sauce Labs Backpack")
    assert signed_in_inventory.cart_count() is None


def test_cart_contains_selected_product(signed_in_inventory):
    signed_in_inventory.add_item("Sauce Labs Backpack")
    signed_in_inventory.open_cart()
    assert CartPage(signed_in_inventory.driver).names() == ["Sauce Labs Backpack"]


def test_checkout_requires_first_name(signed_in_inventory):
    signed_in_inventory.add_item("Sauce Labs Backpack")
    signed_in_inventory.open_cart()
    CartPage(signed_in_inventory.driver).checkout()
    checkout = CheckoutPage(signed_in_inventory.driver)
    checkout.fill_information("", "Raju", "1207")
    checkout.continue_to_overview()
    assert "First Name is required" in checkout.error_message()


def test_checkout_completes_order(signed_in_inventory):
    signed_in_inventory.add_item("Sauce Labs Backpack")
    signed_in_inventory.open_cart()
    CartPage(signed_in_inventory.driver).checkout()
    checkout = CheckoutPage(signed_in_inventory.driver)
    checkout.fill_information("Foyjul", "Raju", "1207")
    checkout.continue_to_overview()
    assert "Item total:" in checkout.subtotal()
    assert "Total:" in checkout.total()
    checkout.finish()
    assert "Thank you for your order" in checkout.confirmation()


def test_cancel_checkout_returns_to_inventory(signed_in_inventory):
    signed_in_inventory.add_item("Sauce Labs Backpack")
    signed_in_inventory.open_cart()
    CartPage(signed_in_inventory.driver).checkout()
    CheckoutPage(signed_in_inventory.driver).cancel()
    assert "inventory.html" in signed_in_inventory.driver.current_url
