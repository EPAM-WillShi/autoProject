# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.time.projectinfo.project import Project
from pageobjects.time.projectinfo.customers import Customers


class TestProjectInfo(unittest.TestCase):
    """
    Test login page
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Create customers
    customer_name = "customer1"
    customer_description = "description1"
    second_customer = "customer11"
    third_customer = "customer12"

    # Create a project
    project_name = "project2"
    project_admin = "John Smith"
    project_description = "description2"

    # Add another project admin
    another_project_admin = "Steven Edwards"

    # Create an activity
    activity_name = "activity1"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.project = Project(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.project.quit_browser()

    def setUp(self):
        """
        Delete all customers (All projects used these customers are also deleted.)
        """
        self.customer = Customers(self.driver)
        self.customer.delete_customer(self.customer_name)
        self.project.go_back_to_project()

    def tearDown(self):
        pass

    def test_case8_project_create_activity(self):  # Create new activity
        self.project.click_add_btn()  # Create a project with new customer
        self.project.add_customer(self.customer_name, self.customer_description)
        self.project.input_project_details(self.project_name, self.project_admin, self.project_description)
        self.project.click_save_btn()
        self.project.click_cancel_btn()
        self.project.open_project(self.project_name)  # Open a project
        self.project.add_activity(self.activity_name)  # Create an activity
        self.project.check_activity(self.activity_name)  # Verify new activity is listed

    def test_case16_project_search_by_projectadmin(self):  # Project search by project admin
        self.project.click_add_btn()  # Create a project with project admin: 'Franc Bridges'
        self.project.add_customer(self.customer_name, self.customer_description)
        self.project.input_project_details(self.project_name, self.project_admin, self.project_description)
        self.project.click_save_btn()
        self.project.click_cancel_btn()
        self.project.click_add_btn()  # Create a project with project admin: 'Franc Bridges' and 'Steven Edwards'
        self.project.add_customer(self.second_customer, self.customer_description)
        self.project.input_project_details(self.project_name, self.project_admin, self.project_description)
        self.project.add_project_admin(self.another_project_admin)
        self.project.click_save_btn()
        self.project.click_cancel_btn()
        self.project.click_add_btn()  # Create a project with project admin: 'Steven Edwards'
        self.project.add_customer(self.third_customer, self.customer_description)
        self.project.input_project_details(self.project_name, self.another_project_admin, self.project_description)
        self.project.click_save_btn()
        self.project.click_cancel_btn()
        self.expected_row = self.project.expected_search_result(self.project_admin)  # Obtain expected row
        self.project.search_projects_by_project_admin(self.project_admin)  # Search projects by 'Franc Bridges'
        self.project.check_search_result(self.expected_row)  # Verify row number is equal to expected row


if __name__ == "__main__":
    unittest.main()
