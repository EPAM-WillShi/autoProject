# coding:utf-8
"""
Created on 2018/4/17
@author: Molly Xue
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from lib.log import Log
from pageobjects.leave.reports.entitle_user_report import EntitleUserReport

class Test_Employee_Report(unittest.TestCase):
    """
    Test Employee Report for Leave Entitlements and Usage Report functions
    """
    browser = config.BROWSER
    employee = "Employee"
    name = "a"
    timeperiod = "2016-01-01 - 2016-12-31"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.leave = EntitleUserReport(cls.driver)

    def test_select_employee(self):
        """
        select elements to query employee table
        """
        self.leave.select_employee(self.employee)
        self.leave.select_name(self.name)
        self.leave.sleep(1)
        self.leave.select_timeperiod(self.timeperiod)
        self.leave.review_report()
        self.leave.table_list()
        Log.info("Employee Leave Report test passed!")

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()

if __name__ == "__main__":
    unittest.main()

