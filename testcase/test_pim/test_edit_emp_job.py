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
    first_name = "dora1"
    last_name = "test"

    #Job information
    jobtitle = "CEO"
    empStatus = "Freelance"
    jobcategory = "Sales Workers"
    joindate = "2018-07-17"
    subunit = "Sales"
    location = "Texas R&D"
    startdate = "2018-07-17"
    enddate = "2020-07-16"
    contract = "jobcontract.txt"
    terdate = "2019-07-17"
    repcontract = "repcontract.txt"


    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.job = Job(cls.driver)
        cls.job.open_job_page_via_creating_emp(cls.first_name, cls.last_name)

    def test_case1_add_emp_job(self):
        """
        test_case1_add job information for employee
        """
        self.job.add_emp_job(self.jobtitle, self.empStatus, self.jobcategory, self.joindate, self.subunit,
                               self.location, self.startdate, self.enddate, self.contract)
        self.job.verify_edit_job_success("Successfully Updated")

    def test_case2_edit_current_contract(self):
        """
        test_case2_replace contract and delete contract
        """
        self.job.replace_current_contract(self.repcontract)
        self.job.verify_edit_job_success("Successfully Updated")
        self.job.delete_current_contract()
        self.job.verify_edit_job_success("Successfully Updated")

    def test_case3_actions_on_employment(self):
        """
        test_case3_terminate employment and activate employment
        """
        self.job.terminate_employment(self.terdate)
        self.job.verify_edit_job_success("Successfully Updated")
        self.job.activate_employment()
        self.job.verify_edit_job_success("Successfully Updated")

    @classmethod
    def tearDownClass(cls):
        cls.job.quit_browser()


