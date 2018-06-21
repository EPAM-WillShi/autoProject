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
    first_name = utils.input_random_text()
    last_name = utils.input_random_text()
    employee_name = first_name + " " + last_name
    user_name = "U" + first_name
    first_name_u = first_name + "_u"
    last_name_u = last_name + "_u"
    employee_name_u = first_name_u + " " + last_name_u
    user_name_u = user_name + "_u"
    user_password = utils.input_random_password()
    user_role = choice(["Admin", "ESS"])
    user_status = choice(["Enabled", "Disabled"])
    user_role_u = choice(["Admin", "ESS"])
    user_status_u = choice(["Enabled", "Disabled"])

    @classmethod
    def setUpClass(cls):
        driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(driver)
        # cls.login.max_browser()
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.user = Users(driver)

    def test_case1_add_user(self):  # Test adding a new user on Users page.
        self.user.add_employee(self.first_name, self.last_name)
        self.user.open_user_page()
        while self.user.check_if_user_exists(self.user_name):
            Log.info("User exists, change to another user name")
            self.user_name = self.user_name + "1"
        self.user.add_user(self.user_role, self.employee_name, self.user_name, self.user_status, self.user_password)
        self.assertTrue(self.user.check_if_user_exists(self.user_name), "Failed to add new user")

    # def test_case2_search_new_user(self):
    #     self.test_case1_add_user()
    #     self.user.search_system_user(self.user_name, self.employee_name, self.user_role, self.user_status)
    #     search_result = self.user.get_all_users()
    #     print(search_result)

    def test_case2_search_reset(self):  # Test search reset after searching
        self.user.open_user_page()
        users_original = self.user.get_all_users()
        self.user.search_system_user(self.user_name, self.employee_name, self.user_role, self.user_status)
        self.user.click_reset()
        info = self.user.get_search_info()
        users_reset = self.user.get_all_users()
        self.assertEqual(["", "Type for hints...", "All", "All"], info, "Failed to reset the search input controls.")
        self.assertEqual(users_original, users_reset, "Failed to reset the users table.")

    def test_case3_edit_user(self):  # Test editing user without changing password.
        """
        This case should run follow "test_case1_add_user"
        """
        # self.test_case1_add_user()
        self.user.add_employee(self.first_name_u, self.last_name_u)
        self.user.open_user_page()
        self.user.open_user(self.user_name)
        self.user.edit_user(self.user_name_u, self.employee_name_u, self.user_role_u, self.user_status_u)
        self.user.open_user(self.user_name_u)
        info_get = self.user.get_user_info()
        info_set = [self.user_name_u, self.employee_name_u, self.user_role_u, self.user_status_u]
        self.assertEqual(info_get, info_set, "Failed to edit the user or user not exists.")

    def test_case4_delete_user(self):  # Test deleting a user.
        """
        This case should run after test_case1,2 and 3
        """
        self.user.open_user_page()
        self.user.delete_user(self.user_name_u)
        self.assertFalse(self.user.check_if_user_exists(self.user_name_u),
                         "Failed to delete the user or user not exists.")

    # def test_temp(self):
    #     user_list = []
    #     self.user.open_user_page()
    #     self.user.search_system_user("Admin")
    #     result = self.user.get_all_users()
    #     for value in result.values():
    #         temp_str = ''.join(value)
    #         user_list = user_list.append(temp_str)
    #     print(user_list)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()






