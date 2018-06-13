# -*- coding: utf-8 -*-
"""
Created on 2018/6/4
@author: Christine Lu
"""

from lib.log import Log
from pageobjects.leave.leave import Leave
import time


class LeaveList(Leave):
    """
    Leave list page main components
    """
    area = ("xpath", "//*[@id='frmFilterLeave']/fieldset/ol/li[1]/label")
    from_date = ("id", "calFromDate")
    to_date = ("id", "calToDate")
    leave_status = ("id", "leaveList_chkSearchFilter_2")
    srch_btn = ("id", "btnSearch")
    srch_result = ('xpath', './/*[@id="resultTable"]//td')
    action_list = ("xpath", "//table[@id='resultTable']/tbody/tr[1]/td[last()]/select")
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

    def leave_list_action(self, actionlist):
        Log.info("Click cancel from the action list")
        self.set_combox_value(value=actionlist, keys=self.action_list)
        self.click(self.save_btn)

