# Test plan — ShopSmart e-commerce SQA capstone

## Purpose and objectives
Assess customer-facing login, product discovery, cart, and checkout behavior on the SauceDemo public training store. Demonstrate risk-based test design, traceability, exploratory testing, maintainable automation, and honest reporting.

Objectives: verify core journeys and visible business rules; exercise validation, sorting, cart state, navigation, and confirmation; map cases to requirement areas; automate stable high-value checks; report only observed outcomes.

## Scope
**In scope:** Authentication, inventory, cart, checkout, basic keyboard/accessibility checks, session behavior, responsive layout, and exploratory testing.

**Out of scope:** Payment processing, real fulfillment, load testing, penetration testing, exhaustive WCAG audit, third-party integrations, or production certification. This is a public demo with seeded behaviors.

## Strategy
1. Review workflows and quality risks.
2. Map coverage through the traceability CSV.
3. Prioritize critical customer flows as P1 and supporting checks as P2.
4. Use public sample data and reset state between independent cases.
5. Automate selected repeatable checks with Selenium and Pytest.
6. Save dated evidence for real executions and report environment failures separately from product defects.

## Environment
- Target: https://www.saucedemo.com/
- Chrome current stable; baseline viewport 1440x1000.
- Manual spot checks: 1366x768 and 390x844.
- Automation: Python 3.10+, Selenium 4, Pytest 8.
- Data: public sample account; see docs/test-data.md.
- Internet required. The demo's uptime and content are outside project control.

## Entry criteria
Target reachable; browser and Python environment available; authorized test data identified; tester/date and target version recorded for an execution run.

## Exit criteria
In-scope cases have actual status or documented reason not run; P1 failures triaged; automation report reviewed; open issues and environment limits summarized. No pass rate without a real run.

## Severity guidance
Critical = broad outage, exposure, or core journey impossible without workaround. High = important journey blocked or materially wrong. Medium = partial impact with workaround. Low = cosmetic or minor usability issue. Priority is execution order; severity describes actual impact.

## Deliverables
Cases, traceability matrix, risk register, charters, defect template, execution template, Selenium suite, JUnit XML, and screenshots on failure.

## Assumptions and constraints
The demo is not a merchant or payment system. Seeded data may change. Include run date because results are time-sensitive. Do not conduct load/security testing against the public site without owner authorization.
