"""Browser fixture and failure screenshot hook."""
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from automation.config import HEADLESS

def pytest_configure():
    Path("reports").mkdir(parents=True, exist_ok=True)


@pytest.fixture
def driver(request):
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1440, 1000)
    yield browser

    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        output = Path("artifacts/screenshots")
        output.mkdir(parents=True, exist_ok=True)
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in request.node.nodeid)
        browser.save_screenshot(str(output / f"{safe}.png"))
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, f"rep_{call.when}", outcome.get_result())
