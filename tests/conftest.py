import json
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from pages.login_page import LoginPage


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOGIN_DATA_FILE = PROJECT_ROOT / "testdata" / "login_data.json"


@pytest.fixture(scope="session")
def login_data() -> dict[str, dict[str, str]]:
    with LOGIN_DATA_FILE.open(encoding="utf-8") as data_file:
        return json.load(data_file)


@pytest.fixture
def browser_context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext) -> Page:
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)
