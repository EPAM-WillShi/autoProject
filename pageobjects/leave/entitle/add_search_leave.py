# -*- coding: utf-8 -*-
"""
Created by Tina Lu
"""
from lib.log import Log
from pageobjects.leave.leave import Leave
from pageobjects.pim.add_employee import AddEmployee
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.leave.configure.leave_period import LeavePeriod


class AddLeaveEntitlement(Leave):
    """
    Add leave entitlements and Employee Entitlements pages main components
    """
    employee_name = ("id", "entitlements_employee_empName")
    leave_type = ("id", "entitlements_leave_type")
    leave_period = ("id", "period")
    entitlement = ("id", "entitlements_entitlement")
    save_btn = ("id", "btnSave")
    cancel_btn = ("id", "btnCancel")
    search_btn = ("id", "searchBtn")
    multiple_employee_checkbox = ("id", "entitlements_filters_bulk_assign")
    location = ("id", "entitlements_filters_location")
    sub_unit = ("id", "entitlements_filters_subunit")
    confirm_btn = ("id", "dialogUpdateEntitlementConfirmBtn")
    match_btn = ("id", "dialogConfirmBtn")
    checkbox_all = ("id", "ohrmList_chkSelectAll")
    add_btn = ("id", "btnAdd")
    delete_btn = ("id", "btnDelete")
    dialog_ok_btn = ("id", "dialogDeleteBtn")

    cancel_confirm_btn = ("xpath", "//input[@value='Cancel']")
    search_title= ("xpath","//h1[text()='Leave Entitlements']")
    no_result = ("xpath","//td[text()='No Records Found']")
    add_title = ("xpath","//h1[text()='Add Leave Entitlement']")
    match_title = ("xpath", "//h3[text()='OrangeHRM - Matching Employees']")
    confirm_title = ("xpath", "//h3[text()='OrangeHRM - Confirmation Required']")

    search_table_element = "//div[@id='tableWrapper']/table/tbody/tr[1]"

    def __init__(self, browser):
        super(AddLeaveEntitlement, self).__init__(browser)

    def select_menu(self):
        """
        Go to Add Entitlements page
        """
        self.switch_main_menu("leave")
        self.click_menu("Entitlements")
        self.click_menu("Add Entitlements")
        self.sleep(2)
        Log.info("Arrive Add Entitlements page")

    def create_employee(self, first_name, last_name):
        """
        Go to PIM, create a new employee
        """
        self.addemployee = AddEmployee(self.driver)
        self.addemployee.add_user_employee(first_name, last_name)

    def delete_employee(self, first_name, last_name):
        """
        Go to PIM, delete an employee
        """
        self.employeelist = EmployeeList(self.driver)
        self.employeelist.delete_employee(first_name + " " + last_name)

    def modify_leave_period(self, start_month, start_date):
        """
        Go to Leave - Configure to modify leave period
        """
        self.leaveperiod = LeavePeriod(self.driver)
        self.leaveperiod.edit_LeavePeriod()
        self.leaveperiod.select_StartMonth(start_month)
        self.leaveperiod.select_StartDate(start_date)
        self.leaveperiod.save_LeavePeriod()

    def input_employee_name(self, name):
        """
        Input employee name
        """
        self.clear_text(self.employee_name)
        self.input_text(name, self.employee_name)
        self.press_enter_key(self.employee_name)
        self.sleep(1)

    def select_type_period(self, leave_type, period):
        """
        Select leave type,period and entitlement
        """
        self.set_combox_value(leave_type, self.leave_type)
        self.set_combox_value(period, self.leave_period)

    def input_entitlement(self, entitlement):
        """
        Input entitlement
        """
        self.clear_text(self.entitlement)
        self.input_text(entitlement, self.entitlement)

    def save(self):
        """
        Click save button and confirm if updating dialog pops up
        """
        self.click(self.save_btn)
        self.sleep(3)
        assert self.get_element(self.search_title).is_displayed()
        Log.info("Save the new leave successfully")

    def cancel(self):
        """
        Click cancel button
        """
        self.click(self.cancel_btn)
        self.sleep(3)
        assert self.get_element(self.search_title).is_displayed()
        Log.info("Cancel to add new leave")

    def save_and_match(self):
        """
        Click save button and confirm on matching dialog
        """
        self.click(self.save_btn)
        self.sleep(3)

        self.wait_unit_el_present(self.match_title)
        self.click(self.match_btn)
        assert self.get_element(self.search_title).is_displayed()
        Log.info("Save the new leave for multiple employees successfully")

    def click_search_btn(self):
        """
        Click search button
        """
        self.click(self.search_btn)
        self.sleep(3)

    def click_multiple_employee(self):
        """
        Click add to multiple employees button
        """
        self.click(self.multiple_employee_checkbox)
        assert self.get_element(self.location).is_displayed()
        assert self.get_element(self.sub_unit).is_displayed()

    def input_location_unit(self, location, unit):
        """
        Input location and sub unit information
        """
        self.set_combox_value(location, self.location)
        self.set_combox_value(unit, self.sub_unit)

    def verify_no_record(self):
        """
        Verify no record in search table
        """
        assert self.get_element(self.no_result).is_displayed()
        Log.info("No new leave is added")

    def verify_new_leave(self, leave_period, entitlement):
        """
        Verify search table result for leave type not All
        """
        assert "Added" == self.get_element_text(("xpath", self.search_table_element + "/td[2]")).encode("utf-8")
        assert leave_period.split(" - ")[0] == \
               self.get_element_text(("xpath", self.search_table_element + "/td[3]")).encode("utf-8")
        assert leave_period.split(" - ")[1] == \
               self.get_element_text(("xpath", self.search_table_element + "/td[4]")).encode("utf-8")
        assert '{:.2f}'.format(float(entitlement)) == \
               self.get_element_text(("xpath", self.search_table_element + "/td[5]")).encode("utf-8")
        Log.info("Add new leave entitlement successfully")

    def click_add_btn(self):
        """
        Click Add button to switch to Add Entitlements page
        """
        self.click(self.add_btn)
        self.wait_unit_el_present(self.add_title)

    def delete_leave_cancel(self):
        """
        Find record in table, delete then cancel
        """
        self.click(self.checkbox_all)
        self.click(self.delete_btn)
        self.wait_unit_el_present(self.confirm_title)
        self.click(self.cancel_confirm_btn)
        self.wait_unit_el_present(self.search_title)
        Log.info("Cancel to delete leave entitlements")

    def delete_all_leave(self):
        """
        Find all records in table and delete
        """
        self.click(self.checkbox_all)
        self.click(self.delete_btn)
        self.wait_unit_el_present(self.confirm_title)
        self.click(self.dialog_ok_btn)
        Log.info("Delete leave entitlements successfully")