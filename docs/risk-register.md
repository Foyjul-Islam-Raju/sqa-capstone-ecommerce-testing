# Risk register

| ID | Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| R-01 | Demo unavailable or behavior changes | Medium | High | Record timestamp; classify environment outages separately; retry before filing. |
| R-02 | UI changes break selectors | Medium | Medium | Prefer data-test selectors and centralize locators in page objects. |
| R-03 | Shared browser state makes tests order-dependent | Medium | Medium | Fresh browser fixture and explicit setup per test. |
| R-04 | Designed cases are mistaken for executed results | Low | High | Keep Not executed status until a dated run and evidence exist. |
| R-05 | Public sample credentials change | Low | Medium | Confirm documented data; parameterize settings through environment variables. |
| R-06 | Browser/driver mismatch causes false failure | Medium | Medium | Use Selenium Manager or managed CI browser; inspect setup errors before triage. |
| R-07 | Excessive traffic affects public service | Low | High | Run only small functional flows; no load scans or high-volume loops. |
| R-08 | Screenshot contains unintended personal information | Low | Medium | Use synthetic data and review artifacts before sharing. |
