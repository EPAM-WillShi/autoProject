# -*- coding: utf-8 -*-

from lib.log import Log
from pageobjects.leave.leave import Leave


class EmployeeEntitlements(Leave):
    employee_name_ele = ('id', 'entitlements_employee_empName')
    leave_type_ele = ('id', 'entitlements_leave_type')
    leave_period_ele = ('id', 'period')
    search_btn = ('id', 'searchBtn')
    search_results = ('xpath', '//table[@id="resultTable"]//td')
    checkall_btn = ('id', 'ohrmList_chkSelectAll')
    delete_btn = ('id', 'btnDelete')
    ok_btn = ('id', 'dialogDeleteBtn')
    cancel_btn = ('class_name', 'btn reset')

    def __init__(self, browser):
        super(EmployeeEntitlements, self).__init__(browser)
        self.click_menu("Entitlements")
        self.click_menu("Employee Entitlements")

    def search_leave_entitlements(self, name, leave_type, leave_period):
        self.set_combox_value(leave_type, self.leave_type_ele)
        self.set_combox_value(leave_period, self.leave_period_ele)
        self.input_text(name, self.employee_name_ele)
        self.press_enter_key(self.employee_name_ele)
        self.click(self.search_btn)

    def check_search_results(self):
        if self.get_element_text(self.search_results) == "No Records Found":
            print("No such records found!")
        else:
            print("Record is found!")

    def delete_all_leave_entitlements(self):
        self.click(self.checkall_btn)
        self.click(self.delete_btn)
        self.click(self.ok_btn)

