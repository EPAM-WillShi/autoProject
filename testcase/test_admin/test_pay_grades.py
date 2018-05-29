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
    add_name = 'Dora_testing'
    modify_name = 'Dora_modified'
    currency_name = 'ALL - Albanian Lek'
    min_salary = '1000'
    max_salary = '200000.12'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.pay = PayGrades(cls.driver)
        Log.info("Start testing Pay Grades page")

    def test_case1_cancel_adding_pay_grades(self):
        """
        Test Case1 - cancel adding a new pay grade
        """
        self.pay.cancel_adding_pay_grades(self.add_name)

    def test_case2_add_pay_grades(self):
        """
        Test Case2 - add a new pay grade
        """
        self.pay.add_pay_grades(self.add_name)
        self.pay.assert_message("Successfully Saved")
        self.pay.click_cancel_button()

    def test_case3_edit_pay_grades_name(self):
        """
        Test Case3 - edit the name of new pay grade
        """
        self.pay.edit_pay_grades_name(self.add_name, self.modify_name)
        self.pay.assert_message("Successfully Saved")
        self.pay.click_cancel_button()

    def test_case4_edit_pay_grades_add_currency(self):
        """
        Test Case4 - add currency to the new pay grade
        """
        self.pay.edit_pay_grades_add_currency(self.modify_name, self.currency_name, self.min_salary, self.max_salary)
        self.pay.assert_message("Successfully Saved")
        self.pay.check_currency_addto_edit(self.currency_name, self.min_salary, self.max_salary)
        self.pay.click_cancel_button()
        self.pay.check_currency_addto_paygrades(self.modify_name, self.currency_name)

    def test_case5_cancel_delete_pay_grades(self):
        """
        Test Case5 - cancel delete the new pay grade
        """
        self.pay.cancel_delete_pay_grades(self.modify_name)

    def test_case6_delete_pay_grades_OK(self):
        """
        Test Case6 - delete the new pay grade
        """
        self.pay.delete_pay_grades(self.modify_name)
        self.pay.assert_message("Successfully Deleted")

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()
        Log.info("End of testing Pay Grades page")


if __name__ == "__main__":
    unittest.main()
