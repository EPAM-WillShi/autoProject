# coding:utf-8
"""
Created on 2018/04/27

@author: Julia_Zhu
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.recruitment.vacancy import Vacancy


class AddVacancy(unittest.TestCase):
    """
    Test Recruitment page functions
    """
    browser = config.BROWSER

    jobtitle = "HR Manager"
    vacancyname = "job_test1"
    hiringmanager = "Fiona Grace"
    positionNo = "01"
    desc = "description1"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.vacancy = Vacancy(cls.driver)

    def test_add_vacancies(self):
        """
        Click the "Recruitment-->Vacancies" menu for recruitment page, and add a new vacancy
        """
        self.vacancy.click_vacancies_menu()
        self.vacancy.add_vacancies_required(self.jobtitle, self.vacancyname, self.hiringmanager, self.positionNo, self.desc)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()