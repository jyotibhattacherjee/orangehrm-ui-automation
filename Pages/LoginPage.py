from selenium.webdriver.common.by import By


from Utilities.wait_utils import WaitUtils


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)
        #self.wait= WebDriverWait(driver, 10)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        #self.wait.until(expected_conditions.presence_of_element_located(self.username_input))
        self.loginButton = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.wait.wait_for_visibility(self.username_input).send_keys(username)
        self.wait.wait_for_visibility(self.password_input).send_keys(password)
        self.wait.wait_for_visibility(self.loginButton).click()





        #self.driver.find_element(*self.username_input).send_keys(username)
        #self.driver.find_element(*self.password_input).send_keys(password)
        #self.driver.find_element(*self.loginButton).click()



