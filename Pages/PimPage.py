from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class PimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.pim_header = (By.XPATH, "//h6[text()='PIM']")


    def click_pim_menu(self):
        self.wait.wait_for_clickable(self.pim_menu).click()

    def is_pim_header_visible(self):
        return self.wait.wait_for_visibility(self.pim_header)