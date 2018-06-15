# coding=utf-8
"""
Created on 2018/6/11
@author: Julie Wu
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.admin.user.users import Users
from random import choice
from lib.log import Log


class TestUsers(unittest.TestCase):
    browser = config.BROWSER
    first_name = "user" + utils.random_suffix()
    last_name = "test" + utils.random_suffix()
    user_role = choice(["Admin", "ESS"])
    employee_name = first_name + " " + last_name
    user_name = first_name
    user_status = choice(["Enabled", "Disabled"])
    user_password = utils.random_suffix()
    update_user_name = user_name + "_updated" + utils.random_suffix()

    @classmethod
    def setUpClass(cls):
        driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(driver)
        # cls.login.max_browser()
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.user = Users(driver)

    def test_case1_add_user(self):
        """
        Test_case1: add a new user on Users page
        1. Add an employee.
        2. On Users page,check if the new username already n the user list, if existing then update to a new username.
        3. Add a new user, fill with username, role, employee name,status and password.
        4. If the new created user is not in the user list, assert error.
        """
        self.user.add_employee(self.first_name, self.last_name)
        self.user.open_user_page()
        while self.user.check_if_user_exists(self.user_name):
            Log.info("User exists, change to another user name")
            self.user_name = self.user_name + "1"
        self.user.add_user(self.user_role, self.employee_name, self.user_name, self.user_status, self.user_password)
        self.assertTrue(self.user.check_if_user_exists(self.user_name), "Failed to add new user")

    def test_case2_delete_user(self):
        """
        Test_case2: delete a user on Users page
        1. On Users page,select the checkbox of the user and delete it by the Delete button.
        2. If the deleted user is still in the user list, then assert error.
        """
        self.user.open_user_page()
        self.user.delete_user(self.user_name)
        self.assertFalse(self.user.check_if_user_exists(self.user_name),
                         "Failed to delete the user or user not exists.")

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()






