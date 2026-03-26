from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class PimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.pim_header = (By.XPATH, "//h6[text()='PIM']")
        self.add_employee_button = (By.XPATH, "//button[text()=' Add ']")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.personal_details_header = (By.XPATH, "//h6[text()='Personal Details']")


    def click_pim_menu(self):
        self.wait.wait_for_clickable(self.pim_menu).click()

    def is_pim_header_visible(self):
        element = self.wait.wait_for_visibility(self.pim_header)
        return element.is_displayed()

    def click_add_employee_button(self):
        self.wait.wait_for_clickable(self.add_employee_button).click()

    def enter_employee_details(self, first_name, last_name):
        self.wait.wait_for_visibility(self.first_name_input).send_keys(first_name)
        self.wait.wait_for_visibility(self.last_name_input).send_keys(last_name)

    def click_save_button(self):
        self.wait.wait_for_clickable(self.save_button).click()
        self.wait.wait_for_visibility(self.personal_details_header)

    def is_personal_details_page_displayed(self):
        element = self.wait.wait_for_visibility(self.personal_details_header)
        return element.is_displayed()
