# coding:utf-8
"""
Created on 2018/04/27

@author: Julia_Zhu
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.config.optional_fields import PIM


class SelectOptional(unittest.TestCase):
    """
    Test Pim page functions
    """
    browser = config.BROWSER

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.optional_fields = PIM(cls.driver)

    def test_edit_pim_config(self):
        """
        Click the "Configuration-->Optional Fields" menu for pim page,
        edit the optional fields and select the checkbox of "Show US Tax Exemptions menu"
        verify the selected checkbox value is correct
        """
        self.optional_fields.click_menu("Configuration")
        self.optional_fields.click_menu("Optional Fields")
        self.optional_fields.edit_pim_config(False, False, False, True)
        self.optional_fields.assert_selected_values(False, False, False, True)

    @classmethod
    def tearDownClass(cls):
         cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()