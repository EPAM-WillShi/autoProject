# coding:utf-8
"""
Created on 2018/04/27

@author: Julia_Zhu
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.config.custom_fields import PIM


class AddCustom(unittest.TestCase):
    """
    Test Pim page functions
    """
    browser = config.BROWSER

    name = "A"
    screen = "Personal Details"
    type = "Text or Number"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.custom_fields = PIM(cls.driver)

    def test_add_custom(self):
        """
        Click the "Configuration-->Custom Fields" menu for pim page,add a new custom field
        """
        self.custom_fields.click_menu("Configuration")
        self.custom_fields.click_menu("Custom Fields")
        self.custom_fields.add_custom_field(self.name, self.screen, self.type)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()