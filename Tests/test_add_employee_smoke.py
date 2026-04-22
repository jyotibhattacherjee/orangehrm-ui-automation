import pytest

from Pages.PimPage import PimPage
from Tests.BaseTest import BaseTest


class TestAddEmployeeSmoke(BaseTest):

    @pytest.mark.smoke
    def test_add_employee(self):
        pim_page = PimPage(self.driver)
        pim_page.click_pim_menu()
        assert pim_page.is_pim_header_visible()

        pim_page.click_add_employee_button()

        first_name = "John"
        last_name = "Doe"
        pim_page.enter_employee_details(first_name, last_name)
        emp_id_before = pim_page.get_employee_id()
        print("Before Save Employee ID: ", emp_id_before)

        pim_page.click_save_button()
        assert pim_page.is_personal_details_page_displayed()

        emp_id_after = pim_page.get_employee_id_after_save()
        print("After Save Employee ID: ", emp_id_after)

        assert emp_id_before == emp_id_after




