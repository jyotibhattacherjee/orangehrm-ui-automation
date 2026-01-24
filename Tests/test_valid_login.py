
from Pages.LoginPage import LoginPage


def test_login_valid_credentials(browser_instance):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    url = driver.current_url
    assert "dashboard" in url
