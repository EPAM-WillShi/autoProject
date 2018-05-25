# -*- coding: utf-8 -*-

from pageobjects.mainpage import MainPage
from lib.log import Log

class Dashboard(MainPage):
    """
    Dashboard page
    """
    #Quick Launch part
    assign_leave = ("xpath","//span[text()='Assign Leave']")
    leave_list = ("xpath","//span[text()='Timesheets']")
    time_sheet = ("xpath","//span[text()='Leave List']")

    def __init__(self, browser):
        super(Dashboard, self).__init__(browser)
        Log.info("Arrive Dashboard page")   
        
    def click_assign_leave(self):
        assign_leave = self.wait_unit_el_present(self.assign_leave)
        if assign_leave is not None:
            self.click(self.assign_leave)
            Log.info("assign leave button is clicked")   
        else:
            raise Exception,"Unable to find the assign leave element"
               
    def click_leave_list(self):
        leave_list = self.wait_unit_el_present(self.leave_list)
        if leave_list is not None:
            self.click(self.leave_list)
            Log.info("Leave list button is clicked")  
        else:
            raise Exception,"Unable to find the assign leave element"
         
    def click_timesheets(self):
        timesheet = self.wait_unit_el_present(self.time_sheet)
        if timesheet is not None:
            self.click(self.time_sheet) 
            Log.info("Tim sheets button is clicked")
        else:
            raise Exception,"Unable to find the assign leave element" 
