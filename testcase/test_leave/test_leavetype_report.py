# coding:utf-8
"""
Created on 2018/4/17
@author: Molly Xue
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.reports.entitle_user_report import EntitleUserReport

class Test_LeaveType_Report(unittest.TestCase):
    """
    Test Leave-Reports-Leave Type page functions
    """
    browser = config.BROWSER

    generatetype = "Leave Type"
    leavetype = "Paternity US"
    datefrom = "2015-01-01 - 2015-12-31"
    role = "IT Manager"
    checkvalue = "All"
    departname = "Administration"

    @classmethod
    def setUpClass(cls):
        """
            Arrive to Leave Entitlements and Usage Report-Leave Type
        """
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.leave = EntitleUserReport(cls.driver)

    # def test_select_LeaveType(self):
    #     self.leave.select_LeaveType(self.generatetype,self.leavetype,self.datefrom,self.role,self.checkvalue,self.departname)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()

if __name__ == "__main__":
    unittest.main()

