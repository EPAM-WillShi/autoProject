# -*- coding: utf-8 -*-

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.entitle.employee_entitlements_winni import EmployeeEntitlements
from pageobjects.pim.add_employee import AddEmployee
from pageobjects.leave.entitle.add_leave_entitlement import AddLeaveEntitlement

class TestEmployeeEntitlements(unittest.TestCase):

    employee_name = "Linda Li"
    first_name = "Linda"
    last_name = "Li"
    leave_type = "FMLA US"
    leave_period = "2018-01-01 - 2018-12-31"
    entitlement = "5"


    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.addemployee = AddEmployee(cls.driver)
        cls.addemployee.add_user_employee(cls.first_name, cls.last_name)
        cls.addleaveentitlement = AddLeaveEntitlement(cls.driver)
        cls.addleaveentitlement.add_entitlement_for_individual(cls.first_name, cls.last_name, cls.leave_type, cls.leave_period, cls.entitlement)

    def setUp(self):
        self.employee_entitlements = EmployeeEntitlements(self.driver)

    def test_case1_search_cancel_delete_leave_entitlements(self):
        self.employee_entitlements.search_leave_entitlements(self.employee_name, self.leave_type, self.leave_period)
        self.employee_entitlements.check_search_results()
        self.employee_entitlements.cancel_delete_all_leave_entitlements()

    def test_case2_search_delete_all_leave_entitlements(self):
        self.employee_entitlements.search_leave_entitlements(self.employee_name, self.leave_type, self.leave_period)
        self.employee_entitlements.check_search_results()
        self.employee_entitlements.delete_all_leave_entitlements()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()