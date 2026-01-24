import pytest

from Pages.LoginPage import LoginPage


@pytest.mark.smoke
@pytest.mark.parametrize("username, password",
    [
        ("Admin", "admin123")
    ])
def test_login_valid_credentials(browser_instance, username, password):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(username, password)
    url = driver.current_url
    assert "dashboard" in url