"""Authentication cases."""
from automation.config import PASSWORD, USERNAME
from automation.pages.inventory_page import InventoryPage
from automation.pages.login_page import LoginPage
import pytest


@pytest.mark.smoke
def test_valid_user_can_log_in(driver):
    LoginPage(driver).open().login(USERNAME, PASSWORD)
    assert InventoryPage(driver).wait_loaded().item_count() == 6


def test_empty_username_is_rejected(driver):
    page = LoginPage(driver).open()
    page.login("", PASSWORD)
    assert "Username is required" in page.error_message()


def test_invalid_credentials_are_rejected(driver):
    page = LoginPage(driver).open()
    page.login("invalid_user", "wrong_password")
    assert "do not match" in page.error_message()


def test_locked_user_is_denied(driver):
    page = LoginPage(driver).open()
    page.login("locked_out_user", PASSWORD)
    assert "locked out" in page.error_message()
