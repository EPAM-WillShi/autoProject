# coding:utf-8
"""
Created on 2018/06/04

@author: yolanda zhang
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.add_employee import AddEmployee
from pageobjects.pim.emp_report_to import Reportto

import random


class TestReportto(unittest.TestCase):
    """
    Test salary page functions
    """
    browser = config.BROWSER

    first_name = "yolanda"
    last_name = "zhang"
    report_fname = "test"
    report_lname = "hrm"

    emp_name = report_fname + ' ' + report_lname
    emp_name2 = first_name + ' ' + last_name
    emp_list = [emp_name, emp_name2]

    method = "Direct"
    edit_method = "Indirect"
    # subordinate_edit_method = "Other"
    subordinate_edit_method = "Other"
    specify_name = "test" + str(random.randint(1, 20))

    document_name = "report.txt"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

        cls.addemp = AddEmployee(cls.driver)
        cls.addemp.add_user_employee(cls.report_fname, cls.report_lname)
        cls.report = Reportto(cls.driver)

    def test_case01_add_assigned_supervisor(self):
        self.report.open_report_page_via_creating_emp(self.first_name, self.last_name)
        self.report.add_assigned_supervisors(self.emp_name, self.method)
        self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))

    def test_case02_cancel_add_assigned_supervisor(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.cancel_add_supervisors(self.emp_name)

    def test_case03_edit_supervisor(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.edit_added_supervisors(self.emp_name, self.edit_method)
        # self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))
        self.report.verify_edit_actual_result(self.emp_name, self.edit_method)

    def test_case04_delete_supervisor(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.delete_supervisor(self.emp_name)
        self.assertTrue("Successfully Deleted" in self.report.get_element_text(self.report.message))

    def test_case05_add_assigned_subordinates(self):
        self.report.add_subordinates(self.emp_name, self.method)
        self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))

    def test_case06_cancel_add_assigned_subordinates(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.cancel_add_subordinates(self.emp_name)

    def test_case07_edit_subordinates(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.edit_added_subordinates(self.emp_name, self.subordinate_edit_method, self.specify_name)
        # self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))
        self.report.verify_edit_actual_result(self.emp_name, self.subordinate_edit_method, self.specify_name)

    def test_case08_delete_subordinates(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.delete_subordinates(self.emp_name)
        self.assertTrue("Successfully Deleted" in self.report.get_element_text(self.report.message))

    def test_case09_add_attchment(self):
        self.report.add_attachment(self.document_name)
        self.report.verify_attachment(self.document_name)

    def test_case10_delete_attachment(self):
        self.report.delete_attachment(self.document_name)
        self.report.verify_attachment(self.document_name)

    @classmethod
    def tearDownClass(cls):
        for emp in cls.emp_list:
            cls.report.delete_employee(emp)
        cls.report.delete_report_method(cls.specify_name)
        cls.report.quit_browser()

if __name__ == "__main__":
    unittest.main()
