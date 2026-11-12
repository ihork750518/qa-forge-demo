# QA Forge v1.0 | Product specification

Status: **planned, not released, not for sale**  
Target price: **$29 one-time** (subject to payment/legal readiness)

## Product promise
A practical, locally runnable Python QA automation starter kit for engineers who want to adapt working API and browser test patterns instead of building all scaffolding from scratch.

## Intended buyer
Manual QA transitioning to automation; junior/mid automation QA; freelance QA engineers and small teams.

## Public demo vs commercial v1.0
| Public demo (MIT) | Commercial v1.0 (planned) |
| --- | --- |
| Local HTTP API and 5 sample tests | Extended CRUD, auth, negative and boundary API scenarios |
| Basic Playwright UI examples | Page Object Model, reusable fixtures, robust selectors |
| Basic local setup | Dev/QA/Staging configuration examples (safe local defaults) |
| Allure raw results | Failure screenshots and reporting guide |
| Basic GitHub Actions | Configurable CI execution, artifacts, troubleshooting |
| README | Step-by-step onboarding, architecture and adaptation guide |

## Acceptance criteria
- [ ] All shipped examples run on Python 3.13 in a clean virtual environment
- [ ] All tests pass locally and in GitHub Actions
- [ ] No real credentials, secrets or publicly exposed demo services
- [ ] Clear separation of illustrative authentication from production security
- [ ] Documented Windows PowerShell and Linux setup
- [ ] Troubleshooting guide for browsers, dependencies, Allure and CI
- [ ] Release ZIP contains versioned source, docs, changelog, license and checksums
- [ ] Delivery, refund terms, payment provider and legal eligibility confirmed before sale
- [ ] Public demo remains free; paid kit code is kept outside this public repository

## Release gates
1. Implement and test commercial features in a **separate private repository**.
2. Validate buyer value with the existing beta-interest form.
3. Review license, legal eligibility to sell while serving, taxes and payment requirements.
4. Set up checkout, delivery, refunds and support contact.
5. Only then switch landing-page messaging from planned price to purchase.

## Non-goals
- Hosted SaaS
- Production-grade authentication server
- Guarantee that tests work unchanged with every buyer application
- Paid product source committed to the public demo repository
