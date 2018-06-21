# coding:utf-8
"""
Created on 2018/06/04

@author: yolanda zhang
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.emp_report_to import Reportto
import string
import random


class TestReportto(unittest.TestCase):
    """
    Test report-to page functions
    """
    browser = config.BROWSER
    last_name = "zhang"
    method = random.choice(["Direct", "Indirect"])
    edit_method = "Other"
    subordinate_edit_method = random.choice(["Direct", "Indirect", "Other"])
    specify_name = "test" + str(random.randint(1, 20))
    method_subordinate = "sub" + str(random.randint(1, 20))
    document_name = "report.txt"
    emp_name_list = []
    emp_list = []

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.report = Reportto(cls.driver)

    def generate_emp_name(self):
        for i in range(3):
            self.emp_name_list.append(''.join(random.choice(string.ascii_letters) for _ in range(4)))
        for i in self.emp_name_list:
            self.emp_list.append(i + ' ' + self.last_name)
            self.report.add_employee(i, self.last_name)

    def test_case01_add_assigned_supervisor(self):
        self.generate_emp_name()
        self.report.open_report_page_via_creating_emp()
        self.report.add_assigned_supervisors(self.emp_list[1], self.method)
        self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))

    def test_case02_cancel_add_assigned_supervisor(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.cancel_add_supervisors(self.emp_list[1])

    def test_case03_edit_supervisor(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.edit_added_supervisors(self.emp_list[1], self.edit_method,
                                           self.method_subordinate)
        # self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))
        self.report.verify_edit_actual_result(self.emp_list[1], self.edit_method,
                                              self.method_subordinate)

    def test_case04_delete_supervisor(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.delete_supervisor(self.emp_list[1])
        self.assertTrue("Successfully Deleted" in self.report.get_element_text(self.report.message))

    def test_case05_add_assigned_subordinates(self):
        self.report.add_subordinates(self.emp_list[0], self.method)
        self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))

    def test_case06_cancel_add_assigned_subordinates(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.cancel_add_subordinates(self.emp_list[0])

    def test_case07_edit_subordinates(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.edit_added_subordinates(self.emp_list[0], self.edit_method,
                                            self.specify_name)
        # self.assertTrue("Successfully Saved" in self.report.get_element_text(self.report.message))
        self.report.verify_edit_actual_result(self.emp_list[0], self.edit_method,
                                              self.specify_name)

    def test_case08_delete_subordinates(self):
        # self.report.search_emp_report(self.first_name, self.last_name)
        self.report.delete_subordinates(self.emp_list[0])
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
        for method in [cls.specify_name, cls.method_subordinate]:
            cls.report.delete_report_method(method)
        cls.report.quit_browser()


if __name__ == "__main__":
    unittest.main()
