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

    firstname = "julia1_first"
    lastname = "julia1_last"
    email = "julia_zhu@epam.com"
    contactNo = "789"
    vacan_name = "job_test1"
    status ="Shortlist"
    status_reason = "test note"
    status1 = "Schedule Interview"
    interview_title = "title1"
    interview_name = "Thomas Fleming"
    interview_date = "2018-05-09"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.candidates = Candidates(cls.driver)

    def test_change_candidates(self):
        """
        Test Case:Change the candidate status to shortlist and schedule interview and check if changed action is correct
        """
        self.candidates.click_candidate_menu()
        self.candidates.add_candidates_required(self.firstname, self.lastname, self.email, self.contactNo, self.vacan_name)
        self.candidates.candidates_change_status(self.status, self.status_reason)
        self.candidates.candidates_change_status1(self.status1, self.interview_title, self.interview_name, self.interview_date)


    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()