import pytest

from Pages.PimPage import PimPage
from Tests.BaseTest import BaseTest


class TestEmployeeListSmoke(BaseTest):

    @pytest.mark.smoke
    def test_employee_list_navigation(self):
        pim_page = PimPage(self.driver)

        pim_page.click_pim_menu()
        assert pim_page.is_pim_header_visible()

        pim_page.click_add_employee_button()

        first_name = "Joe"
        last_name = "Bhat"

        pim_page.enter_employee_details(first_name, last_name)

        emp_id = pim_page.get_employee_id()

        pim_page.click_save_button()
        assert pim_page.is_personal_details_page_displayed()

        pim_page.click_employee_list_tab()
        assert pim_page.is_employee_list_page_displayed()

        pim_page.search_employee_by_id(emp_id)
        assert pim_page.is_employee_present_by_id(emp_id)
        #assert pim_page.is_employee_present(first_name)



