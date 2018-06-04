# coding:utf-8
"""
Created on 2018/05/30

@author: yolanda zhang
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.add_employee import AddEmployee
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.pim.emp_salary import Salary
import random


class TestSalary(unittest.TestCase):
    """
    Test salary page functions
    """
    browser = config.BROWSER

    first_name = "yolanda"
    last_name = "zhang"
    emp_name = first_name + ' ' + last_name
    grade = "Executive"
    # component = "test salary"+ str(random.randint(0,20))
    component = "test salary"
    frequency = "Monthly"
    currency = "United States Dollar"
    amount = "50000"
    amount2 = "75000"
    account_num = "123456"
    a_type = "Savings"
    r_num = "2222222"
    r_amount = "1000.00"

    deposit_list = [account_num, a_type, r_num, r_amount]

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

        cls.addemp = AddEmployee(cls.driver)
        cls.addemp.add_user_employee(cls.first_name, cls.last_name)
        cls.salary = Salary(cls.driver)

    #
    # def test_case1_add_salary_new_emp(self):
    #     self.salary.check_salary_page(self.first_name, self.last_name)
    #     self.salary.assign_salary(self.grade, self.component, self.frequency, self.currency, self.amount)
    #     self.assertTrue("Successfully Saved" in self.salary.get_element_text(self.salary.message))
    #
    def test_case2_add_salary_exist_emp(self):
        self.salary.search_emp_salary(self.first_name, self.last_name)
        self.salary.assign_salary(self.grade, self.component, self.frequency, self.currency, self.amount)
        self.assertTrue("Successfully Saved" in self.salary.get_element_text(self.salary.message))

    def test_case3_cancel(self):
        # self.salary.search_emp_salary(self.first_name,self.last_name)
        self.salary.cancel_assgin_salary()
        self.salary.verify_cancel()

    def test_case4_edit_salary(self):
        self.salary.edit_salary(self.component, self.amount2, self.account_num, self.a_type, self.r_num, self.r_amount)
        self.assertTrue("Successfully Saved" in self.salary.get_element_text(self.salary.message))

    def test_case5_show_deposit(self):
        # self.salary.search_emp_salary(self.first_name, self.last_name)
        self.salary.show_direct_deposit(self.component)
        self.salary.verify_deposit_detail()
        self.assertListEqual(self.salary.list, self.deposit_list)

    def test_case6_add_attachment(self):
        self.salary.add_attachment()
        self.salary.verify_attachment()

    def test_case7_delete_salary(self):
        self.salary.delete_salary(self.component)


    @classmethod
    def tearDownClass(cls):
        cls.salary.delete_employee(cls.emp_name)
        cls.salary.quit_browser()


if __name__ == "__main__":
    unittest.main()
