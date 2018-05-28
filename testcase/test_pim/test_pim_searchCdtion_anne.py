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
        ep_status = self.pim.get_element_text(self.pim.search_empsts)
        print ep_status
        ep_status_utf = ep_status.encode('utf-8')
        print ep_status_utf.split("\n")
        self.assertListEqual(ep_status_utf.split("\n"), self.lst_status, 'fail')

        # validate dropdownlist value
        job_name = self.pim.get_element_text(self.pim.search_empjobtl)
        print job_name
        job_name_utf = job_name.encode('utf-8')
        print job_name_utf.split("\n")
        self.assertListEqual(job_name_utf.split("\n"), self.lst_jobtitle, 'fail')

        # validate sub unit list
        sub_unit = self.pim.get_element_text(self.pim.search_subunit)
        sub_unit_utf = sub_unit.encode('utf-8')
        self.assertListEqual( sub_unit_utf.split("\n"),self.lst_subunit, 'fail')

        # validate include list
        includ = self.pim.get_element_text(self.pim.search_includ)
        includ_utf = includ.encode('utf-8')
        self.assertListEqual(includ_utf.split("\n"), self.lst_include, 'fail')

    @classmethod
    def tearDownClass(cls):
        cls.pim.quit_browser()


if __name__ == "__main__":
    unittest.main()