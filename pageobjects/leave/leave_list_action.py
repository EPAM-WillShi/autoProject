# -*- coding: utf-8 -*-
"""
Created on 2018/6/4
@author: Christine Lu
"""

from lib.log import Log
from pageobjects.leave.leave import Leave


class LeaveList(Leave):
    """
    Leave list page main components
    """
    area = ("xpath", "//*[@id='frmFilterLeave']/fieldset/ol/li[1]/label")
    from_date = ("id", "calFromDate")
    to_date = ("id", "calToDate")
    leave_status = ("id", "leaveList_chkSearchFilter_checkboxgroup_allcheck")
    srch_btn = ("id", "btnSearch")
    srch_result = ('xpath', './/*[@id="resultTable"]//td')
    action_list = ("xpath", "//table[@id='resultTable']/tbody/tr[1]/td[last()]/select")
    emp_name_list = ("xpath", "//table[@id='resultTable']/tbody/tr/td[position()=2]")
    detailed_view_ele = "//table[@id='resultTable']/tbody/tr[./td[2]/a[text()='{}']]//td[8]/a"
    status_list_ele = "//table[@id='resultTable']/tbody/tr[./td[2]/a[text()='{}']]//td[6]/a"
    status_ele = ("xpath", "//table[@id='resultTable']/tbody/tr[1]/td[5]")
    save_btn = ("id", "btnSave")

    def __init__(self, browser):
        super(LeaveList, self).__init__(browser)
        self.click_menu("Leave List")
        Log.info("Arrive leave list page!")

    def search_leave_list(self, fdate, tdate):
        self.wait_unit_el_present(self.from_date)
        self.input_text(fdate, self.from_date)
        self.input_text(tdate, self.to_date)
        self.click(self.leave_status)
        self.click(self.srch_btn)
        Log.info("Search leave list")
        srch_res = self.get_element_text(self.srch_result)
        if srch_res == 'No Records Found':
            print("No records found!")
        else:
            print("Record is found!")

    def verify_employee_name(self, empname):
        for name in self.emp_name_list:
            if name == empname:
                return name
        Log.info("Find the employee you just created!")

    def leave_list_action(self, action):
        Log.info("Click cancel from the action list")
        self.set_combox_value(value=action, keys=self.action_list)
        self.click(self.save_btn)

    # def leave_list_action_via_empname(self, empname, action):
    #     Log.info("Click cancel from the action list")
    #     find_emp = self.action_list_ele.format(empname)
    #     emp = ('xpath', find_emp)
    #     self.set_combox_value(value=action, keys=emp)
    #     self.click(self.save_btn)

    # Go to Detailed View
    def leave_list_action_via_empname(self, empname, action):
        Log.info("Click cancel from the action list")
        find_emp = self.detailed_view_ele.format(empname)
        self.click(("xpath", find_emp))
        self.set_combox_value(value=action, keys=self.action_list)
        self.click(self.save_btn)

    # def verify_leave_list_status(self, empname, status):
    #     find_emp = self.status_list_ele.format(empname)
    #     emp_status = ("xpath", find_emp)
    #     self.get_element_text(emp_status)
    #     if emp_status == status:
    #         print("Test pass!")
    #     else:
    #         print("Test fail!")

    def verify_leave_list_status(self, status):
        emp_status = self.get_element_text(self.status_ele)
        if emp_status == status:
            print("Test pass!")
        else:
            print("Test fail!")





