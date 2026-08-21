import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_user_can_login_with_valid_credentials(
    login_page: LoginPage, login_data: dict[str, dict[str, str]]
) -> None:
    credentials = login_data["valid_user"]

    login_page.open()
    login_page.login(credentials["username"], credentials["password"])
    login_page.expect_dashboard()


def test_user_cannot_login_with_invalid_credentials(
    login_page: LoginPage, login_data: dict[str, dict[str, str]]
) -> None:
    credentials = login_data["invalid_user"]

    login_page.open()
    login_page.login(credentials["username"], credentials["password"])
    login_page.expect_invalid_credentials()
