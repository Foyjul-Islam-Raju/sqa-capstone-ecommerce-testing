# Manual test cases

**System:** SauceDemo public training store  
**Designed cases:** 50  
**Execution status:** Not executed. No execution results are implied.

Run with the public sample account and record actual status, run date, browser, and evidence in the execution report. Do not treat this design document as an execution record.

## AUTH-001 — Successful login with standard user
- **Area / requirement:** Authentication / AUTH-01
- **Priority:** P1
- **Steps:** Open login; enter standard_user and secret_sauce; submit.
- **Expected:** Inventory page loads and six products are visible.
- **Status:** Not executed

## AUTH-002 — Username is required
- **Area / requirement:** Authentication / AUTH-02
- **Priority:** P1
- **Steps:** Leave username empty; enter valid password; submit.
- **Expected:** Inline validation states that username is required.
- **Status:** Not executed

## AUTH-003 — Password is required
- **Area / requirement:** Authentication / AUTH-03
- **Priority:** P1
- **Steps:** Enter valid username; leave password empty; submit.
- **Expected:** Inline validation states that password is required.
- **Status:** Not executed

## AUTH-004 — Invalid username and password
- **Area / requirement:** Authentication / AUTH-04
- **Priority:** P1
- **Steps:** Enter unrecognized username and password; submit.
- **Expected:** Access is denied with a clear credential error.
- **Status:** Not executed

## AUTH-005 — Invalid password for known user
- **Area / requirement:** Authentication / AUTH-05
- **Priority:** P1
- **Steps:** Enter standard_user with incorrect password; submit.
- **Expected:** Access is denied; no authenticated page is shown.
- **Status:** Not executed

## AUTH-006 — Locked-out account
- **Area / requirement:** Authentication / AUTH-06
- **Priority:** P1
- **Steps:** Enter locked_out_user and the public sample password; submit.
- **Expected:** Access is denied and lockout is explained.
- **Status:** Not executed

## AUTH-007 — Error can be dismissed
- **Area / requirement:** Authentication / AUTH-07
- **Priority:** P2
- **Steps:** Cause a login validation error; activate its close control.
- **Expected:** Error message disappears and form remains usable.
- **Status:** Not executed

## AUTH-008 — Login form supports keyboard submission
- **Area / requirement:** Authentication / AUTH-08
- **Priority:** P2
- **Steps:** Tab through username and password; press Enter from password.
- **Expected:** Valid credentials submit and inventory opens.
- **Status:** Not executed

## AUTH-009 — Password is masked
- **Area / requirement:** Authentication / AUTH-09
- **Priority:** P2
- **Steps:** Type a sample password in the password field.
- **Expected:** Entered characters are visually masked.
- **Status:** Not executed

## AUTH-010 — Successful login URL and page state
- **Area / requirement:** Authentication / AUTH-10
- **Priority:** P1
- **Steps:** Log in with standard_user; inspect URL and page heading.
- **Expected:** Authenticated inventory route and expected page heading appear.
- **Status:** Not executed

## INV-001 — Inventory has six products
- **Area / requirement:** Inventory / INV-01
- **Priority:** P1
- **Steps:** Log in as standard_user; count product cards.
- **Expected:** Exactly six product cards are displayed.
- **Status:** Not executed

## INV-002 — Each product has name, image, description, and price
- **Area / requirement:** Inventory / INV-02
- **Priority:** P1
- **Steps:** Inspect every product card.
- **Expected:** Each card presents a non-empty name, description, image, and valid price.
- **Status:** Not executed

## INV-003 — Sort product name ascending
- **Area / requirement:** Inventory / INV-03
- **Priority:** P2
- **Steps:** Select Name (A to Z).
- **Expected:** Names appear in case-insensitive ascending order.
- **Status:** Not executed

## INV-004 — Sort product name descending
- **Area / requirement:** Inventory / INV-04
- **Priority:** P2
- **Steps:** Select Name (Z to A).
- **Expected:** Names appear in case-insensitive descending order.
- **Status:** Not executed

## INV-005 — Sort price low to high
- **Area / requirement:** Inventory / INV-05
- **Priority:** P2
- **Steps:** Select Price (low to high).
- **Expected:** Prices appear in numeric ascending order.
- **Status:** Not executed

## INV-006 — Sort price high to low
- **Area / requirement:** Inventory / INV-06
- **Priority:** P2
- **Steps:** Select Price (high to low).
- **Expected:** Prices appear in numeric descending order.
- **Status:** Not executed

