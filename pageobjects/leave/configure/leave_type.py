# -*- coding: utf-8 -*-
"""
Created on 2018/4/17
@author: Yolanda Zhang
"""

from lib.log import Log
from pageobjects.leave.leave import Leave


class LeaveType(Leave):
    """
    leave type page main components
    """
    add_button = ('id', 'btnAdd')
    delete_button = ('id', 'btnDelete')
    record = ('link_text', 'test leave')
    delete_confirm_button = ('id', 'dialogDeleteBtn')
    leave_type_name = ('id', "leaveType_txtLeaveTypeName")
    save_btn = ('id', 'saveButton')
    edit_check_box = ('id', 'leaveType_excludeIfNoEntitlement')
    delete_check_box = ('xpath', "//a[contains(text(), 'test leave')]/../preceding-sibling::td/input[@type='checkbox']")
    message = ('xpath', "//div[contains(@class,'success')]")

    def __init__(self, browser):
        super(LeaveType, self).__init__(browser)
        self.click_menu( "Configure")
        self.click_menu("Leave Types")

    def add_leave_type(self, name):
        """
        add leave type
        """
        self.click(self.add_button)
        self.clear_text(self.leave_type_name)
        self.input_text(name, self.leave_type_name, )
        self.click(self.save_btn)
        self.get_element_text(self.message)
        Log.info("Add record successfully!")

    def edit_leave_type(self):
        """
         edit above added leave type
         """
        self.click(self.record)
        self.click(self.edit_check_box)
        self.click(self.save_btn)
        Log.info("Edit record successfully!")

    def delete_leave_type(self):
        """
         delete above added leave type
         """
        self.click(self.delete_check_box)
        self.click(self.delete_button)
        self.click(self.delete_confirm_button)
        Log.info("Delete record successfully!")

