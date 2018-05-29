# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.admin.job.employment_status import EmploymentStatus


class TestEmploymentStatus(unittest.TestCase):
    """
    Test Employment Status page functions
    """
    browser = config.BROWSER
    status_name = 'test employment status'
    update_name = 'test employment status_updated'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.es = EmploymentStatus(cls.driver)

    def test_case1_add_employee_status(self):
        self.es.add_employee_status(self.status_name)

    def test_case3_edit_employee_status(self):
        self.es.add_employee_status(self.status_name)
        self.es.edit_employee_status(self.update_name)
        self.es.delete_employee_status(self.update_name)

    def test_case2_delete_employee_status(self):
        self.es.delete_employee_status(self.status_name)

    @classmethod
    def tearDownClass(cls):
        cls.es.quit_browser()



if __name__ == "__main__":
    unittest.main()