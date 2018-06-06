# coding:utf-8
"""
Created on 2018/5/30
@author: Christine_Lu
"""

import unittest
from config import config
from com import utils
from pageobjects.pim.emplist_search import EmployeeListSearch
from pageobjects.login import Login

class TestSearchById(unittest.TestCase):
    """
    Test search employee by id
    """
    srch_empname = "Christine Lu"
    srch_empid = "0001"
    supervios_name = "John Smith"
    job_title = "IT Manager"
    sub_unit = "IT"
    status = 'Full-Time Contract'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.emplist_search = EmployeeListSearch(cls.driver)
        cls.emplist_search.click_menu("Employee List")

    def test_case1_search_employee_by_name(self):
        self.emplist_search.search_employee_by_name(self.srch_empname)
        self.emplist_search.check_all_textbox_empty()

    def test_case2_search_employee_by_id(self):
        self.emplist_search.search_employee_by_id(self.srch_empid)
        self.emplist_search.check_all_textbox_empty()

    def test_case3_emplist_search_by_supervisor_name(self):
        self.emplist_search.search_emp_by_supervisor_name(self.supervios_name)
        self.emplist_search.check_all_textbox_empty()

    def test_case4_emplist_search_by_job_title(self):
        self.emplist_search.search_emp_by_job_title(self.job_title)
        self.emplist_search.check_all_textbox_empty()

    def test_case5_emplist_search_by_sub_unit(self):
        self.emplist_search.search_emp_by_sub_unit(self.sub_unit)
        self.emplist_search.check_all_textbox_empty()

    def test_case6_emplist_search_by_status(self):
        self.emplist_search.search_emp_by_status(self.status)
        self.emplist_search.check_all_textbox_empty()

    def test_reset(self):
        self.emplist_search.search_employee_by_name(self.srch_empname)
        self.emplist_search.check_all_textbox_empty()

    @classmethod
    def tearDownClass(cls):
        cls.emplist_search.quit_browser()

if __name__ == "__main__":
    unittest.main()


