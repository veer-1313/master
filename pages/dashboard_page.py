from playwright.sync_api import Page, expect


class DashboardPage:
    """Page object for the OrangeHRM dashboard."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.get_by_role("heading", name="Dashboard")

    def expect_loaded(self) -> None:
        expect(self.page).to_have_url("**/dashboard/index")
        expect(self.heading).to_be_visible()
