# -*- coding: utf-8 -*-
import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.login import Login
from pageobjects.admin.job.pay_grades import PayGrades

class TestPayGrades(unittest.TestCase):
    """
    Test Pay Grades page functions
    """
    browser = config.BROWSER
    # set testing data
    add_name = 'Molly_pay_grade'
    modify_name = 'Molly_pay_grade_modified'
    currency_name = 'USD - United States Dollar'
    min_salary = '2000'
    max_salary = '200000.23'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.pay = PayGrades(cls.driver)
        Log.info("Arrive to Admin-Job: Pay Grades page")

    def test_case1_cancel_adding_pay_grades(self):
        """
        Test Case1 - cancel adding a new pay grade
        """
        Log.info("Start to run test_case1_cancel_adding_pay_grades")
        self.pay.cancel_adding_pay_grades(self.add_name)
        Log.info("Run Test Case 1: Cancel the adding pay grades operation - completed")

    def test_case2_add_pay_grades(self):
        """
        Test Case2 - add a new pay grade
        """
        Log.info("test_case2_add_pay_grades")
        self.pay.add_pay_grades(self.add_name)
        self.pay.assert_message("Successfully Saved")
        self.pay.click_cancel_button()
        Log.info("Run Test Case 2: Add pay grade operation - completed")

    def test_case3_edit_pay_grades_name(self):
        """
        Test Case3 - edit the name of new pay grade
        """
        Log.info("Start to run test_case3_edit_pay_grades_name")
        self.pay.edit_pay_grades_name(self.add_name, self.modify_name)
        self.pay.assert_message("Successfully Saved")
        self.pay.click_cancel_button()
        Log.info("Run Test Case 3: Edit pay grade name operation - completed")

    def test_case4_edit_pay_grades_add_currency(self):
        """
        Test Case4 - add currency to the new pay grade
        """
        Log.info("Start to run test_case4_edit_pay_grades_add_currency")
        self.pay.edit_pay_grades_add_currency(self.modify_name, self.currency_name, self.min_salary, self.max_salary)
        self.pay.assert_message("Successfully Saved")
        self.pay.check_currency_addto_edit(self.currency_name, self.min_salary, self.max_salary)
        self.pay.click_cancel_button()
        self.pay.check_currency_addto_paygrades(self.modify_name, self.currency_name)
        Log.info("Run Test Case 4: Edit pay grade name, currency:name, salary operation - completed")

    def test_case5_cancel_delete_pay_grades(self):
        """
        Test Case5 - cancel delete the new pay grade
        """
        Log.info("Start to run test_case5_cancel_delete_pay_grades")
        self.pay.cancel_delete_pay_grades(self.modify_name)
        Log.info("Run Test Case 5: Cancel deleting for pay grade operation - completed")

    def test_case6_delete_pay_grades(self):
        """
        Test Case6 - delete the new pay grade
        """
        Log.info("Start to run test_case6_delete_pay_grades")
        self.pay.delete_pay_grades(self.modify_name)
        self.pay.assert_message("Successfully Deleted")
        Log.info("Run Test Case 6: Delete pay grade operation - completed")

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()
        Log.info("End of testing Pay Grades page")

if __name__ == "__main__":
    unittest.main()
