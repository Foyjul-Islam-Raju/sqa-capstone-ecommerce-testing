# ShopSmart E-Commerce SQA Capstone

Portfolio-ready manual QA and UI automation project for the public SauceDemo training store.

## At a glance
- 50 designed manual cases across 8 quality areas, with a requirements traceability matrix.
- Python + Selenium + Pytest automation using page objects and explicit waits.
- GitHub Actions smoke workflow with JUnit XML and failure screenshots.
- Public training account defaults only; no private credentials are stored.
- Honest reporting: designed cases are not presented as executed results.

Application under test: https://www.saucedemo.com/

## Quick start
Requirements: Python 3.10+, Google Chrome, and internet access.

~~~powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r automation/requirements.txt
python -m pytest -m smoke
~~~

Run all UI checks with: python -m pytest

Environment options:
- SAUCEDEMO_BASE_URL (default https://www.saucedemo.com/)
- SAUCEDEMO_USERNAME and SAUCEDEMO_PASSWORD (public training credentials by default)
- HEADLESS (default true)
- WAIT_TIMEOUT (default 10 seconds)

## Deliverables
| Path | Contents |
| --- | --- |
| docs/test-plan.md | Scope, approach, criteria, environments, risks |
| docs/test-cases.md | 50 manual scenarios with steps and expected results |
| docs/requirements.md | Atomic acceptance criteria |
| docs/traceability-matrix.csv | Requirement-to-case coverage |
| docs/test-data.md | Public test data and safe handling |
| docs/risk-register.md | Ranked risks and mitigations |
| docs/exploratory-charters.md | Focused exploratory sessions |
| docs/defect-report-template.md | Reusable defect template |
| docs/execution-report-template.md | Run report ready to fill with actual evidence |
| automation/ | Maintainable Selenium + Pytest tests and page objects |
| .github/workflows/ui-tests.yml | CI smoke run and evidence artifact |

## Case distribution
Authentication 10 · Inventory 10 · Cart 8 · Checkout 10 · Accessibility 4 · Security 3 · Compatibility 3 · Usability 2 = 50.

Automation is a selected functional subset. Manual accessibility, security, compatibility, and exploratory checks are design assets, not claimed automation results.

## Reporting and limitations
Pytest writes reports/junit.xml. Failure screenshots are stored under artifacts/screenshots/. These are ignored by Git. The public training site may change or be unavailable. Record actual runs in the execution report; never represent designed cases as executed. This project is not a production certification, penetration test, load test, or full accessibility audit. Do not load-test or security-scan the public demo without its owner's authorization.

## License
MIT; see LICENSE.

