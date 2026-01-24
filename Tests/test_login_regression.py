import pytest

from Pages.LoginPage import LoginPage


@pytest.mark.regression
@pytest.mark.parametrize("username, password, exp_res",
    [
        ("Admin", "admin123", "success"),
        ("Admin", "wrongpass", "failure"),
        ("WrongUser", "admin123", "failure"),
        ("", "", "failure")
    ]
    )
def test_login_valid_credentials(browser_instance, username, password, exp_res):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(username, password)
    url = driver.current_url

    if exp_res == "success":
        assert "dashboard" in url
    else:
        assert "dashboard" not in url