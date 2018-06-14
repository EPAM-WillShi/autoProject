# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.emp_memberships import Memberships
from pageobjects.admin.qual.memberships import QualityMemberships


class TestMemberships(unittest.TestCase):
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

    # Create a membership
    membership = "membership_dora_test"

    pay = "Company"
    amount = "110"
    currency = "Chinese Yuan Renminbi"
    abb_currency = "CNY"  # Abbreviation of currency
    com_date = "02-06-2018"
    renew_date = "02-06-2020"

    modified_pay = "Individual"
    modified_amount = "1000"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

        cls.qua_memberships = QualityMemberships(cls.driver)
        cls.qua_memberships.add_quality_membership(cls.membership)

        cls.memberships = Memberships(cls.driver)
        cls.memberships.open_memberships_page_via_creating_emp(cls.first_name, cls.last_name)

    def test_case1_add_membership(self):
        """
        test_case1_add membership information for employee
        """
        self.memberships.add_membership(self.membership, self.pay, self.amount, self.currency,
                                        self.com_date, self.renew_date, self.abb_currency)
        self.memberships.verify_membership_success("Successfully Saved")

    def test_case2_edit_membership(self):
        """
         test_case2_edit membership information for employee
         """
        self.memberships.edit_membership(self.membership, self.modified_pay, self.modified_amount)
        self.memberships.verify_membership_success("Successfully Saved")

    def test_case3_delete_membership(self):
        """
         test_case3_delete membership
         """
        self.memberships.delete_membership(self.membership)
        self.memberships.verify_membership_success("Successfully Deleted")

    @classmethod
    def tearDownClass(cls):
        cls.memberships.quit_browser()

