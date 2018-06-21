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
from pageobjects.leave.entitle.employee_entitlements import EmployeeEntitlements
from pageobjects.pim.employee_list import EmployeeList
import random
import string


class TestLeaveList(unittest.TestCase):
    """
    Test leave list page functions
    """
    browser = config.BROWSER
    first_name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    last_name = "test"
    emp_name = first_name + ' ' + last_name
    fdate = "2018-05-01"
    tdate = "2018-11-01"
    date_input = "2018-04-06"
    duraton_input_samedate = "Full Day"
    comment_input = "Assign leave test"
    status_list = [-1, 0, 1, 2, 3]
    sub_unit = random.choice(['All', 'Sales', 'Administration', 'IT', 'Finance'])
    period = "2018-01-01 - 2018-12-31"
    entitlement = "10"
    leave_type_input = "Vacation US"
    date_input = "2018-06-14"
    partial_days = "All Days"
    duration = "Specify Time"
    half_day = "Morning"
    time_from = "10:00"
    time_to = "16:00"
    time_duration = "6"
    comment = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    ter_date = "2018-06-14"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.employeelist = EmployeeList(cls.driver)
        cls.employeelist.add_employee(cls.first_name, cls.last_name)
        cls.employeelist.find_employee(cls.emp_name)
        cls.addleave = EmployeeEntitlements(cls.driver)
        cls.addleave.add_entitlement(cls.emp_name, cls.leave_type_input,
                                     cls.period, cls.entitlement)
        cls.leavelist = LeaveList(cls.driver)

        cls.assignleave = AssignLeave(cls.driver)

    def test_case001_prepare_test_data(self):
        self.assignleave.select_name_and_type(self.leave_type_input, self.emp_name)
        self.assignleave.input_date(self.date_input, self.date_input)
        self.assignleave.input_duration(self.duration, self.half_day, self.time_from, self.time_to, self.time_duration)
        self.assignleave.input_comment(self.comment)
        self.assignleave.assign()

    def test_case01_search_leave(self):
        """
        test search function: fill in criteria to search
        """
        self.leavelist.click_menu("Leave List")
        self.leavelist.search_leave(self.emp_name, self.fdate, self.tdate)
        self.fdate = datetime.datetime.strptime(self.fdate, '%Y-%m-%d')
        self.tdate = datetime.datetime.strptime(self.tdate, '%Y-%m-%d')
        self.leavelist.verify_search_result(self.fdate, self.tdate, self.emp_name)

    def test_case02_reset(self):
        """
        test reset search function: fill in criteria and then click reset
        """
        # self.test_case01_search_leave()
        self.leavelist.reset_search()
        self.leavelist.verify_reset_function()

    def test_case_03_search_by_status(self):
        self.leavelist.reset_search()
        self.leavelist.click(self.leavelist.all)
        self.leavelist.click(self.leavelist.all)
        for i in self.status_list:
            self.leavelist.search_by_status(i)
            self.leavelist.verify_search_result()

    def test_case_04_search_by_date(self):
        self.leavelist.reset_search()
        self.leavelist.search_by_date(self.fdate, self.tdate)
        self.fdate = datetime.datetime.strptime(self.fdate, '%Y-%m-%d')
        self.tdate = datetime.datetime.strptime(self.tdate, '%Y-%m-%d')
        self.leavelist.verify_search_result(self.fdate, self.tdate)

    # def test_case06_search_by_subunit(self):
    #     self.leavelist.search_by_subunit(self.sub_unit)

    def test_case_07_search_by_emp_status(self):
        self.leavelist.terminate_emp(self.first_name, self.last_name, self.ter_date)
        self.leavelist.switch_main_menu("Leave")
        self.leavelist.click_menu("Leave List")
        self.leavelist.search_by_emp_status()
        self.leavelist.verify_search_result(self.emp_name)

    @classmethod
    def tearDownClass(cls):
        cls.leavelist.quit_browser()


if __name__ == "__main__":
    unittest.main()
