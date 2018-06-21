# -*- coding: utf-8 -*-
import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.login import Login
from pageobjects.admin.org.locations import Location


class TestOrgLocation(unittest.TestCase):
    """
    Test location page functions
    """
    browser = config.BROWSER
    # set testing data
    add_loc_name = "test-loc"
    add_loc_province = "test-province"
    add_loc_city = "test-city"
    add_loc_address = "test-address"
    add_loc_zip = "1111"
    add_loc_phone = "2222"
    add_loc_fax = "3333"
    add_loc_notes = "test-notes"

    edit_loc_name = "edit-test-loc"
    edit_loc_province = "edit-test-province"
    edit_loc_city = "edit-test-city"
    edit_loc_address = "edit-test-address"
    edit_loc_zip = "111155"
    edit_loc_phone = "222255"
    edit_loc_fax = "333355"
    edit_loc_notes = "edit-test-notes"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.location = Location(cls.driver)
        Log.info("Start testing organization structure page")

    def test_case01_add_location(self):
        """
        Test Case  -  org location add
        """
        self.location.add_location(self.add_loc_name, self.add_loc_province, self.add_loc_city, self.add_loc_address, self.add_loc_zip, self.add_loc_phone, self.add_loc_fax, self.add_loc_notes)

    def test_case02_delete_location(self):
        """
        Test Case  -  org location delete
        """
        self.location.delete_location()

    def test_case03_edit_location(self):
        """
        Test Case  -  org location edit
        """
        self.location.edit_location(self.edit_loc_name, self.edit_loc_province, self.edit_loc_city, self.edit_loc_address, self.edit_loc_zip, self.edit_loc_phone, self.edit_loc_fax, self.edit_loc_notes)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()
        Log.info("End testing organization location page")

if __name__ == "__main__":
    unittest.main()