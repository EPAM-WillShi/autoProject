# coding:utf-8
"""
Created by Tina Lu
Updated by Linda
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.leave.entitle.employee_entitlements import EmployeeEntitlements
from pageobjects.leave.assign_leave import AssignLeave


class TestAssignLeave(unittest.TestCase):
    """
    Test Assign leave page functions
    """
    browser = config.BROWSER

    first_name = "linda"
    last_name = "test"
    name = "linda test"
    period = "2018-01-01 - 2018-12-31"
    entitlement = "10"
    leave_type_input = "Vacation US"
    date_input = "2018-05-02"
    partial_days = "All Days"
    duration = "Specify Time"
    half_day = "Morning"
    time_from = "10:00"
    time_to = "16:00"
    time_duration = "6"
    from_date_input = "2018-05-07"
    to_date_input = "2018-05-10"
    partial_day = "Start and End Day"
    first_duration = "Specify Time"
    first_half_day = "Morning"
    first_time_from = "09:00"
    first_time_to = "10:30"
    first_time_duration = "1.5"
    second_duration = "Specify Time"
    second_half_day = "Morning"
    second_time_from = "13:00"
    second_time_to = "15:30"
    second_time_duration = "2.5"
    expected_result = "linda test" + "Vacation US" + "10.00" + "" + "0.00" + "0.00" + "0.00" + "10.00"
    comment = "added"
    expected_result_same_date = "linda test" + "Vacation US" + "10.00" + "" + "0.75" + "0.00" + "0.00" + "9.25"
    expected_result_diff_date = "linda test" + "Vacation US" + "10.00" + "" + "0.50" + "0.00" + "0.00" + "8.75"
    balance = "10.00view details"
    balance_same_date = "9.25view details"
    balance_diff_date = "8.75view details"

    @classmethod
    def setUpClass(cls):
        """
         Login, create an employee, add entitlements and go to Assign leave entitlement page
         """
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.employeelist = EmployeeList(cls.driver)
        cls.employeelist.delete_employee(cls.name)
        cls.employeelist.add_employee(cls.first_name, cls.last_name)
        cls.employeelist.find_employee(cls.name)
        cls.addleave = EmployeeEntitlements(cls.driver)
        cls.addleave.add_entitlement(cls.name, cls.leave_type_input,
                                     cls.period, cls.entitlement)
        cls.assignleave = AssignLeave(cls.driver)

    def test_case1_check_balance_leave(self):  # Test assign leave for an employee,  then verify balance
        self.assignleave.select_name_and_type(self.leave_type_input, self.name)
        actual_result = self.assignleave.check_leave_balance()
        self.assertEqual(actual_result, self.balance)
        actual_result_of_balance_details = self.assignleave.check_leave_balance_details()
        self.assertEqual(actual_result_of_balance_details, self.expected_result)

    def test_case2_assign_leave_same_date(self):  # Test assign leave for same date, then verify balance
        self.assignleave.select_name_and_type(self.leave_type_input, self.name)
        self.assignleave.input_date(self.date_input, self.date_input)
        self.assignleave.input_duration(self.duration, self.half_day, self.time_from, self.time_to, self.time_duration)
        self.assignleave.input_comment(self.comment)
        self.assignleave.assign()
        actual_result = self.assignleave.check_leave_balance()
        self.assertEqual(actual_result, self.balance_same_date)
        actual_result_of_balance_details = self.assignleave.check_leave_balance_details()
        self.assertEqual(actual_result_of_balance_details, self.expected_result_same_date)

    def test_case3_assign_leave_multiperiod(self):  # Test assign leave for different date, then verify balance
        self.assignleave.select_name_and_type(self.leave_type_input, self.name)
        self.assignleave.input_date(self.from_date_input, self.to_date_input)
        self.assignleave.input_partial_day(self.partial_day, self.first_duration, self.first_half_day,
                                           self.first_time_from, self.first_time_to, self.first_time_duration,
                                           self.second_duration, self.second_half_day, self.second_time_from,
                                           self.second_time_to, self.second_time_duration)
        self.assignleave.input_comment(self.comment)
        self.assignleave.assign()
        actual_result = self.assignleave.check_leave_balance()
        self.assertEqual(actual_result, self.balance_diff_date)
        actual_result_of_balance_details = self.assignleave.check_leave_balance_details()
        self.assertEqual(actual_result_of_balance_details, self.expected_result_diff_date)

    @classmethod
    def tearDownClass(cls):
        """
        Delete employee and logout
        """
        cls.employeelist = EmployeeList(cls.driver)
        cls.employeelist.delete_employee(cls.name)
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()
