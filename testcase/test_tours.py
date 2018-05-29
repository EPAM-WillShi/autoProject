# coding:utf-8
import unittest
from lib.log import Log
from com import utils
from config import config
from pageobjects.tours import Tours


class TestTours(unittest.TestCase):
    """
    Test login page
    """
    @classmethod
    def setUpClass(cls):
        driver = utils.get_browser_driver(config.BROWSER)
        cls.tours = Tours(driver)
        cls.tours.open_browser(config.LOGIN_URL)
        cls.tours.switch_main_menu("Tours")

    @classmethod
    def tearDownClass(cls):
        cls.tours.quit_browser()


if __name__ == "__main__":
    unittest.main()
