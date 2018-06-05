# coding:utf-8
"""
Created on 2018/5/29
@author: Molly Xue
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.admin.job.employment_status import EmploymentStatus
from lib.log import Log

class TestEmploymentStatus(unittest.TestCase):
    """
    Test Employment Status page functions
    """
    browser = config.BROWSER
    # set testing data
    null_status_name = ''
    limit_status_name = 'ABCDEFGHJIKLMNOPQRSTUVXXYZabcdehhjhjhjhjhjhlklklkfghijklmnopqrstuvwxyz'
    mul_status_name = 'employment status add'
    mul_time = 5
    valid_status_name = 'test employment status'
    update_name_null = ''
    update_name_duplicate = 'test employment status'
    update_name_valid = 'test employment status_updated'
    def_epstatus_namelist = ['Freelance', 'Full-Time Contract', 'Full-Time Permanent',
                             'Full-Time Probation', 'Part-Time Contract', 'Part-Time Internship']

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.es = EmploymentStatus(cls.driver)
        Log.info("SetupClass for Employment Status- passed")
        cls.es.select_menu()
        Log.info("Arrive to Admin->Job:Employment Status page")

    def test_case1_check_null_employee_textfiled(self):
        """
        Test Case1: Try to check employee status with NULL
        """
        Log.info("Start to run test_case1_check_null_employee_textfiled")
        self.es.check_if_emp_status_valid(self.null_status_name)
        Log.info("Run Test Case1: Check Null employment status is not allowed - completed!")

    def test_case2_check_limit_employee_textfield(self):
        """
        Test Case2: Try to check employee status with more than 50 characters
        """
        Log.info("Start to run test_case2_check_limit_employee_textfield")
        self.es.check_if_emp_status_valid(self.limit_status_name)
        Log.info("Run Test Case2: Check 50+ characters employment status is not allowed - completed!")

    def test_case3_add_employee_status(self):
        """
        Test Case3: Try to add one new employment status
        """
        Log.info("Start to run test_case3_add_employee_status")
        check_epstatus_name = self.es.check_if_emp_status_exist(self.valid_status_name)
        if check_epstatus_name is None:
            self.es.add_employee_status(self.valid_status_name)
            Log.info("Run Test Case3: Add one new employment status - completed!")
        else:
            Log.info("Don't run Test Case3: Add one new employment status - skipped...")

    def test_case4_add_mul_employee_status(self):
        """
        Test Case4: Try to add multiple employment status
        """
        Log.info("Start to run test_case4_add_mul_employee_status")
        check_epstatus_name = self.es.check_if_emp_status_exist(self.mul_status_name)
        if check_epstatus_name is None:
            for i in range(1, self.mul_time):
                suffix = str(i)
                mul_staus_name = self.mul_status_name + suffix
                self.es.add_employee_status(mul_staus_name)
                i += 1
            Log.info("Run Test Case4: Add multiple employment status - completed!")
        else:
            Log.info("Don't run Test Case 4: Add multiple employment status - skipped...")

    def test_case5_edit_empty_employee_status(self):
        """
        Test Case5: Try to find exist employee status and modify into NULL for employee status
        """
        Log.info("Start to run test_case5_edit_empty_employee_status")
        self.es.edit_employee_status(self.valid_status_name, self.update_name_null)
        Log.info("Run Test Case 5: Edit exist employment status to empty not allowed")

    def test_case6_edit_duplicate_employee_status(self):
        """
        Test Case6: Try to find exist employee status and modify into duplicate one
        """
        Log.info("Start to run test_case6_edit_duplicate_employee_status")
        self.es.edit_employee_status(self.valid_status_name, self.update_name_duplicate)
        Log.info("Run Test Case 6: Edit duplicate employee status not allowed")

    def test_case7_edit_employee_status(self):
        """
        Test Case7: Try to find exist employee status and modify into a new valid employee status
        """
        Log.info("Start to run test_case7_edit_employee_status")
        self.es.edit_employee_status(self.valid_status_name, self.update_name_valid)
        Log.info("Run Test Case 7: Edit exist employment status into new valid one - completed")

    def test_case8_delete_employee_status(self):
        """
        Test Case8: Try to delete one employee status
        """
        Log.info("Start to run test_case8_delete_employee_status")
        self.es.delete_employee_status(self.update_name_valid)
        Log.info("Run Test Case 8: Delete exist employment status - completed!")

    def test_case9_delete_mul_employee_status(self):
        """
        Test Case9: Try to delete user defined multiple employee status
        """
        Log.info("Start to run test_case9_delete_mul_employee_status")
        self.es.delete_muluser_employee_status(self.def_epstatus_namelist)
        Log.info("Run Test Case 9: Delete multiple user defined employment status - completed!")

    @classmethod
    def tearDownClass(cls):
        cls.es.quit_browser()
        Log.info("End of testing employment status page")

if __name__ == "__main__":
    unittest.main()