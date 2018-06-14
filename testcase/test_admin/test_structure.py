# -*- coding: utf-8 -*-
import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.login import Login
from pageobjects.admin.org.structure import Structure


class TestOrgStructure(unittest.TestCase):
    """
    Test Structure page functions
    """
    browser = config.BROWSER
    # set testing data
    add_unit_id = '111'
    add_unit_name = 'Tower2'
    add_unit_desc = "The unit is Tower2"

    edit_unit_id = '333'
    edit_unit_name = 'Tower2_edit'
    edit_unit_desc = "The unit is updated"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.structure = Structure(cls.driver)
        Log.info("Start testing organization structure page")

    def test_case01_init_structure(self):
        """
        Test Case  -  structure init check
        """
        self.structure.verify_init_structure()

    def test_case02_add_unit(self):
        """
        Test Case  -  structure unit add
        """
        self.structure.add_unit(self.add_unit_id, self.add_unit_name, self.add_unit_desc)

    def test_case03_delete_unit(self):
        """
        Test Case  -  structure unit delete
        """
        self.structure.delete_unit()

    def test_case04_edit_unit(self):
        """
        Test Case  -  structure unit edit
        """
        self.structure.edit_unit(self.edit_unit_id, self.edit_unit_name, self.edit_unit_desc)

    def test_case05_delete_unit(self):
        """
        Test Case  -  structure unit delete
        """
        self.structure.delete_unit()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()
        Log.info("End testing organization structure page")

if __name__ == "__main__":
    unittest.main()
