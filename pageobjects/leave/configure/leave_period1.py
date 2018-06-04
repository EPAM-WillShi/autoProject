# -*- coding: utf-8 -*-
"""
Created on 2018/6/1
@author: Christine Lu
"""

from selenium.webdriver.support.ui import Select
from lib.log import Log
from pageobjects.leave.leave import Leave

class LeavePeriod(Leave):
    """
    Leave Period page main components
    """
    edit_btn = ('XPATH', ".//input[@id='btnEdit'][@value='Edit']")
    save_btn = ('XPATH', ".//input[@id='btnEdit'][@value='Save']")
    reset_bth = ("id", "btnReset")
    start_month = ("id", "leaveperiod_cmbStartMonth")
    start_date = ("id", "leaveperiod_cmbStartDate")
    end_date = ('XPATH', ".//label[@id='labelEndDate']")
    current_period = ('XPATH', ".//*[@id='frmLeavePeriod']/fieldset/ol/li[4]/span")
    success_msg = ("XPATH", ".//*[@id='location']/div[2]/div")

    def __init__(self, browser):
        """
        Arrive to Leave Period Page
        """
        super(LeavePeriod, self).__init__(browser)
        self.click_menu("Configure")
        self.click_menu("Leave Period")
        Log.info("Arrive to Leave Period page - pass!")

    def edit_leave_page(self):
        self.wait_unit_el_present(self.edit_btn)
        self.click(self.edit_btn)
        Log.info("Click edit button to enable editing leave period page - pass!")

    def select_start_month(self, startmonth):
        self.wait_unit_el_present(self.start_month)
        self.set_combox_value(value=startmonth, keys=self.start_month)
        Log.info("Start month has been selected - pass!")

    def select_start_date(self, startdate):
        self.wait_unit_el_present(self.start_date)
        self.set_combox_value(value=startdate, keys=self.start_date)
        Log.info("Start date has been selected - pass!")

    def check_end_date(self, enddate):
        self.wait_unit_el_present(self.end_date)
        get_enddate = self.get_element_text(self.end_date)
        assert get_enddate == enddate
        Log.info("End date is updated - pass!")

    def check_current_leave_period(self, period):
        self.wait_unit_el_present(self.current_period)
        get_currentperiod = self.get_element_text(self.current_period)
        assert get_currentperiod == period
        Log.info("Current leave period is updated - pass!")

    def save_leave_period(self):
        self.wait_unit_el_present(self.save_bth)
        self.click(self.save_bth)
        self.wait_unit_el_present(self.success_msg)
        assert "Successfully Saved" in self.get_element_text(self.success_msg)
        Log.info("Leave period is saved - pass!")



