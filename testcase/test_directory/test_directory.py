# coding:utf-8
"""
Created on 2018/4/25
@author: Molly Xue
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from lib.log import Log
from pageobjects.directory import Directory

class Test_Directory(unittest.TestCase):
    """
    Test Leave-Directory page main components and define the elements on Directory page
    """
    browser = config.BROWSER
    search_name = "Linda"
    search_jobtitle = "HR Manager"
    search_location = "    New York Sales Office"

    first_name = "Molly Test"
    last_name = "Xue"
    jobtitle1 = "IT Manager"
    location1 = "    New York Sales Office"

    @classmethod
    def setUpClass(cls):
        """
        Arrive to Directory page - Search Directory
        """
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.directory = Directory(cls.driver)
        cls.directory.create_employee(cls.first_name, cls.last_name)
        cls.directory.switch_main_menu("Directory")

    def testcase1_resetDirectory(self):
        """
        Directory page test reset functions for name, job title and location
        """
        self.directory.resetDirectory(self.search_name,self.search_jobtitle,self.search_location)
        Log.info("Test reset function on Directory Page for name, job title and location - passed")

    # def testcase2_searchDirectory_One(self):
    #     """
    #     Directory page test search functions one by one for name, job title and location
    #     """
    #     self.directory.searchDirectory_One(self.search_name, self.search_jobtitle, self.search_location)
    #     Log.info("Test search function by name, jobtitle, location one by one - passed")
    #
    # def testcase3_searchDirectory_All(self):
    #     """
    #     Directory page test search functions together for name, job title and location - existed
    #     """
    #     self.directory.search_SearchDirectory_All(self.search_name, self.search_jobtitle, self.search_location)
    #     Log.info("Test exist result while search function by name, jobtitle, location together - passed")

    def testcase4_searchDirectory_No(self):
        """
        Directory page test search functions together for name, job title and location - not existed
        """
        self.directory.search_SearchDirectory_No(self.first_name, self.jobtitle1, self.location1)
        Log.info("Test not exist while search function by name, jobtitle, location together - passed")

    @classmethod
    def tearDownClass(cls):
        cls.directory.delete_employee(cls.last_name)
        cls.login.quit_browser()

if __name__ == "__main__":
    unittest.main()

