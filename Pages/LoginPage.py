from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.loginButton = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.wait.wait_for_visibility(self.username_input).send_keys(username)
        self.wait.wait_for_visibility(self.password_input).send_keys(password)
        self.wait.wait_for_visibility(self.loginButton).click()





        #self.driver.find_element(*self.username_input).send_keys(username)
        #self.driver.find_element(*self.password_input).send_keys(password)
        #self.driver.find_element(*self.loginButton).click()



