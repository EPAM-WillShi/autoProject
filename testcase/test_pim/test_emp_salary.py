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
from pageobjects.pim.emp_salary import Salary
import random
import string
import re


class TestSalary(unittest.TestCase):
    """
    Test salary page functions
    """
    browser = config.BROWSER
    first_name = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    last_name = "zhang"
    emp_name = first_name + ' ' + last_name
    grade = random.choice(["Chief Executive Officer (C.E.O)", "Executive"])
    component = "test salary" + str(random.randint(0, 20))
    frequency = "Monthly"
    currency = "United States Dollar"
    amount = 0
    a_type = random.choice(["Savings", "Checking", "Other"])
    num = ''.join(random.choice(string.digits) for _ in range(5))
    r_amount = str(round(random.uniform(1000, 7500), 2))
    o_name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    deposit_list = [num, a_type, num, r_amount]

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

        cls.addemp = AddEmployee(cls.driver)
        cls.addemp.add_user_employee(cls.first_name, cls.last_name)
        cls.salary = Salary(cls.driver)

    def amount_generator(self):
        if self.grade == "Executive":
            self.amount = str(round(random.uniform(50000, 75000), 2))
        else:
            self.amount = str(round(random.uniform(75000, 125000), 2))

    #
    # def test_case1_add_salary_new_emp(self):
    #     self.salary.check_salary_page(self.first_name, self.last_name)
    #     self.salary.assign_salary(self.grade, self.component, self.frequency, self.currency, self.amount)
    #     self.assertTrue("Successfully Saved" in self.salary.get_element_text(self.salary.message))
    #
    def test_case2_add_salary_exist_emp(self):
        self.amount_generator()
        self.salary.search_emp_salary(self.first_name, self.last_name)
        self.salary.assign_salary(self.grade, self.component, self.frequency, self.currency, self.amount)
        self.assertTrue("Successfully Saved" in self.salary.get_element_text(self.salary.message))

    def test_case3_cancel(self):
        # self.salary.search_emp_salary(self.first_name,self.last_name)
        self.salary.cancel_assgin_salary()
        self.salary.verify_cancel()

    def test_case4_edit_salary(self):
        self.amount_generator()
        self.salary.edit_salary(self.component, self.amount, self.num, self.a_type, self.num, self.r_amount,
                                self.o_name)
        if self.a_type == "Other":
            self.deposit_list[1] = self.o_name
        if re.match(r'^[0]', self.num):
            self.deposit_list[2] = self.num.lstrip('0')
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
