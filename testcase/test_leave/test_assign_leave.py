# coding:utf-8
"""
Created by Tina Lu
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.assign_leave import AssignLeave


class TestAssignLeave(unittest.TestCase):
    """
    Test Assign leave page functions
    """
    browser = config.BROWSER

    first_name = "Tina"
    last_name = "AssignLeave"
    leave_type_input = "Vacation US"
    date_input = "2018-05-02"
    from_date_iput = "2018-05-03"
    to_date_iput = "2018-05-04"
    partial_days = "All Days"
    duraton_input_samedate = "Full Day"
    duration_input_differdate = "Specify Time"
    time_from = "09:00"
    time_to = "17:00"
    comment_input = "Assign leave test"

    @classmethod
    def setUpClass(cls):
        """
         Login, create an employee and go to Assign leave entitlement page
         """
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

        cls.assignleave = AssignLeave(cls.driver)
        cls.assignleave.create_employee(cls.first_name, cls.last_name)

        cls.assignleave.select_menu()

    def test_case1_assign_leave_same_date(self):
        """
        Test assign leave for same date, then verify balance
        """
        self.assignleave.select_name_type(self.first_name + " " + self.last_name,self.leave_type_input)
        self.assignleave.input_samedate_duration_comment(self.date_input,
                                                         self.duraton_input_samedate, self.comment_input)
        self.assignleave.assign()
        self.assignleave.verify_balance_samedate(self.first_name + " " + self.last_name,
                                                 self.leave_type_input,self.date_input)

        self.assignleave.assign()
        self.assignleave.check_overlapping(self.date_input, self.leave_type_input)

    # def test_case2_assign_leave_multiperiod(self):
    #     """
    #     Test assign leave for different date, then verify balance
    #     """
        self.assignleave.click_menu("Assign Leave")
        self.assignleave.select_name_type(self.first_name + " " + self.last_name, self.leave_type_input)
        self.assignleave.input_multiperiod_partial(self.from_date_iput, self.to_date_iput, self.partial_days)
        self.assignleave.input_duration_time_comment(self.duration_input_differdate,
                                                     self.time_from,self.time_to, self.comment_input)
        self.assignleave.assign()
        self.assignleave.verify_balance_multiperiod(self.first_name + " " + self.last_name, self.leave_type_input,
                                                    self.from_date_iput, self.to_date_iput)

    @classmethod
    def tearDownClass(cls):
        """
        Delete employee and logout
        """
        cls.assignleave.delete_employee(cls.first_name, cls.last_name)
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()