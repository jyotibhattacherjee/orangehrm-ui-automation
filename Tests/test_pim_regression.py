import json

import pytest

from Pages.PimPage import PimPage
from Tests.BaseTest import BaseTest
from Utilities.path_utils import TESTDATA_DIR


def get_pim_regression_data():
    with open(TESTDATA_DIR/"regression_pim_data.json", "r") as f:
        data = json.load(f)
        scenario = data["pim_navigation"]

        return [(scenario["module"],)]

class TestPimRegression(BaseTest):

    @pytest.mark.regression
    @pytest.mark.parametrize("module", get_pim_regression_data())
    def test_pim_regression(self, module):
        assert self.dashboard_page.is_side_menu_visible()
        pim_page = PimPage(self.driver)
        pim_page.click_pim_menu()
        assert pim_page.is_pim_header_visible()







