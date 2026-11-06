# Exploratory testing charters

Use a 30-minute timebox. Record date, browser, notes, and actual observations. Charters do not imply that testing has occurred.

## EC-01 — Authentication resilience
Explore empty, invalid, locked, keyboard, and repeated-submit paths. Look for unclear errors or stuck states. Do not attempt denial of service.

## EC-02 — Product discovery and sorting
Explore product cards, details, images, sorting, back navigation, and refresh. Check consistency between list and detail.

## EC-03 — Cart state transitions
Explore add/remove, multiple products, badge, continue shopping, and navigation. Look for count mismatch or stale state.

## EC-04 — Checkout validation and recovery
Explore required fields, cancel actions, overview math, and completion with synthetic data. Do not submit real payment or personal data.

## EC-05 — Keyboard and narrow viewport
Navigate the critical flow with keyboard only and at a narrow viewport. Record focus visibility, order, clipping, and reachable controls.
