# -*- coding: utf-8 -*-
"""
Created by Linda
"""
from lib.log import Log
from pageobjects.leave.leave import Leave


class EmployeeEntitlements(Leave):
    name = ('id', 'entitlements_employee_empName')
    search_btn = ('xpath', '//input[@id="searchBtn"]')
    check_all_entitlements = ('id', 'ohrmList_chkSelectAll')
    delete_btn = ('id', 'btnDelete')
    ok_btn = ('id', 'dialogDeleteBtn')
    result = ('id', 'resultTable')
    leave_type = ("id", "entitlements_leave_type")
    leave_period = ("id", "period")
    entitlement = ("id", "entitlements_entitlement")
    save_btn = ("id", "btnSave")
    search_leave_period = ('id', 'period')
    add_btn = ('id', 'btnAdd')

    def __init__(self, browser):
        super(EmployeeEntitlements, self).__init__(browser)
        self.click_menu("Entitlements")
        self.click_menu("Employee Entitlements")

    def search(self, name, period):

        self.input_text(name, self.name)
        self.press_enter_key(self.name)
        self.set_combox_value("All", self.leave_type)
        self.set_combox_value(period, self.search_leave_period)
        self.sleep(3)
        self.click(self.search_btn)
        self.sleep(3)

    def check_result(self):
        if self.get_element_text(self.result) == "No Records Found":
            return False
        else:
            return True

    def delete_all_entitlements(self):
        if self.check_result() is True:
            self.click(self.check_all_entitlements)
            self.click(self.delete_btn)
            self.click(self.ok_btn)

    def add_entitlement(self, name, leave_type, period, entitlement):
        self.sleep(2)
        self.search(name, period)
        self.click(self.add_btn)
        self.set_combox_value(leave_type, self.leave_type)
        self.set_combox_value(period, self.leave_period)
        self.input_text(entitlement, self.entitlement)
        self.input_text(name, self.name)
        self.press_enter_key(self.name)
        self.click(self.save_btn)
        Log.info("Added an entitlement.")


