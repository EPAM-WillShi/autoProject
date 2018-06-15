# # coding=utf-8
#
# import unittest
# from config import config
# from com import utils
# from pageobjects.login import Login
# from pageobjects.admin.user.users import Users
# from pageobjects.pim.add_employee import AddEmployee
#
#
# class SearchAndUpdateUser(unittest.TestCase):
#     """
#     Test search user functions
#     """
#
#     browser = config.BROWSER
#     employee_first_name = "epm"
#     employee_last_name = "suzhou"
#     employee_name = "epm suzhou"
#     user_role_value = "ESS"
#     user_name_value = "sandy"
#     user_status_value = "Enabled"
#     user_pwd_value = "123456"
#     updated_user_name = "test0"
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = utils.get_browser_driver(cls.browser)
#         cls.login = Login(cls.driver)
#         cls.login.open_browser(config.LOGIN_URL)
#         cls.login.login(config.USER_NAME, config.PASSWORD)
#         cls.user = Users(cls.driver)
#
#     def test_search_and_update(self):
#         self.user.create_employee(self.employee_first_name, self.employee_last_name)
#         self.user.switch_main_menu("admin")
#         self.user.add_user(self.user_role_value, self.employee_name,
#                            self.user_name_value, self.user_status_value, self.user_pwd_value)
#         self.user.search(self.user_name_value)
#         self.user.update_user(self.user_name_value, self.updated_user_name)
#         self.user.search(self.updated_user_name)
#         self.user.delete(self.updated_user_name)
#         self.pim = AddEmployee(self.driver)
#         self.pim.delete_employee(self.employee_last_name)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.login.quit_browser()
#
# if __name__ == "__main__":
#     unittest.main()
#
#
#
#
