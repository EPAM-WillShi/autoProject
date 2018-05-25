# coding:utf-8
"""
Created on 2018/4/17
@author: Yolanda Zhang
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.configure.leave_type import LeaveType


class TestLeaveType(unittest.TestCase):
    """
    Test leave type page functions
    """
    browser = config.BROWSER

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.leavetype = LeaveType(cls.driver)

    def test_add_leave_type(self):
        """
         Test add leave type function
         """
        self.assertTrue("leaveType" in self.leavetype.get_page_url())
        self.leavetype.add_leave_type("test leave")
        self.assertTrue("Successfully Saved" in self.leavetype.get_element_text(self.leavetype.message))

    def test_edit_leave_type(self):
        """
         Test edit leave type function
         """
        self.leavetype.add_leave_type("test leave")
        self.leavetype.edit_leave_type()
        self.assertTrue("Successfully Saved" in self.leavetype.get_element_text(self.leavetype.message))

    def test_delete_leave_type(self):
        """
         Test delete leave type function
         """
        self.leavetype.delete_leave_type()
        self.assertTrue("Successfully Deleted" in self.leavetype.get_element_text(self.leavetype.message))

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()

