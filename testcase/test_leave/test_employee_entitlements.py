# -*- coding: utf-8 -*-

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.entitle.employee_entitlements_winni import EmployeeEntitlements

class TestEmployeeEntitlements(unittest.TestCase):

    employee_name = "Linda Anderson"
    leave_type = "FMLA US"
    leave_period = "2018-01-01 - 2018-12-31"


    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.employee_entitlements = EmployeeEntitlements(cls.driver)

    def test_case1_search_leave_entitlements(self):
        self.employee_entitlements.search_leave_entitlements(self.employee_name, self.leave_type, self.leave_period)
        self.employee_entitlements.check_search_results()
        self.employee_entitlements.delete_all_leave_entitlements()


    @classmethod
    def tearDownClass(cls):
        cls.employee_entitlements.quit_browser()


if __name__ == "__main__":
    unittest.main()