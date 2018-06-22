# -*- coding: utf-8 -*-
"""
Created on 2018/4/17

@author: Bonnie_Wang
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.employee_list import EmployeeList


class TestEmpDel(unittest.TestCase):
    """
    Test PIM page Employee List Panel
    """
    browser = config.BROWSER
    employee = config.EMPLOYEE

    @classmethod
    def setUpClass(cls):
        # Login
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.emplist = EmployeeList(cls.driver)
        
    def test_case1_employeelist_check(self):
        """
        Test Employee List Check all Function
        """
        self.emplist.emplist_chkall()
         
    def test_case2_employeelist_uncheck(self):
        """
        Test Employee List Check all Function
        """  
        self.emplist.emplist_unchkall()   

    def test_case3_cancel_del_employee(self):
        """
        Test Employee List cancel delete Function
        """
        self.emplist.cancel_del_employee(self.employee)
    
    def test_case4_del_employee(self):
        """
        Test Employee List Delete Function
        """
        self.emplist.delete_employee(self.employee)
        
    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()
