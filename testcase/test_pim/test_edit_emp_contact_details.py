# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.emplist_contact_details import ContactDetails


class TestContactDetails(unittest.TestCase):
    """
    Test PIM Add Employee page functions
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Edit an employee
    first_name = "Christine"
    last_name = "Lu"

    # Edit contact details
    contact_street1 = "Xinghu Street"
    contact_city = "Suzhou"
    mobile = "18012345654"
    workemail = "test2@epam.com"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.CD = ContactDetails(cls.driver)

    def setUp(self):
        self.CD.switch_main_menu("PIM")

    def test_edit_contact_details(self):
        self.CD.open_contact_details_page_via_creation(self.first_name, self.last_name)
        # self.CD.open_contact_details_page_via_edition(self.first_name, self.last_name)
        self.CD.click_edit_button()
        self.CD.edit_contact_street1(self.contact_street1)
        self.CD.edit_contact_city(self.contact_city)
        self.CD.edit_contact_mobile(self.mobile)
        self.CD.edit_work_email(self.workemail)
        self.CD.click_save_button()
        try:
            self.CD.assert_message("Successfully Saved")
            print("Test Pass!")
        except Exception as e:
            print("Test Fail!", format(e))

    @classmethod
    def tearDownClass(cls):
        cls.CD.quit_browser()

if __name__ == "__main__":
    unittest.main()