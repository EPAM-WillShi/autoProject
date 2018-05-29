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

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass

    # def test_login(self):
    #     """
    #     Test login function with correct username and password
    #     """
    #     self.login_with_user.login(self.username, self.passwd)
        # Check the login status
        # self.login_with_user.check_login_status()
        # Log.info("Login successfully!")
        

if __name__ == "__main__":
    unittest.main()