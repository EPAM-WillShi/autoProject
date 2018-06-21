# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.add_employee import AddEmployee
from pageobjects.pim.employee_list import EmployeeList


class TestAddEmployee(unittest.TestCase):
    """
    Test PIM Add Employee page functions
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Create an employee
    first_name = "linda"
    middle_name = "test"
    last_name = "zang"
    upload_file = "1.png"
    login_name = "linda1"
    login_password = "password"
    confirm_password = "password"
    user_status = "Enabled"
    name = "linda zang"

    @classmethod
    def setUpClass(cls):    
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)   
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.addemployee = AddEmployee(cls.driver)

    def setUp(self):
        self.employee_list = EmployeeList(self.driver)
        self.employee_list.delete_employee(self.name)
        self.addemployee.go_back_to_add_employee()

    @classmethod
    def tearDownClass(cls):
        cls.addemployee.quit_browser()

    def test_case5_addemployee_without_login(self):
        """
        Test Add Employee - Not create login details
        """
        self.addemployee.input_employee_details(self.first_name, self.middle_name,
                                                self.last_name, self.upload_file)  # Input employee details
        self.employee_id = self.addemployee.get_employee_id_add_page()  # Obtain employee id
        self.addemployee.save_employee()  # Save it and check save successfully
        self.addemployee.check_employee_details(self.first_name, self.middle_name,
                                                self.last_name, self.employee_id)  # Check employee details

    def test_case6_addemployee_with_login(self):
        """
        Test Add Employee - create login details(enable status)
        """
        self.addemployee.input_employee_details(self.first_name, self.middle_name,
                                                self.last_name, self.upload_file)  # Input employee details
        self.addemployee.input_login_details(self.login_name, self.login_password,
                                             self.confirm_password, self.user_status)  # Input login details
        self.employee_id = self.addemployee.get_employee_id_add_page()  # Obtain employee id
        self.addemployee.save_employee()  # Save it and check save successfully
        self.addemployee.check_employee_details(self.first_name, self.middle_name,
                                                self.last_name, self.employee_id)  # Check employee details
        self.addemployee.log_out_btn()  # Logout
        self.login.login(self.login_name, self.login_password)  # Use new employee to login again
        self.login.check_login_status()  # Check Login successfully


if __name__ == "__main__":
    unittest.main()
