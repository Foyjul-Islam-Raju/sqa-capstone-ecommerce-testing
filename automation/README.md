# UI automation guide

The suite uses Pytest fixtures for browser lifetime, page objects for locators/actions, explicit waits for synchronization, and data-test selectors for resilient element targeting.

From the repository root:
~~~shell
python -m pip install -r automation/requirements.txt
python -m pytest -m smoke
python -m pytest
~~~

Set HEADLESS=false to view the browser. Configure BASE_URL, username, password, or WAIT_TIMEOUT with the environment variables documented in the root README. Use only an authorized test account. Default credentials are public SauceDemo training data.

Outputs: reports/junit.xml and artifacts/screenshots/. Both are generated and git-ignored.
