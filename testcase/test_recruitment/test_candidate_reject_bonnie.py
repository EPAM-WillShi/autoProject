# -*- coding: utf-8 -*-
"""
Created on 2018/4/18

@author: Bonnie_Wang
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.recruitment.candidates import Candidates
from pageobjects.recruitment.vacancies import Vacancies


class TestCandirej(unittest.TestCase):
    """
    Test PIM page Employee List Panel
    """
    browser = config.BROWSER
    # vacancy elements
    vacan_name = 'Test Vacancy'
    job_title = 'IT Manager'
    hiring_manager = 'Thomas Fleming'

    # candidates elements
    first_name = 'Vfirst'
    last_name = 'Vlast'
    email = first_name + '.' + last_name + '@epam.com'
    status = 'Reject'
    status_reason = 'Test vacancy rejection'

    @classmethod
    def setUpClass(cls):
        # Login
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.candidates = Candidates(cls.driver)
        cls.vacancy = Vacancies(cls.driver)

    def test_vacancy_rej(self):
        """
        Test Change the candidate status to reject Function
        """
        self.vacancy.delete_vacancies( self.vacan_name)
        self.vacancy.add_vacancies_required( self.job_title, 
                self.vacan_name, self.hiring_manager)
        self.candidates.delete_candidates( self.vacan_name)
        self.candidates.add_candidates_required( self.first_name, 
                self.last_name, self.email, self.vacan_name)
        self.candidates.candidates_edit_status( self.vacan_name,
                self.status, self.status_reason)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()
