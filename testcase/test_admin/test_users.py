# coding=utf-8

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.admin.user.users import Users


class TestUsers(unittest.TestCase):
    """
    Test search user functions
    """

    browser = config.BROWSER
    first_name = "Dorothy"
    last_name = "Tang"
    user_role = "Admin"
    employee_name = "Dorothy Tang"
    user_name = "dorothy_0123"
    user_status = "Enabled"
    user_password = "123456"
    update_user_name = "dorothy_0123_updated" + utils.random_suffix()

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.user = Users(cls.driver)
        cls.user.create_employee(cls.first_name, cls.last_name)
        cls.user.switch_menu()

    def test_case1_add_user(self):
        self.user.add_user(self.user_role, self.employee_name, self.user_name, self.user_status, self.user_password)
        self.user.search_user(self.user_name)
        self.assertEqual(self.user_name, self.user.search_name)

    def test_case3_delete_user(self):
        self.user.delete_user(self.update_user_name)
        self.user.search_user(self.update_user_name)
        self.assertEqual(None, self.user.search_name)

    def test_case2_edit_user(self):
        self.user.edit_user(self.update_user_name)

    @classmethod
    def tearDownClass(cls):
        # cls.user.delete_employee(cls.last_name)
        cls.login.quit_browser()

if __name__ == "__main__":
    unittest.main()







