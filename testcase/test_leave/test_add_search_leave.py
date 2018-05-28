# coding:utf-8
"""
Created by Tina Lu
"""
import unittest
from com import utils
from config import config
from pageobjects.login import Login
from pageobjects.leave.entitle.add_search_leave import AddLeaveEntitlement


class TestAddLeaveEntitlement(unittest.TestCase):
    """
    Test Add/Search leave entitlements page functions
    """
    browser = config.BROWSER

    first_name = "Tina"
    last_name = "AddLeave"
    start_month = "January"
    start_date = "1"
    leave_type_input_cancel = "FMLA US"
    leave_type_input = "Paternity US"
    leave_type_input_multiple = "Vacation US"
    leave_type_input_delete = "All"
    leave_period_input = "2018-01-01 - 2018-12-31"
    entitlement_input = "10"
    location_input = "All"
    unit_input = "All"

    @classmethod
    def setUpClass(cls):
        """
        Login, create an employee, set leave period and go to Add leave entitlement page
        """
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)

        cls.addleave = AddLeaveEntitlement(cls.driver)
        cls.addleave.create_employee(cls.first_name, cls.last_name)
        cls.addleave.modify_leave_period(cls.start_month, cls.start_date)

        cls.addleave.select_menu()

    def test_case1_cancel_leave_individual_employee(self):
        """
        Cancel leave entitlement for individual employee
        """
        self.addleave.input_employee_name(self.first_name + " " + self.last_name)
        self.addleave.select_type_period(self.leave_type_input_cancel, self.leave_period_input)
        self.addleave.input_entitlement(self.entitlement_input)
        self.addleave.cancel()

        self.addleave.input_employee_name(self.first_name + " " + self.last_name)
        self.addleave.select_type_period(self.leave_type_input_cancel, self.leave_period_input)
        self.addleave.click_search_btn()
        self.addleave.verify_no_record()

    # def test_case2_add_leave_individual_employee(self):
    #     """
    #     Add leave entitlement for individual employee
    #     """
        self.addleave.click_add_btn()
        self.addleave.input_employee_name(self.first_name + " " + self.last_name)
        self.addleave.select_type_period(self.leave_type_input, self.leave_period_input)
        self.addleave.input_entitlement(self.entitlement_input)
        self.addleave.save()

        self.addleave.input_employee_name(self.first_name + " " + self.last_name)
        self.addleave.select_type_period(self.leave_type_input, self.leave_period_input)
        self.addleave.click_search_btn()
        self.addleave.verify_new_leave(self.leave_period_input, self.entitlement_input)

    # def test_case3_add_leave_multiple_employees(self):
    #     """
    #     Add leave entitlement for multiple employees
    #     """
        self.addleave.click_add_btn()
        self.addleave.click_multiple_employee()
        self.addleave.input_location_unit(self.location_input, self.unit_input)
        self.addleave.select_type_period(self.leave_type_input_multiple, self.leave_period_input)
        self.addleave.input_entitlement(self.entitlement_input)
        self.addleave.save_and_match()

        self.addleave.input_employee_name(self.first_name + " " + self.last_name)
        self.addleave.select_type_period(self.leave_type_input_multiple, self.leave_period_input)
        self.addleave.click_search_btn()
        self.addleave.verify_new_leave(self.leave_period_input, self.entitlement_input)

    # def test_case4_cancel_delete_leave_entitlement(self):
    #     """
    #     Try to delete leave entitlement for one employee, but cancel
    #     """
        self.addleave.delete_leave_cancel()
        self.addleave.input_employee_name(self.first_name + " " + self.last_name)
        self.addleave.select_type_period(self.leave_type_input_multiple, self.leave_period_input)
        self.addleave.click_search_btn()
        self.addleave.verify_new_leave(self.leave_period_input, self.entitlement_input)

    # def test_case5_delete_all_leave_entitlements(self):
    #     """
    #     Delete all leave entitlement for one employee
    #     """
        self.addleave.input_employee_name(self.first_name + " " + self.last_name)
        self.addleave.select_type_period(self.leave_type_input_delete, self.leave_period_input)
        self.addleave.click_search_btn()
        self.addleave.delete_all_leave()
        self.addleave.verify_no_record()

    @classmethod
    def tearDownClass(cls):
        """
        Delete employee and logout
        """
        cls.addleave.delete_employee(cls.first_name, cls.last_name)
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()
