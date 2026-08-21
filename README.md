# OrangeHRM Playwright Automation

End-to-end browser tests for the OrangeHRM demo application using Python, Playwright, pytest, and the Page Object Model.

## Project layout

```text
pages/                  Page objects and selectors
testdata/login_data.json  JSON-driven credentials
tests/                  Test cases and fixtures
requirements.txt        Python dependencies
pytest.ini              Pytest configuration
```

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run tests

Run headless tests:

```powershell
pytest
```

Run the smoke test in a visible browser:

```powershell
pytest -m smoke --headed
```

The demo credentials are kept in `testdata/login_data.json` and are loaded by the shared pytest fixture.
