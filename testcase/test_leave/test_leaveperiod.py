# coding:utf-8
"""
Created on 2018/4/17
@author: Molly Xue, Joanna Li
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.configure.leave_period import LeavePeriod
from lib.log import Log

class TestLeavePeriod(unittest.TestCase):
    """
    Test Leave-Configure-Leave Period page functions
    """
    browser = config.BROWSER
    Start_Month = "February"
    Start_Date = "20"
    End_Date = "February 19 (Following Year)"
    Current_LeavePeriod = "2018-01-01 to 2019-02-19"

    startmonth = 'June'
    startdate = '4'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.leaveperiod = LeavePeriod(cls.driver)

    def test_case1_save_NewLeavePeriod(self):
        self.assertTrue("defineLeavePeriod" in self.leaveperiod.get_page_url())
        self.leaveperiod.edit_LeavePeriod()
        self.leaveperiod.select_StartMonth(self.Start_Month)
        self.leaveperiod.select_StartDate(self.Start_Date)
        self.leaveperiod.check_EndDate(self.End_Date)
        self.leaveperiod.save_LeavePeriod()
        self.leaveperiod.check_Current_LeavePeriod(self.Current_LeavePeriod)
        Log.info("Test save Leave Period passed")

    def test_case2_leaveperiod_reset(self):
        self.leaveperiod.reset_leaveperiod(self.startmonth, self.startdate)

    @classmethod
    def tearDownClass(cls):
        cls.leaveperiod.quit_browser()

if __name__ == "__main__":
    unittest.main()
