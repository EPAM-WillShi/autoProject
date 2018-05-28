# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.performance.performance import Performance


class TestLeave(unittest.TestCase):
    """
    Test Leave page functions
    """
    browser = config.BROWSER
    
    @classmethod
    def setUpClass(cls):    
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)   
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.leave = Performance(cls.driver)
         
    def test_click_menu(self):
        """
        This is a demo function to entry second menu page
        """
        self.leave.click_menu("Manage Reviews")
        self.leave.click_menu("Manage Reviews")
                    
    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()
        
if __name__ == "__main__":
    unittest.main()