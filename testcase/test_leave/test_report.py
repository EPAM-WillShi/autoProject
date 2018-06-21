# -*- coding: utf-8 -*-

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.reports.leave_entitlements_and_usage_report import Report


class TestReport(unittest.TestCase):
    """
        Test Leave Entitlements and Usage Report
    """
    # Login
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
        cls.reports = Report(cls.driver)

    def test_search_by_leave_type(self):
        self.reports.search_by_leave_type()

    def test_search_by_employee(self):
        self.reports.search_by_employee()

    @classmethod
    def tearDownClass(cls):
        cls.reports.quit_browser()


if __name__ == "__main__":
    unittest.main()
