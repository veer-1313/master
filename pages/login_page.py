from playwright.sync_api import Page, expect


class LoginPage:
    """Page object for the OrangeHRM login page."""

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.invalid_credentials_message = page.get_by_text("Invalid credentials")

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")
        expect(self.login_button).to_be_visible()

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_dashboard(self) -> None:
        expect(self.page).to_have_url("**/dashboard/index")
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()

    def expect_invalid_credentials(self) -> None:
        expect(self.invalid_credentials_message).to_be_visible()