## INV-007 — Open product detail
- **Area / requirement:** Inventory / INV-07
- **Priority:** P1
- **Steps:** Open Sauce Labs Backpack from its product name.
- **Expected:** Detail page shows matching name, description, image, and price.
- **Status:** Not executed

## INV-008 — Return from product detail
- **Area / requirement:** Inventory / INV-08
- **Priority:** P2
- **Steps:** Open a product; activate Back to products.
- **Expected:** Inventory list is restored.
- **Status:** Not executed

## INV-009 — Add product from inventory
- **Area / requirement:** Inventory / INV-09
- **Priority:** P1
- **Steps:** Add Sauce Labs Backpack.
- **Expected:** Button changes to Remove and cart badge increments to one.
- **Status:** Not executed

## INV-010 — Product imagery loads
- **Area / requirement:** Inventory / INV-10
- **Priority:** P2
- **Steps:** Inspect all inventory product images after page load.
- **Expected:** Images render with no broken-image indicator.
- **Status:** Not executed

## CART-001 — Open empty cart
- **Area / requirement:** Cart / CART-01
- **Priority:** P2
- **Steps:** Log in; open cart without adding products.
- **Expected:** Cart page is shown with an empty item list and shopping can continue.
- **Status:** Not executed

## CART-002 — Added product appears in cart
- **Area / requirement:** Cart / CART-02
- **Priority:** P1
- **Steps:** Add Sauce Labs Backpack; open cart.
- **Expected:** Cart contains that product with matching name and price.
- **Status:** Not executed

## CART-003 — Remove product from cart
- **Area / requirement:** Cart / CART-03
- **Priority:** P1
- **Steps:** Add product; open cart; activate Remove.
- **Expected:** Product disappears and cart badge is cleared.
- **Status:** Not executed

## CART-004 — Cart badge reflects multiple products
- **Area / requirement:** Cart / CART-04
- **Priority:** P1
- **Steps:** Add two distinct products from inventory.
- **Expected:** Badge shows two; cart contains both products.
- **Status:** Not executed

## CART-005 — Continue shopping returns to inventory
- **Area / requirement:** Cart / CART-05
- **Priority:** P2
- **Steps:** Open cart; select Continue Shopping.
- **Expected:** Inventory page is displayed.
- **Status:** Not executed

## CART-006 — Cart persists when navigating to product detail
- **Area / requirement:** Cart / CART-06
- **Priority:** P2
- **Steps:** Add a product; open another product detail; return to cart.
- **Expected:** Previously selected product remains in cart.
- **Status:** Not executed

## CART-007 — Cart item quantity is represented correctly
- **Area / requirement:** Cart / CART-07
- **Priority:** P2
- **Steps:** Add one product and inspect its cart row.
- **Expected:** Quantity is one and product details are consistent.
- **Status:** Not executed

## CART-008 — Remove one of multiple products
- **Area / requirement:** Cart / CART-08
- **Priority:** P1
- **Steps:** Add two products; remove one from cart.
- **Expected:** Only selected product is removed; remaining item and badge are correct.
- **Status:** Not executed

## CHK-001 — Checkout cannot start with an empty cart
- **Area / requirement:** Checkout / CHK-01
- **Priority:** P1
- **Steps:** Open empty cart and inspect checkout action.
- **Expected:** Checkout is unavailable or flow prevents an empty order.
- **Status:** Not executed

## CHK-002 — Checkout information requires first name
- **Area / requirement:** Checkout / CHK-02
- **Priority:** P1
- **Steps:** Add item; proceed; leave first name blank; continue.
- **Expected:** Validation identifies first name as required.
- **Status:** Not executed

## CHK-003 — Checkout information requires last name
- **Area / requirement:** Checkout / CHK-03
- **Priority:** P1
- **Steps:** Add item; proceed; leave last name blank; continue.
- **Expected:** Validation identifies last name as required.
- **Status:** Not executed

## CHK-004 — Checkout information requires postal code
- **Area / requirement:** Checkout / CHK-04
- **Priority:** P1
- **Steps:** Add item; proceed; leave postal code blank; continue.
- **Expected:** Validation identifies postal code as required.
- **Status:** Not executed

## CHK-005 — Valid information opens order overview
- **Area / requirement:** Checkout / CHK-05
- **Priority:** P1
- **Steps:** Enter valid first name, last name, and postal code; continue.
- **Expected:** Overview page shows selected item and order summary.
- **Status:** Not executed

## CHK-006 — Cancel checkout information
- **Area / requirement:** Checkout / CHK-06
- **Priority:** P2
- **Steps:** On information page, select Cancel.
- **Expected:** Flow returns to inventory without placing an order.
- **Status:** Not executed

