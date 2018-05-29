# coding:utf-8
import unittest
from lib.log import Log
from com import utils
from config import config
from pageobjects.flights import Flights


class TestFlights(unittest.TestCase):
    """
    Test login page
    """
    @classmethod
    def setUpClass(cls):
        driver = utils.get_browser_driver(config.BROWSER)
        cls.flights = Flights(driver)
        cls.flights.open_browser(config.LOGIN_URL)
        cls.flights.switch_main_menu("Flights")

    @classmethod
    def tearDownClass(cls):
        cls.flights.quit_browser()


if __name__ == "__main__":
    unittest.main()
