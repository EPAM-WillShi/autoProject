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
from pageobjects.pim.add_employee import AddEmployee
from pageobjects.leave.assign_leave import AssignLeave


class TestLeaveList(unittest.TestCase):
    """
    Test leave list page functions
    """
    f_name = "Christine"
    l_name = "Lu1"

    # Assign leave
    emp_name = "Christine Lu1"
    leave_type = "Vacation US"
    from_date = "2018-06-12"
    to_date = "2018-06-17"

    date_from = "2018-01-01"
    date_to = "2019-12-31"
    cancel = "Cancel"
    message = ('XPATH', "//*[@class='message success fadable']")

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

    def test_add_employee(self):
        self.addemployee =  AddEmployee(self.driver)
        self.addemployee.add_user_employee(self.f_name, self.l_name)

    def test_assign_leave(self):
        self.assignleave = AssignLeave(self.driver)
        self.assignleave.select_menu()
        self.assignleave.select_name_and_type(self.leave_type, self.emp_name)
        self.assignleave.input_date(self.from_date, self.to_date)
        time.sleep(2)
        self.assignleave.assign()

    def test_cancel_leave_list(self):
        self.leavelist = LeaveList(self.driver)
        self.leavelist.search_leave_list(self.date_from, self.date_to)
        # self.fromdate = datetime.datetime.strptime(self.fromdate, '%Y-%m-%d')
        # self.todate = datetime.datetime.strptime(self.todate, '%Y-%m-%d')
        time.sleep(3)
        self.leavelist.leave_list_action(self.cancel)
        # self.assertEqual("Successfully Updated", self.leavelist.get_element_text(self.message))

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()

if __name__ == "__main__":
    unittest.main()