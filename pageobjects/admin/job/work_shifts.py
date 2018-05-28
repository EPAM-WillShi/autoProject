# -*- coding: utf-8 -*-
"""
Created on 2018/4/24
@author: Dora Zhu
"""

from lib.log import Log
from pageobjects.admin.admin import Admin


class WorkShifts(Admin):
    """
    Work Shifts page functions
    """
    # work shifts main page objects
    add_btn = ('ID', 'btnAdd')
    delete_btn = ('ID', 'btnDelete')

    # add work shifts page object
    add_flag = "//*[text()='Add Work Shift']"
    shift_name = ('ID', 'workShift_name')
    workHour_from = ('ID', 'workShift_workHours_from')
    workHour_to = ('ID', 'workShift_workHours_to')
    selectEle = ('ID', 'workShift_availableEmp')
    add_employee_btn = ('ID', 'btnAssignEmployee')
    save_btn = ('ID', 'btnSave')
    message = ('XPATH', "//*[@class='message success fadable']")

    # delete objects
    ok_btn = ('ID', 'dialogDeleteBtn')
    element = '//*[@id="resultTable"]//tr[./td/a[text()="{}"]]//input'

    def __init__(self, browser):
        super(WorkShifts, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Work Shifts")
        Log.info("Arrive at Work shift page")

    def add_work_shift(self, add_name, workHourFrom, workHourTo):
        """
        Add a new work shift
        """
        Log.info("Start to add a work shift")
        self.click(self.add_btn)
        self.input_text(add_name, self.shift_name)
        self.set_combox_value(workHourFrom, self.workHour_from)
        self.set_combox_value(workHourTo, self.workHour_to)
        self.select_option(self.selectEle, 0)
        self.click(self.add_employee_btn)
        self.click(self.save_btn)

    def delete_work_shift(self, add_name):
        """
        Delete work shift
        """
        Log.info("Start to delete a work shift")
        checkbox = self.element.format(add_name)
        ielement = ('XPATH', checkbox)
        self.click(ielement)
        self.sleep(2)
        self.click(self.delete_btn)
        self.sleep(2)
        self.click(self.ok_btn)

    def assert_message(self, return_message):
        """
        Assert the result of current operation
        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)

