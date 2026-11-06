"""Runtime settings for the SauceDemo UI suite."""
import os

BASE_URL = os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com/")
USERNAME = os.getenv("SAUCEDEMO_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCEDEMO_PASSWORD", "secret_sauce")
HEADLESS = os.getenv("HEADLESS", "true").strip().lower() not in {"0", "false", "no"}
WAIT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "10"))
