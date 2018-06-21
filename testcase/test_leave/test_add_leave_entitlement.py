# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.leave.entitle.add_leave_entitlement import AddLeaveEntitlement
from pageobjects.pim.add_employee import AddEmployee


class TestAddLeaveEntitlement(unittest.TestCase):
    """
    Test  Add Leave Entitlement page functions
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Create an employee
    first_name = "dora"
    last_name = "testing"

    leave_type = "Vacation US"
    leave_period = "2018-01-01 - 2018-12-31"
    entitlement1 = "15"
    entitlement2 = "2"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.addemployee = AddEmployee(cls.driver)
        cls.addemployee.add_user_employee(cls.first_name, cls.last_name)
        # cls.leaveentitlement = AddLeaveEntitlement(cls.driver)

    def setUp(self):
        self.leaveentitlement = AddLeaveEntitlement(self.driver)

    def test_case1_add_entitlement_for_individual(self):
        """
        test_case1_add_entitlement_for_individual
        """
        self.leaveentitlement.add_entitlement_for_individual(self.first_name, self.last_name, self.leave_type,
                                                             self.leave_period, self.entitlement1)
        self.leaveentitlement.assert_message("Successfully Added")

    def test_case2_add_entitlement_for_multiple_employees(self):
        """
        test_case2_add_entitlement_for_multiple_employees
        """
        self.leaveentitlement.add_entitlement_for_multiple_employees(self.first_name, self.last_name, self.leave_type,
                                                             self.leave_period, self.entitlement1, self.entitlement2)
        self.leaveentitlement.assert_message("Entitlements added")

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()





