# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.immigration import Immigration



class TestImmigration(unittest.TestCase):
    """
    Test PIM Add Employee page functions
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Create an employee
    first_name = "linda"
    last_name = "test"


    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.immigration = Immigration(cls.driver)

    def setUp(self):
        self.immigration.switch_main_menu("PIM")


    @classmethod
    def tearDownClass(cls):
        cls.immigration.quit_browser()

    def test_open_immigration_page_via_creating_emp(self):
        self.immigration.open_immigration_page_via_creating_emp(self.first_name, self.last_name)

    def test_open_immigration_page_via_editing_emp(self):
        self.immigration.open_immigration_page_via_editing_emp(self.first_name, self.last_name)


if __name__ == "__main__":
    unittest.main()