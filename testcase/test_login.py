# coding:utf-8
import unittest
from lib.log import Log
from com import utils
from config import config
from pageobjects.login import Login


class TestLogin(unittest.TestCase):
    """
    Test login page
    """
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER
    
    @classmethod
    def setUpClass(cls):    
        driver = utils.get_browser_driver(cls.browser)
        cls.alogin = Login(driver)
        cls.alogin.open_browser(cls.login_url)

    @classmethod
    def tearDownClass(cls):
        cls.alogin.quit_browser()
        
    def test_login_with_normal_account(self):
        """
        Test login function with correct username and password
        """
        Log.info("Test login function with username: %s password: %s" %(self.username, self.passwd))
        self.alogin.login(self.username, self.passwd)
        # Check the login status 
        self.alogin.check_login_status()  
        Log.info("Login successfully!")    

if __name__ == "__main__":
    unittest.main()