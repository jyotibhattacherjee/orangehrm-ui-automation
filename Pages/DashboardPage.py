from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.side_menu = (By.XPATH, "//div[@class='oxd-sidepanel-body']")

    def is_dashboard_visible(self):
        return self.wait.wait_for_visibility(self.dashboard_header)

    def is_side_menu_visible(self):
        return self.wait.wait_for_visibility(self.side_menu)