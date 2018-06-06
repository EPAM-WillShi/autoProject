# coding:utf-8
"""
Created on 2018/06/06

@author: yolanda zhang
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.config.reporting_methods import Report_method

import random


class TestReportmethod(unittest.TestCase):
    """
    Test salary page functions
    """
    browser = config.BROWSER

    name = "test" + str(random.randint(1, 20))

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.repmethod = Report_method(cls.driver)

    def test_case01_add_method(self):
        self.repmethod.add_report_method(self.name)
        self.assertTrue("Successfully Saved" in self.repmethod.get_element_text(self.repmethod.message))

    def test_case02_delete_added_method(self):
        self.repmethod.delete_report_method(self.name)
        self.assertTrue("Successfully Deleted" in self.repmethod.get_element_text(self.repmethod.message))

    @classmethod
    def tearDownClass(cls):
        cls.repmethod.quit_browser()


if __name__ == "__main__":
    unittest.main()
