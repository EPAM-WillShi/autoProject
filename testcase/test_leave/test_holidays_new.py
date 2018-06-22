# -*- coding: utf-8 -*-

import unittest
import random
import string
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.configure.holidays_new import HolidayNew


class TestHolidayNew(unittest.TestCase):
    """
        Test add Holiday
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
        cls.holidays = HolidayNew(cls.driver)

    @staticmethod
    def set_holiday_name():
        """
        Create a random holiday name
        """
        name = ''.join(random.sample(string.ascii_letters + string.digits, 6)) + " Holiday"  # 随机产生一个6位的字符串
        return name

    def test_add_holiday_save(self):
        name = self.set_holiday_name()
        self.holidays.add_holiday_save(name)
        self.holidays.delete_one_holiday(name)

    def test_add_holiday_cancel(self):
        name = self.set_holiday_name()
        self.holidays.add_holiday_cancel(name)

    def test_delete_one_holiday(self):
        name = self.set_holiday_name()
        self.holidays.add_holiday_save(name)
        self.holidays.delete_one_holiday(name)

    def test_delete_all_holidays(self):
        name = self.set_holiday_name()
        self.holidays.add_holiday_save(name)
        self.holidays.delete_all_holiday()

    def test_edit_holiday(self):
        name = self.set_holiday_name()
        self.holidays.add_holiday_save(name)
        self.holidays.edit_holiday(name)
        self.holidays.delete_one_holiday(name)

    def test_search_holiday(self):
        self.holidays.search_holiday()

    def test_check_list_data(self):
        name = self.set_holiday_name()
        self.holidays.add_holiday_save(name)
        self.holidays.check_holiday_list(name)
        self.holidays.delete_one_holiday(name)

    @classmethod
    def tearDownClass(cls):
        cls.holidays.quit_browser()


if __name__ == "__main__":
    unittest.main()
