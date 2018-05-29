# coding:utf-8
import unittest
from lib.log import Log
from com import utils
from config import config
from pageobjects.hotels import Hotels


class TestHotels(unittest.TestCase):
    """
    Test login page
    """
    @classmethod
    def setUpClass(cls):
        driver = utils.get_browser_driver(config.BROWSER)
        cls.hotels = Hotels(driver)
        cls.hotels.open_browser(config.LOGIN_URL)
        cls.hotels.switch_main_menu("Hotels")

    @classmethod
    def tearDownClass(cls):
        cls.hotels.quit_browser()


if __name__ == "__main__":
    unittest.main()
