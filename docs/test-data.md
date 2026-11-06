# Test data and reset guide

## Public demo data
- Account: standard_user
- Password: secret_sauce
- Locked account for access rejection: locked_out_user
- URL: https://www.saucedemo.com/

These are public training credentials, not private account data. Confirm they remain documented by the application before execution.

## Safe use
Use only public seeded data or an account you are authorized to test. Never commit personal credentials, tokens, or real customer data. Use synthetic checkout details such as Foyjul / Raju / 1207. This demo does not process a real payment. Keep runs low-volume; this is functional automation, not load testing.

## Repeatability
Start independent cases from a known browser/session state. Remove cart contents or open a new browser between cases. Record the observed app state and date because the demo can change.
