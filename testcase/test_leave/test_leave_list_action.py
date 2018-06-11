# -*- coding: utf-8 -*-
"""
Created on 2018/6/4
@author: Christine
"""

import unittest
import datetime
import time
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.leave_list_action import LeaveList


class TestLeaveList(unittest.TestCase):
    """
    Test leave list page functions
    """
    fromdate = "2018-01-01"
    todate = "2019-12-31"
    cancel = "Cancel"
    message = ('XPATH', "//*[@class='message success fadable']")

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.leavelist = LeaveList(cls.driver)

    def test_cancel_leave_list(self):
        self.leavelist.search_leave_list(self.fromdate, self.todate)
        self.fromdate = datetime.datetime.strptime(self.fromdate, '%Y-%m-%d')
        self.todate = datetime.datetime.strptime(self.todate, '%Y-%m-%d')
        time.sleep(3)
        self.leavelist.leave_list_action(self.cancel)
        # self.assertEqual("Successfully Updated", self.leavelist.get_element_text(self.message))

    @classmethod
    def tearDownClass(cls):
        cls.leavelist.quit_browser()


if __name__ == "__main__":
    unittest.main()