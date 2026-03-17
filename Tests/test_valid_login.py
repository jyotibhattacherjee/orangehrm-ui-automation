from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage


def test_login_valid_credentials(browser_instance):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dashboard_visible()
    assert dashboard_page.is_side_menu_visible()

