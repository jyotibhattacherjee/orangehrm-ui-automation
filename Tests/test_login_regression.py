import json

import pytest

from Pages.LoginPage import LoginPage

def get_regression_login_data():
    with open("testdata/regression_login_data.json", "r") as f:
        data = json.load(f)
        scenarios = data["scenarios"]

        return[(s["username"], s["password"], s["exp_res"]) for s in scenarios]

@pytest.mark.regression
@pytest.mark.parametrize("username, password, exp_res", get_regression_login_data())

def test_login_valid_credentials(browser_instance, username, password, exp_res):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(username, password)
    url = driver.current_url

    if exp_res == "success":
        assert "dashboard" in url
    else:
        assert "dashboard" not in url