## CHK-007 — Cancel order overview
- **Area / requirement:** Checkout / CHK-07
- **Priority:** P2
- **Steps:** Reach overview; select Cancel.
- **Expected:** Flow returns to inventory and order is not submitted.
- **Status:** Not executed

## CHK-008 — Subtotal equals sum of item prices
- **Area / requirement:** Checkout / CHK-08
- **Priority:** P1
- **Steps:** Add multiple products; reach overview; compare listed prices and subtotal.
- **Expected:** Displayed item subtotal equals arithmetic sum of products.
- **Status:** Not executed

## CHK-009 — Total includes displayed tax
- **Area / requirement:** Checkout / CHK-09
- **Priority:** P1
- **Steps:** Reach overview and compare item subtotal, tax, and total.
- **Expected:** Total equals subtotal plus displayed tax, subject to displayed rounding.
- **Status:** Not executed

## CHK-010 — Finish order shows confirmation
- **Area / requirement:** Checkout / CHK-10
- **Priority:** P1
- **Steps:** Complete valid checkout from overview.
- **Expected:** Order confirmation page states the order is complete.
- **Status:** Not executed

## A11Y-001 — Keyboard reaches all login controls
- **Area / requirement:** Accessibility / A11Y-01
- **Priority:** P1
- **Steps:** Use Tab and Shift+Tab from browser start on login page.
- **Expected:** Username, password, submit, and error close control are keyboard reachable in logical order.
- **Status:** Not executed

## A11Y-002 — Visible focus is identifiable
- **Area / requirement:** Accessibility / A11Y-02
- **Priority:** P2
- **Steps:** Tab through login and inventory controls.
- **Expected:** Focused control has a visible focus indicator.
- **Status:** Not executed

## A11Y-003 — Form fields have accessible names
- **Area / requirement:** Accessibility / A11Y-03
- **Priority:** P1
- **Steps:** Inspect login and checkout inputs with accessibility tree or screen reader.
- **Expected:** Inputs expose meaningful accessible names and required state.
- **Status:** Not executed

## A11Y-004 — Validation error is announced
- **Area / requirement:** Accessibility / A11Y-04
- **Priority:** P1
- **Steps:** Submit incomplete login or checkout form with screen reader active.
- **Expected:** Validation feedback is announced and associated with the relevant form.
- **Status:** Not executed

## SEC-001 — Login input handles special characters safely
- **Area / requirement:** Security / SEC-01
- **Priority:** P1
- **Steps:** Enter quote and markup-like strings in login fields; submit.
- **Expected:** Input is handled as data; no script executes and no authenticated session appears.
- **Status:** Not executed

## SEC-002 — Protected route after logout
- **Area / requirement:** Security / SEC-02
- **Priority:** P1
- **Steps:** Authenticate; log out; navigate back to inventory URL.
- **Expected:** Protected content is not available without a valid session.
- **Status:** Not executed

## SEC-003 — Session ends after logout
- **Area / requirement:** Security / SEC-03
- **Priority:** P1
- **Steps:** Authenticate; log out; use browser back and refresh.
- **Expected:** User remains unauthenticated; private content is not restored.
- **Status:** Not executed

## COMP-001 — Desktop viewport layout
- **Area / requirement:** Compatibility / COMP-01
- **Priority:** P2
- **Steps:** Open login, inventory, cart, checkout at 1366x768.
- **Expected:** Primary controls remain visible and usable without unintended overlap.
- **Status:** Not executed

## COMP-002 — Narrow mobile viewport layout
- **Area / requirement:** Compatibility / COMP-02
- **Priority:** P2
- **Steps:** Set viewport near 390x844; inspect primary customer journey.
- **Expected:** Content reflows; controls remain operable without horizontal clipping.
- **Status:** Not executed

## COMP-003 — Refresh on authenticated inventory
- **Area / requirement:** Compatibility / COMP-03
- **Priority:** P2
- **Steps:** Log in; refresh inventory page.
- **Expected:** Application displays a consistent authenticated state or handles session state safely.
- **Status:** Not executed

## USAB-001 — Empty cart state gives a clear next action
- **Area / requirement:** Usability / USAB-01
- **Priority:** P2
- **Steps:** Open cart with no items.
- **Expected:** Empty state is understandable and Continue Shopping is easy to find.
- **Status:** Not executed

## USAB-002 — Purchase completion has clear confirmation
- **Area / requirement:** Usability / USAB-02
- **Priority:** P1
- **Steps:** Complete checkout and inspect final page.
- **Expected:** Success message is prominent and makes the completed state clear.
- **Status:** Not executed
