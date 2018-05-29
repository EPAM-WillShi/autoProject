# coding:utf-8
"""
Created on 2018/04/27

@author: Julia_Zhu
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.recruitment.candidates import Candidates


class AddCandidate(unittest.TestCase):
    """
    Test Recruitment page functions
    """
    browser = config.BROWSER

    firstname = "julia_first"
    lastname = "julia_last"
    email = "julia_zhu@epam.com"
    contactNo = "123"
    vacan_name = "job_test1"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.candidates = Candidates(cls.driver)

    def test_recruit_candidates(self):
        """
        Test Case:Configuration-Custom fields on recruitment screen(add a new candidate,
        edit a candidate, delete a specific candidate
        """
        self.candidates.click_candidate_menu()
        self.candidates.add_candidates_required(self.firstname, self.lastname, self.email, self.contactNo, self.vacan_name)
        self.candidates.edit_candidate_contact(contactNo = "456")
        self.candidates.delete_candidates(vacan_name = "job_test1")


    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()