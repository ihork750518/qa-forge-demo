# QA Forge | Free Public Demo

A **real, local-only** API + browser testing demo with Python, pytest, Playwright, HTTPX, Allure and GitHub Actions. This is a limited free sample, **not the full commercial beta**.

## Quick start (Windows PowerShell)

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m playwright install chromium
python -m pytest -v --browser chromium --alluredir=allure-results
```

To view results, install Allure CLI separately, then `allure serve allure-results`.

## What you can try

- Local HTTP API: health check, task CRUD, simple demo token endpoint
- UI: add tasks through a real browser using Playwright
- 5 example tests (3 API + 2 UI)
- CI: GitHub Actions and raw Allure artifacts

## Free demo vs planned paid kit

| Free demo | Planned paid kit ($29, not on sale yet) |
| --- | --- |
| 5 real HTTP/UI tests | Extended API/auth/negative coverage |
| Local demo server | Reusable API client and environment setup examples |
| Basic GitHub Actions | Onboarding and troubleshooting documentation |

**Important:** The local server is not secure for public hosting. It binds to `127.0.0.1` only, has no persistent database, and uses an illustrative token. Do not deploy it to the internet.

## Licensing

This public demo is MIT-licensed. Third-party dependencies retain their own licenses. The separate paid product will have its own distribution terms, which are not yet finalized.
