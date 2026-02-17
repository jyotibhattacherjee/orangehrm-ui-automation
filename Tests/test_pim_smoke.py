import pytest

from Pages.PimPage import PimPage
from Tests.BaseTest import BaseTest


class TestPimSmoke(BaseTest):

    @pytest.mark.smoke
    def test_pim_page_navigation(self):
        assert self.dashboard_page.is_side_menu_visible()
        pim_page = PimPage(self.driver)
        pim_page.click_pim_menu()

        assert pim_page.is_pim_header_visible()
