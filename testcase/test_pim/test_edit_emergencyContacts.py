# coding:utf-8

import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.login import Login
from pageobjects.pim.edit_emergencyContacts import EditEmergencyContacts

class TestEditEmergencyContacts(unittest.TestCase):
    """
    Test Edit Emergency Contacts function
    """
    browser = config.BROWSER
    first_name = 'wang'
    last_name = 'test'
    name = 'TestWang'
    relationship = 'Relation'
    homePhone = '123'
    mobile = '000'
    workPhone = '456'
    attachment = '1.png'
    comment = 'TestCommt'

    upname = 'editwang'
    uprelationship = 'editship'
    uphomePhone = '456'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.emg = EditEmergencyContacts(cls.driver)

    def test_case1_open_emergency_page_via_creating_emp(self):
        """
        Test add emergency contacts function
        """
        self.emg.open_emergency_page_via_creating_emp(self.first_name, self.last_name)
        self.emg.add_emg_contacts(self.name, self.relationship, self.homePhone, self.mobile, self.workPhone)
        self.emg.assert_message("Successfully Saved")
        self.emg.add_attach(self.attachment, self.comment)
        self.emg.assert_message("Successfully Saved")

    def test_case2_edit_emg_contacts(self):
        """
        Test edit emergency contacts function
        """
        self.emg.edit_emg_contacts(self.name, self.upname, self.uprelationship, self.uphomePhone)
        self.emg.assert_message("Successfully Saved")

    def test_case3_delete_emg_contacts(self):
        """
        Test delete emergency contacts function
        """
        self.emg.delete_emg_contacts(self.upname)
        self.emg.assert_message("Successfully Deleted")


    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()
        Log.info("End testing Emergency Contacts page")


if __name__ == "__main__":
    unittest.main()