# -*- coding:utf-8 -*-
import unittest
from config import config
from com import utils
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.login import Login
# from lib.basepage import BasePage
# from pageobjects.mainpage import MainPage


class TestReset(unittest.TestCase):
    """
    Test Reset Button
    """
    browser = config.BROWSER
    lst_status = ['All', 'Freelance', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Probation',
                  'Part-Time Contract', 'Part-Time Internship']
    lst_jobtitle = ['All',  'Account Clerk', 'CEO', 'Finance Manager','HR Executive', 'HR Manager',
                    'IT Executive', 'IT Manager', 'Sales Executive', 'Sales Manager']
    lst_subunit = ['All', 'Sales', 'Administration', 'IT', 'Finance']
    lst_include = ['Current Employees Only', 'Current and Past Employees', 'Past Employees Only']

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.pim = EmployeeList(cls.driver)
        # cls.bps=BasePage(cls.driver)
        cls.pim.max_browser()

    def test_case10_validate_dropdown(self):
        """
        validate dropdownlist value
        """
        self.pim.wait(3)
        self.pim.validate_list_value(self.pim.search_empsts, self.lst_status)

        # validate dropdownlist value
        self.pim.validate_list_value(self.pim.search_empjobtl, self.lst_jobtitle)

        # validate sub unit list
        self.pim.validate_list_value(self.pim.search_subunit, self.lst_subunit)

        # validate include list
        self.pim.validate_list_value(self.pim.search_includ, self.lst_include)

    @classmethod
    def tearDownClass(cls):
        cls.pim.quit_browser()


if __name__ == "__main__":
    unittest.main()