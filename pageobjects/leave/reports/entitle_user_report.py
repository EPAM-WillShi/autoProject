# -*- coding: utf-8 -*-
"""
Created on 2018/4/17
@author: Molly Xue
"""

from pageobjects.leave.leave import Leave
from lib.log import Log

class EntitleUserReport(Leave):
    """
    Leave-Reports-Employee main components
    """
    leave_entitlement_menu = ('id', 'menu_leave_viewLeaveBalanceReport')
    reports_menu = ('id', 'menu_leave_Reports')
    generate_for = ('id', 'leave_balance_report_type')
    employee = ('id', 'leave_balance_employee_empName')
    employee_check = ('id', 'leave_balance_employee_empId')
    time_duration = ('id', 'period')
    view_button = ('id', 'viewBtn')
    leave_type_table = ('XPATH', "//*[@class= 'header']/../../tr[2]")
    leave_type_table_1 = ('XPATH', "//*[@class= 'header']/../../tr[2]/th[1]")
    leave_type = ('id', 'leave_balance_leave_type')
    job_title = ('id', 'leave_balance_job_title')
    location = ('id', 'leave_balance_location')
    sub_unit = ('id', 'leave_balance_sub_unit')
    past_employee_include = ('id', 'leave_balance_include_terminated')
    
    def __init__(self, browser):
        super(EntitleUserReport, self).__init__(browser)
        self.click_menu("Reports")
        self.wait_unit_el_present(self.leave_entitlement_menu)
        self.click_menu("Leave Entitlements and Usage Report")
        Log.info("Arrive Leave page")

    def select_employee(self,report_type):
        """
        select Enployee for Generate For
        """
        self.set_combox_value(value=report_type, keys=self.generate_for)
        reporttype = self.get_element_attribute(self.generate_for, "value")
        assert reporttype == "2"
        Log.info("Employee leave type format is selected")

    def select_name(self,employee_name):
        """
        select Enployee name for Employee
        """
        self.input_text(value=employee_name, keys=self.employee)
        self.press_enter_key(self.employee)
        t = self.get_element_attribute(self.employee, "value")
        if t == employee_name:
            d = self.get_element_attribute(self.employee_check, "value")
            if d == "Invalid":
                print "Employee name does exist! Please enter another name!"
            else:
                pass
        else:
            print "Employee name is selected:", t
        Log.info("Employee name is selected")

    def select_timeperiod(self,employee_timeperiod):
        """
        select Date range for From
        """
        self.set_combox_value(value=employee_timeperiod, keys=self.time_duration)
        # print "From is selected:", employee_timeperiod
        Log.info("Employ from is selected")

    def review_report(self):
        """
        click view button to query out results
        """
        self.click(self.view_button)
        Log.info("View button is clicked")

    def table_list(self):
        """
        check the query out results meet the expected table contains the expected columns
        """
        assert self.get_element(self.leave_type_table).is_displayed()
        column_1 = self.get_element_text(self.leave_type_table_1)
        assert column_1 == "Leave Type"
        Log.info("Employ report table show")
        
    def select_LeaveType(self, generatetype,leavetype,datefrom,role,checkvalue,departname):
        """
        test Leave Type report on Leave Entitlements and Usage Report
        """
        self.set_combox_value(value=generatetype, keys=self.generate_for)
        Log.info("Generate For is selected!")

        self.set_combox_value(value=leavetype, keys=self.leave_type)
        Log.info("Leave Type is selected!")

        self.set_combox_value(value=datefrom, keys=self.time_duration)
        Log.info("From is selected!")

        self.set_combox_value(value=role, keys=self.job_title)
        Log.info("Job Title is selected!")

        self.set_combox_value(value=checkvalue, keys=self.location)
        Log.info("Location is selected!")

        self.set_combox_value(value=departname, keys=self.sub_unit)
        Log.info("Sub Unit is selected!")

        self.click(self.past_employee_include)
        Log.info("Include Past Employees is checked!")

        self.click(self.view_button)
        Log.info("View button is clicked")
        assert self.get_element(self.leave_type_table).is_displayed()

        Log.info("Query Leave Table show success!")