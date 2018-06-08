# -*- coding: utf-8 -*-
"""
Created on 2018/4/17
@author: Yolanda zhang
"""

from lib.log import Log
from pageobjects.leave.leave import Leave
import random


class WorkWeek(Leave):
    """
    work week page main components
    """
    edit_button = ('id', 'saveBtn')
    monday_dropdown = ('id', 'WorkWeek_day_length_Monday')
    tuesday_dropdown = ('id', 'WorkWeek_day_length_Tuesday')
    message = ('xpath', "//div[contains(@class,'success')]")
    """
    Add components by Rachel
    """
    wednesday_dropdown = ('id', 'WorkWeek_day_length_Wednesday')
    thursday_dropdown = ('id', 'WorkWeek_day_length_Thursday')
    friday_dropdown = ('id', 'WorkWeek_day_length_Friday')
    saturday_dropdown = ('id', 'WorkWeek_day_length_Saturday')
    sunday_dropdown = ('id', 'WorkWeek_day_length_Sunday')
    day_value = ['Full Day', 'Half Day', 'Non-working Day']
    monday_choice = random.choice(day_value)
    tuesday_choice = random.choice(day_value)
    wednesday_choice = random.choice(day_value)
    thursday_choice = random.choice(day_value)
    friday_choice = random.choice(day_value)
    saturday_choice = random.choice(day_value)
    sunday_choice = random.choice(day_value)

    def __init__(self, browser):
        super(WorkWeek, self).__init__(browser)
        self.click_menu("Configure")
        self.click_menu("Work Week")

    def select_month(self):
        self.set_combox_value(self.monday_choice, self.monday_dropdown)
        self.set_combox_value(self.tuesday_choice, self.tuesday_dropdown)
        self.set_combox_value(self.wednesday_choice, self.wednesday_dropdown)
        self.set_combox_value(self.thursday_choice, self.thursday_dropdown)
        self.set_combox_value(self.friday_choice, self.friday_dropdown)
        self.set_combox_value(self.saturday_choice, self.saturday_dropdown)
        self.set_combox_value(self.sunday_choice, self.sunday_dropdown)

    def save_workweek(self):
        self.click(self.edit_button)
        self.select_month()
        self.click(self.edit_button)
        Log.info("Save workweek successfully!")
