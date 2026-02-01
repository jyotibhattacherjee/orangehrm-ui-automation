from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage


class BaseTest:
    def __init__(self):
        self.driver = None
        self.login_page = None
        self.dashboard_page = None

    def setup_method(self, browser_instance):
        self.driver = browser_instance

        self.login_page = LoginPage(self.driver)
        self.login_page.login("Admin", "admin123")
        self.dashboard_page = DashboardPage(self.driver)


