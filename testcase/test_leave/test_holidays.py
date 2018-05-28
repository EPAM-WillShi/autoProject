# -*- coding: utf-8 -*-
"""
@author: Joanna Li
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.configure.holidays import Holidays

class TestHoliday(unittest.TestCase):
    """
    Test Holidays' search, add, delete
    """
    browser = config.BROWSER
    hname = 'joanna_name'
    hdate = '2018-05-13'
    hday = 'Half Day'
    hannual = True
    names = ('joanna_name',)

    hname_update = 'joanna_name_update'
    hdate_update = '2018-06-13'
    hday_update = 'Full Day'
    names_update = ('joanna_name_update',)

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.holiday = Holidays(cls.driver)

    # Test case [Leave:14]
    def test_case1_add_holiday(self):
        self.holiday.add_holiday(self.hname, self.hdate, self.hannual, self.hday)

    # Test case[Leave:13]
    def test_case2_delete(self):
        self.holiday.delete_holiday(self.names)

    # Test case edit holiday
    def test_case3_edit_holiday(self):
        self.holiday.add_holiday(self.hname, self.hdate, self.hannual, self.hday)
        self.holiday.edit_holiday(self.hname, self.hname_update, self.hdate_update, self.hday_update)
        self.holiday.delete_holiday(self.names_update)

    # Test case[Leave:11]
    def test_case4_search_holiday(self):
        self.holiday.add_holiday(self.hname, self.hdate, self.hannual, self.hday)
        self.holiday.search_holiday(True, self.hdate, self.hdate, self.names)
        self.holiday.delete_holiday(self.names)
        self.holiday.search_holiday(False, self.hdate, self.hdate, self.names)

    @classmethod
    def tearDownClass(cls):
        cls.holiday.quit_browser()


if __name__ == "__main__":
    unittest.main()
