# Acceptance requirements

Atomic acceptance statements linked to the designed test cases. Requirement IDs map directly to observable expected outcomes; the CSV is the machine-readable traceability source. Status is design coverage only, not execution status.

| Requirement ID | Acceptance criterion | Test case |
| --- | --- | --- |
| AUTH-01 | Inventory page loads and six products are visible. | AUTH-001 |
| AUTH-02 | Inline validation states that username is required. | AUTH-002 |
| AUTH-03 | Inline validation states that password is required. | AUTH-003 |
| AUTH-04 | Access is denied with a clear credential error. | AUTH-004 |
| AUTH-05 | Access is denied; no authenticated page is shown. | AUTH-005 |
| AUTH-06 | Access is denied and lockout is explained. | AUTH-006 |
| AUTH-07 | Error message disappears and form remains usable. | AUTH-007 |
| AUTH-08 | Valid credentials submit and inventory opens. | AUTH-008 |
| AUTH-09 | Entered characters are visually masked. | AUTH-009 |
| AUTH-10 | Authenticated inventory route and expected page heading appear. | AUTH-010 |
| INV-01 | Exactly six product cards are displayed. | INV-001 |
| INV-02 | Each card presents a non-empty name, description, image, and valid price. | INV-002 |
| INV-03 | Names appear in case-insensitive ascending order. | INV-003 |
| INV-04 | Names appear in case-insensitive descending order. | INV-004 |
| INV-05 | Prices appear in numeric ascending order. | INV-005 |
| INV-06 | Prices appear in numeric descending order. | INV-006 |
| INV-07 | Detail page shows matching name, description, image, and price. | INV-007 |
| INV-08 | Inventory list is restored. | INV-008 |
| INV-09 | Button changes to Remove and cart badge increments to one. | INV-009 |
| INV-10 | Images render with no broken-image indicator. | INV-010 |
| CART-01 | Cart page is shown with an empty item list and shopping can continue. | CART-001 |
| CART-02 | Cart contains that product with matching name and price. | CART-002 |
| CART-03 | Product disappears and cart badge is cleared. | CART-003 |
| CART-04 | Badge shows two; cart contains both products. | CART-004 |
| CART-05 | Inventory page is displayed. | CART-005 |
| CART-06 | Previously selected product remains in cart. | CART-006 |
| CART-07 | Quantity is one and product details are consistent. | CART-007 |
| CART-08 | Only selected product is removed; remaining item and badge are correct. | CART-008 |
| CHK-01 | Checkout is unavailable or flow prevents an empty order. | CHK-001 |
| CHK-02 | Validation identifies first name as required. | CHK-002 |
| CHK-03 | Validation identifies last name as required. | CHK-003 |
| CHK-04 | Validation identifies postal code as required. | CHK-004 |
| CHK-05 | Overview page shows selected item and order summary. | CHK-005 |
| CHK-06 | Flow returns to inventory without placing an order. | CHK-006 |
| CHK-07 | Flow returns to inventory and order is not submitted. | CHK-007 |
| CHK-08 | Displayed item subtotal equals arithmetic sum of products. | CHK-008 |
| CHK-09 | Total equals subtotal plus displayed tax, subject to displayed rounding. | CHK-009 |
| CHK-10 | Order confirmation page states the order is complete. | CHK-010 |
| A11Y-01 | Username, password, submit, and error close control are keyboard reachable in logical order. | A11Y-001 |
| A11Y-02 | Focused control has a visible focus indicator. | A11Y-002 |
| A11Y-03 | Inputs expose meaningful accessible names and required state. | A11Y-003 |
| A11Y-04 | Validation feedback is announced and associated with the relevant form. | A11Y-004 |
| SEC-01 | Input is handled as data; no script executes and no authenticated session appears. | SEC-001 |
| SEC-02 | Protected content is not available without a valid session. | SEC-002 |
| SEC-03 | User remains unauthenticated; private content is not restored. | SEC-003 |
| COMP-01 | Primary controls remain visible and usable without unintended overlap. | COMP-001 |
| COMP-02 | Content reflows; controls remain operable without horizontal clipping. | COMP-002 |
| COMP-03 | Application displays a consistent authenticated state or handles session state safely. | COMP-003 |
| USAB-01 | Empty state is understandable and Continue Shopping is easy to find. | USAB-001 |
| USAB-02 | Success message is prominent and makes the completed state clear. | USAB-002 |
