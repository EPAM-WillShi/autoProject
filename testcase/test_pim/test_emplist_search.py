# coding:utf-8
"""
Created on 2018/5/30
@author: Christine_Lu
"""

import unittest
from config import config
from com import utils
from pageobjects.pim.emplist_search import EmployeeList
from pageobjects.login import Login

class TestSearchById(unittest.TestCase):
    """
    Test search employee by id
    """
    srch_empname = "Christine Lu"
    srch_empid = "0001"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.Emplist = EmployeeList(cls.driver)

    def test_search_employee_by_name(self):
        self.Emplist.switch_main_menu("PIM")
        self.Emplist.search_employee_by_name(self.srch_empname)

    def test_search_employee_by_id(self):
        self.Emplist.switch_main_menu("PIM")
        self.Emplist.search_employee_by_id(self.srch_empid)

    @classmethod
    def tearDownClass(cls):
        cls.Emplist.quit_browser()

if __name__ == "__main__":
    unittest.main()


