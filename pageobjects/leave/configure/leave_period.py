# -*- coding: utf-8 -*-
"""
Created on 2018/4/17
@author: Molly Xue, Joanna Li
"""
from selenium.webdriver.support.ui import Select
from lib.log import Log
from pageobjects.leave.leave import Leave

class LeavePeriod(Leave):
    """
    Leave-Configure-Leave Period page main components
    """
    leave_period = ('id', 'menu_leave_defineLeavePeriod')
    edit_button = ('XPATH', ".//input[@id='btnEdit'][@value='Edit']")
    save_button = ('XPATH', ".//input[@id='btnEdit'][@value='Save']")
    reset_button = ('id', 'btnReset')
    start_month = ('id', 'leaveperiod_cmbStartMonth')
    start_date = ('id', 'leaveperiod_cmbStartDate')
    end_date = ('XPATH', ".//label[@id='labelEndDate']")
    current_period = ('XPATH', ".//*[@id='frmLeavePeriod']/fieldset/ol/li[4]/span")
    success_msg = ("XPATH", ".//*[@id='location']/div[2]/div")

    def __init__(self, browser):
        """
        Arrive user to Leave Period Page
        """
        super(LeavePeriod, self).__init__(browser)
        self.click_menu("Configure")
        self.wait_unit_el_present(self.leave_period)
        self.click_menu("Leave Period")

    def edit_LeavePeriod(self):
        """
        Click Edit button to enable the Leave Period Page
        """
        self.wait_unit_el_present(self.edit_button)
        self.click(self.edit_button)
        Log.info("Click Edit button to enable the edit leave period page - pass!")

    def select_StartMonth(self, startmonth):
        """
        Select Start Month for Leave Period
        """
        self.wait_unit_el_present(self.start_month)
        self.set_combox_value(value=startmonth, keys=self.start_month)
        Log.info("Start Month is selected on Leave Period Page - pass!")

    def select_StartDate(self, startdate):
        """
        Select Start Date for Leave Period
        """
        self.wait_unit_el_present(self.start_date)
        self.set_combox_value(value=startdate, keys=self.start_date)
        Log.info("Start Date is selected on Leave Period Page - pass!")

    def check_EndDate(self, enddate):
        """
        Check End Date updated for new selected Start Month and Start Date
        """
        self.wait_unit_el_present(self.end_date)
        get_enddate = self.get_element_text(self.end_date)
        assert get_enddate == enddate
        Log.info("End Date is updated according to Start Month and Start Date on Leave Period Page - pass!")

    def check_Current_LeavePeriod(self, period):
        """
        Check Current Leave Period updated based on End Date
        """
        self.wait_unit_el_present(self.current_period)
        get_currentperiod = self.get_element_text(self.current_period)
        assert get_currentperiod == period
        Log.info("Current Leave Period is updated based on End Date on Leave Period Page - pass!")

    def save_LeavePeriod(self):
        """
        Click Save button and check the success message
        """
        self.wait_unit_el_present(self.save_button)
        self.click(self.save_button)
        self.wait_unit_el_present(self.success_msg)
        if self.get_element_text(self.success_msg) is not None:
            assert ("Successfully Saved" in self.get_element_text(self.success_msg))
            Log.info("New Leave Period is saved and success message show - pass!")
        else:
            raise Exception("Didn't get the message about Successfully Saved")

    def reset_leaveperiod(self, startmonth, startdate):
        """
        Reset leave period
        """
        self.sleep(3)
        self.click(self.edit_button)
        assert self.get_element(self.reset_button) is not None

        selector_startmonth = Select(self.get_element(self.start_month))
        option_startmonth = selector_startmonth.first_selected_option
        orig_startmonth = option_startmonth.text
        selector_startdate = Select(self.get_element(self.start_date))
        option_startdate = selector_startdate.first_selected_option
        orig_startdate = option_startdate.text
        orig_enddate = self.get_element_text(self.end_date)

        self.set_combox_value(startmonth, self.start_month)
        self.sleep(3)
        self.set_combox_value(startdate, self.start_date)
        self.sleep(3)
        Log.info("Select new values for start month & start date")

        current_option_startmonth = selector_startmonth.first_selected_option
        current_startmonth = current_option_startmonth.text
        assert current_startmonth == startmonth

        self.click(self.reset_button)
        self.sleep(3)
        Log.info("Click reset button")

        reset_option_startmonth = selector_startmonth.first_selected_option
        reset_startmonth = reset_option_startmonth.text
        assert reset_startmonth == orig_startmonth

        reset_option_startdate = selector_startdate.first_selected_option
        reset_startdate = reset_option_startdate.text
        assert reset_startdate == orig_startdate

        assert self.get_element_text(self.end_date) == orig_enddate