# -*- coding: utf-8 -*-
import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.login import Login
from pageobjects.admin.job.work_shifts import WorkShifts


class TestWorkShifts(unittest.TestCase):
    """
    Test Work Shifts page functions
    """
    browser = config.BROWSER
    # set testing data
    add_name = 'Joanna_Workshift'
    workhourfrom = '09:15'
    workhourto = '17:30'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.shift = WorkShifts(cls.driver)
        Log.info("Start testing Work shift page")

    def test_add_one_work_shift(self):
        """
        Test Case  -  one Work shift add
        """
        self.shift.add_one_work_shift(self.add_name, self.workhourfrom, self.workhourto)
        self.shift.assert_message("Successfully Saved")

    def test_delete_work_shift(self):
        """
        Test Case  - Work shift delete the added record
        """
        self.shift.delete_work_shift(self.add_name)

    def test_add_multiple_work_shift(self):
        """
        Test Case  -  one Work shift add
        """
        self.shift.add_multiple_work_shift(self.add_name, self.workhourfrom, self.workhourto, '8.25')

    # def test_edit_work_shift(self):
    #     self.shift.edit_work_shit(self.add_name)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()
        Log.info("End testing Work shift page")


if __name__ == "__main__":
    unittest.main()
