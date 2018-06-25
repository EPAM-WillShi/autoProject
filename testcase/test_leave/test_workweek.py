# coding:utf-8
"""
Created on 2018/4/17
@author: Yolanda Zhang
Edited on 2018/6/8 by Rachel
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.configure.work_week import WorkWeek


class TestWorkWeek(unittest.TestCase):
    """
    Test work week page functions
    """
    browser = config.BROWSER
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.workweek = WorkWeek(cls.driver)

    def test_save_workweek(self):
        """
         Test save workweek function
         """
        self.assertTrue("WorkWeek" in self.workweek.get_page_url())
        self.workweek.save_workweek()
        self.assertTrue("Successfully Saved" in self.workweek.get_element_text(self.workweek.message))
        self.workweek.wait(1)
        self.workweek.reset_default_workweek()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()
