from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.employee_list_tab = (By.XPATH, "//a[text()='Employee List']")
        self.employee_list_header = (By.XPATH, "//h5[text()='Employee Information']")
        self.employee_name_search_input = (By.XPATH, "//label[text()='Employee Name']/following::input[1]")
        self.search_employee_id_input = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
        self.search_button = (By.XPATH, "//button[text()=' Search ']")
        self.add_employee_id_input = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
        self.personal_employee_id_input = (By.XPATH, "//h6[text()='Personal Details']/following::label[text()='Employee Id']/following::input[1]")



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

    def get_employee_id(self):
        emp_id_element = self.wait.wait_for_visibility(self.add_employee_id_input)
        return emp_id_element.get_attribute("value")

    def click_save_button(self):

        #WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader")))

        save_btn = self.wait.wait_for_clickable(self.save_button)
        save_btn.click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.personal_details_header))
        #self.wait.wait_for_visibility(self.personal_details_header)

    def is_personal_details_page_displayed(self):

        element = self.wait.wait_for_visibility(self.personal_details_header)
        return element.is_displayed()

    def get_employee_id_after_save(self):
        def value_is_not_empty(driver):
            element = driver.find_element(*self.personal_employee_id_input)
            value = element.get_attribute("value")
            return value if value != "" else False

        return WebDriverWait(self.driver, 10).until(value_is_not_empty)

    #def get_employee_id_after_save(self):
        #emp_id_element = self.wait.wait_for_visibility(self.personal_employee_id_input)
        #return emp_id_element.get_attribute("value")


    def click_employee_list_tab(self):
        self.wait.wait_for_clickable(self.employee_list_tab).click()

    def is_employee_list_page_displayed(self):
        element = self.wait.wait_for_visibility(self.employee_list_header)
        return element.is_displayed()

    def search_employee_by_id(self, emp_id):
        input_box = self.wait.wait_for_visibility(self.search_employee_id_input)
        input_box.clear()
        input_box.send_keys(emp_id)
        self.wait.wait_for_clickable(self.search_button).click()

        def is_employee_loaded(driver):
            elements = driver.find_elements(By.XPATH, f"//div[@class='oxd-table-body']//div[text()='{emp_id}']")
            return len(elements) > 0
        WebDriverWait(self.driver, 10).until(is_employee_loaded)
        #self.wait.wait_for_visibility((By.XPATH, "//div[@class='oxd-table-body']"))

    def is_employee_present(self, name):
        #full_name = f"{first_name} {last_name}"
        employee_xpath = f"//div[@class='oxd-table-body']//div[contains(text(),'{name}')]"
        elements = self.driver.find_elements(By.XPATH, employee_xpath)
        return len(elements) > 0

    def is_employee_present_by_id(self, emp_id):
        employee_xpath = f"//div[@class='oxd-table-body']//div[text()='{emp_id}']"
        elements = self.driver.find_elements(By.XPATH, employee_xpath)

        if len(elements) ==1:
            return True
        elif len(elements) > 1:
            raise AssertionError(f"Multiple entries found with Employee ID: {emp_id}")
        else:
            return False