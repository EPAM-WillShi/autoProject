# -*- coding: utf-8 -*-
"""
Created on 2018/4/25
@author: Yolanda Zhang
"""

import unittest
import datetime
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.leave_list import LeaveList
from pageobjects.leave.assign_leave import AssignLeave


class TestLeaveList(unittest.TestCase):
    """
    Test leave list page functions
    """
    browser = config.BROWSER
    first_name = "yolanda"
    last_name = "zhang"
    emp_name = first_name + ' ' + last_name
    fdate = "2018-04-01"
    tdate = "2018-05-01"
    date_input = "2018-04-06"
    duraton_input_samedate = "Full Day"
    comment_input = "Assign leave test"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

        cls.assignleave = AssignLeave(cls.driver)
        cls.assignleave.create_employee(cls.first_name, cls.last_name)
        cls.assignleave.select_menu()
        cls.assignleave.select_name_type(cls.emp_name, "FMLA US")
        cls.assignleave.input_samedate_duration_comment(cls.date_input, cls.duraton_input_samedate, cls.comment_input)
        cls.assignleave.assign()

        cls.leavelist = LeaveList(cls.driver)

    def test_case1_search_leave(self):
        """
        test search function: fill in criteria to search
        """
        self.leavelist.search_leave(self.emp_name, self.fdate, self.tdate)
        self.fdate = datetime.datetime.strptime(self.fdate, '%Y-%m-%d')
        self.tdate = datetime.datetime.strptime(self.tdate, '%Y-%m-%d')
        self.leavelist.verify_search_result(self.emp_name, self.fdate, self.tdate)

    def test_case2_reset(self):
        """
        test reset search function: fill in criteria and then click reset
        """
        self.test_case1_search_leave()
        self.leavelist.reset_search()
        self.leavelist.verify_reset_function()

    @classmethod
    def tearDownClass(cls):
        cls.leavelist.quit_browser()


if __name__ == "__main__":
    unittest.main()
