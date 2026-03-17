import pytest

from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, browser_instance):
        self.driver = browser_instance

        self.login_page = LoginPage(self.driver)
        self.login_page.login("Admin", "admin123")

        self.dashboard_page = DashboardPage(self.driver)
        assert self.dashboard_page.is_dashboard_visible()
        assert self.dashboard_page.is_dashboard_visible()


