# -*- coding: utf-8 -*-
"""
Created on 2018/4/17
@author: Yolanda zhang
"""

from lib.log import Log
from pageobjects.leave.leave import Leave


class WorkWeek(Leave):
    """
    work week page main components
    """
    edit_button = ('id', 'saveBtn')
    monday_dropdown = ('id', 'WorkWeek_day_length_Monday')
    tuesday_dropdown = ('id', 'WorkWeek_day_length_Tuesday')
    message = ('xpath', "//div[contains(@class,'success')]")

    def __init__(self, browser):
        super(WorkWeek, self).__init__(browser)
        self.click_menu("Configure")
        self.click_menu("Work Week")

    def select_month(self):
        self.set_combox_value("Non-working Day", self.tuesday_dropdown)
        self.set_combox_value("Non-working Day", self.monday_dropdown)

    def save_workweek(self):
        self.click(self.edit_button)
        self.select_month()
        self.click(self.edit_button)
        Log.info("Save workweek successfully!")
