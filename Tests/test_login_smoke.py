import json

import pytest

from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage
from Utilities.path_utils import TESTDATA_DIR


def get_smoke_login_data():
    with open(TESTDATA_DIR/"smoke_login_data.json", "r") as f:
        data = json.load(f)
        user = data["valid_user"]
        return[(user["username"], user["password"])]

@pytest.mark.smoke
@pytest.mark.parametrize("username, password", get_smoke_login_data())
def test_login_valid_credentials(browser_instance, username, password):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(username, password)
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dashboard_visible()