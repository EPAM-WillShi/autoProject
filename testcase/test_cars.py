# coding:utf-8
import unittest
from lib.log import Log
from com import utils
from config import config
from pageobjects.cars import Cars


class TestCars(unittest.TestCase):
    """
    Test login page
    """
    @classmethod
    def setUpClass(cls):
        driver = utils.get_browser_driver(config.BROWSER)
        cls.cars = Cars(driver)
        cls.cars.open_browser(config.LOGIN_URL)
        cls.cars.switch_main_menu("Cars")

    @classmethod
    def tearDownClass(cls):
        cls.cars.quit_browser()


if __name__ == "__main__":
    unittest.main()
