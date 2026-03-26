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

        pim_page.click_save_button()
        assert pim_page.is_personal_details_page_displayed()



