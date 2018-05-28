# coding:utf-8
'''
@author: Christine_lu
'''
import unittest
import time
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.termination_reasons import TerminationReasons


class TestTerminationReasons(unittest.TestCase):
    """
    Test Dashboard page functions
    """
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.tr = TerminationReasons(cls.driver)

    def test_add_termination_reason(self):
        self.tr.create_termination_reason("test")

    @classmethod
    def tearDownClass(cls):
        cls.tr.quit_browser()

if __name__ == "__main__":
    unittest.main()