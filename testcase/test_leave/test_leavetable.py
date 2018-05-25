# coding:utf-8
"""
Created on 2018/4/17
@author: Molly Xue
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.leavetable import LeaveTable
from lib.log import Log

class Test_LeaveTable(unittest.TestCase):
    """
    Test Leave-Configure-Leave Period page functions
    """
    browser = config.BROWSER
    LeaveType = "FMLA US"
    OptionValue__LeaveType = "2"
    startmonth = "January"
    startdate = "1"
    DateFrom = "2018-01-01 - 2018-12-31"
    OptionValue_DateFrom = "2018-01-01$$2018-12-31"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.leavetable = LeaveTable(cls.driver)
        Log.info("SetupClass - passed")
        cls.leavetable.set_leaveperiod(cls.startmonth, cls.startdate)
        cls.leavetable.select_menu()

    def testcase1_leavetable(self):
        self.leavetable.query_LeaveTypeTable(self.LeaveType, self.DateFrom)
        Log.info("Ran query Leave Type function - passed")

    def testcase2_leavetable_EntitlementLink(self):
        self.leavetable.check_LeaveEntitlementsLink(self.OptionValue__LeaveType, self.OptionValue_DateFrom)
        Log.info("Ran check for Leave Entitlements link - passed")

    def testcase3_leavetable_PendingApprovalLink(self):
        self.leavetable.check_LeaveList_PendingApprovalLink(self.DateFrom)
        Log.info("Ran check for Leave Pending Approval (Days) link - passed")

    def testcase4_leavetable_ScheduledLink(self):
        self.leavetable.check_LeaveList_ScheduledLink(self.DateFrom)
        Log.info("Ran check for Leave Scheduled (Days) link - passed")

    def testcase5_leavetable_TakenLink(self):
        self.leavetable.check_leaveList_TakenLink(self.DateFrom)
        Log.info("Ran check for Leave Taken (Days) link - passed")


    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()

if __name__ == "__main__":
    unittest.main()
