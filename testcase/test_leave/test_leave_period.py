# -*- coding: utf-8 -*-
"""
Created on 2018/6/1
@author: Christine Lu
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.configure.leave_period1 import LeavePeriod


class TestLeavePeriod(unittest.TestCase):
    """
    Test Leave Period page functions
    """
    start_month = "February"
    start_date = "20"
    end_date = "February 19 (Following Year)"
    current_leave_period = "2018-01-01 to 2019-02-19"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.LP = LeavePeriod(cls.driver)

    def test_edit_leave_period(self):
        self.LP.edit_leave_page()
        self.LP.select_start_month(self.start_month)
        self.LP.select_start_date(self.start_date)
        self.LP.check_end_date(self.end_date)
        self.LP.save_leave_period()
        self.LP.check_current_leave_period(self.current_leave_period)

    @classmethod
    def tearDown(cls):
        cls.LP.quit_browser()

if __name__ == "__main__":
    unittest.main()

