# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.job import Job


class TestJob(unittest.TestCase):
    """
    Test PIM Add Employee page functions
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Create an employee
    first_name = "dora"
    last_name = "testing1"

    jobtitle = "CEO"
    empStatus = "Freelance"


    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.job = Job(cls.driver)

    def setUp(self):
        self.job.switch_main_menu("PIM")

    # def test_case_open_job_page_via_creating_emp(self):

    # def test_open_job_page_via_editing_emp(self):
    #     self.job.open_job_page_via_editing_emp(self.first_name, self.last_name)

    def test_case1_edit_emp_job(self):
        self.job.open_job_page_via_creating_emp(self.first_name, self.last_name)
        self.job.edit_emp_job(self.jobtitle, self.empStatus)

    @classmethod
    def tearDownClass(cls):
        cls.job.quit_browser()


