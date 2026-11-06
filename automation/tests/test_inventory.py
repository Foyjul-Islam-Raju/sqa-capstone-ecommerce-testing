"""Inventory tests."""
import pytest
from automation.config import PASSWORD, USERNAME
from automation.pages.inventory_page import InventoryPage
from automation.pages.login_page import LoginPage


@pytest.fixture
def inventory(driver):
    LoginPage(driver).open().login(USERNAME, PASSWORD)
    return InventoryPage(driver).wait_loaded()


@pytest.mark.smoke
def test_inventory_shows_six_products(inventory):
    assert inventory.item_count() == 6


def test_inventory_sorts_names_ascending(inventory):
    inventory.sort_by("az")
    assert inventory.names() == sorted(inventory.names(), key=str.casefold)


def test_inventory_sorts_names_descending(inventory):
    inventory.sort_by("za")
    assert inventory.names() == sorted(inventory.names(), key=str.casefold, reverse=True)


def test_selected_product_detail_opens(inventory):
    inventory.open_item("Sauce Labs Backpack")
    assert "inventory-item.html" in inventory.driver.current_url
    assert "Sauce Labs Backpack" in inventory.driver.page_source
