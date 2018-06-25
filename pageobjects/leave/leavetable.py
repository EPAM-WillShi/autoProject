# -*- coding: utf-8 -*-
"""
Created on 2018/4/17
@author: Molly Xue
"""

from lib.log import Log
from pageobjects.leave.leave import Leave
from pageobjects.leave.configure.leave_period import LeavePeriod

class LeaveTable(Leave):
    """
    Leave-Configure-Leave Period page main components
    """
    #Leave Page components
    leave_entitlement_menu = ('id', 'menu_leave_viewLeaveBalanceReport')
    reports_menu = ('id', 'menu_leave_Reports')
    generate_for = ('id', 'leave_balance_report_type')
    leave_type = ('id', 'leave_balance_leave_type')
    time_duration = ('id', 'period')
    job_title = ('id', 'leave_balance_job_title')
    location = ('id', 'leave_balance_location')
    sub_unit = ('id', 'leave_balance_sub_unit')
    past_employee_include = ('id', 'leave_balance_include_terminated')
    view_button = ('id', 'viewBtn')
    table_title_element = "//*[@class= 'header']/../../tr[2]"
    table_element = "//*[@id='report-results']/div/table/tbody"
    table_link = ".//*[@id='report-results']/div/table/tbody/tr[1]"

    #Leave Entitlements components
    entitlements_employee = ('id', 'entitlements_employee_empName')
    entitlements_leavetype = ('id', 'entitlements_leave_type')
    entitlements_leaveperiod = ('id', 'period')

    #Leave List components
    list_from = ('id', 'calFromDate')
    list_to = ('id', 'calToDate')
    list_pendingapproval = ('id', 'leaveList_chkSearchFilter_1')
    list_scheduled = ('id', 'leaveList_chkSearchFilter_2')
    list_taken = ('id', 'leaveList_chkSearchFilter_3')
    list_employee = ('id', 'leaveList_txtEmployee_empName')


    def __init__(self, browser):
        super(LeaveTable, self).__init__(browser)

    def select_menu(self):
        """
        Go to Leave Entitlements and Usage Report page
        """
        self.driver.implicitly_wait(5)
        self.click_menu("Reports")
        self.driver.implicitly_wait(5)
        self.click_menu("Leave Entitlements and Usage Report")
        self.driver.implicitly_wait(5)
        Log.info("Arrive Leave Entitlements and Usage Report page")

    def set_leaveperiod(self, startmonth, startdate):
        self.leaveperiod = LeavePeriod(self.driver)
        self.leaveperiod.edit_LeavePeriod()
        self.leaveperiod.select_StartMonth(startmonth)
        self.leaveperiod.select_StartDate(startdate)
        self.leaveperiod.save_LeavePeriod()

    def query_LeaveTypeTable(self,leavetype,datefrom):
        """
        Query out Leave Types table
        """
        self.driver.implicitly_wait(2)
        self.set_combox_value(value="Leave Type", keys=self.generate_for)
        self.wait_unit_el_present(self.view_button)
        self.set_combox_value(value=leavetype, keys=self.leave_type)
        self.set_combox_value(value=datefrom, keys=self.time_duration)
        self.set_combox_value(value="All", keys=self.job_title)
        self.set_combox_value(value="All", keys=self.location)
        self.set_combox_value(value="All", keys=self.sub_unit)
        self.click(self.past_employee_include)
        self.driver.implicitly_wait(2)
        self.click(self.view_button)
        self.driver.implicitly_wait(2)
        assert self.get_element(('xpath', self.table_title_element)).is_displayed()
        Log.info("Query Leave Table show success!")

    def check_LeaveEntitlementsLink(self, optionvalue_leavetype, optionvalue_leaveperiod):
        """
        Test link in Leave Entitlements(Days)-click link
        """
        #Get employee name from query out table
        queryout_employee = self.get_element_text(("xpath", self.table_element + "/tr[1]/td[1]"))
        #Click Leave Entitlements(Days) link in query out table and switch to Leave Entitlements page
        self.click(("xpath", self.table_link + "/td[2]/a"))
        self.driver.implicitly_wait(2)
        self.wait_unit_el_present(self.entitlements_employee)
        displayname = self.get_element_attribute(self.entitlements_employee, "value")
        #Test link in Leave Entitlements(Days)-assert display name
        assert queryout_employee == displayname
        self.driver.implicitly_wait(2)
        displayleavetype_value = self.get_element_attribute(self.entitlements_leavetype, "value")
        #Test link in Leave Entitlements(Days)-assert display leave type
        assert displayleavetype_value == optionvalue_leavetype
        self.driver.implicitly_wait(2)
        displayleaveperiod_value = self.get_element_attribute(self.entitlements_leaveperiod, "value")
        # Test link in Leave Entitlements(Days)-assert display leave period
        assert displayleaveperiod_value == optionvalue_leaveperiod
        #Switch back to leave query out table
        self.back_browser()
        Log.info("Test link in Leave Entitlements(Days) - passed")

    def check_LeaveList_PendingApprovalLink(self, datefrom):
        """
        Test link in Leave Pending Approval(Days)-click link
        """
        # Get employee name from query out table
        queryout_employee = self.get_element_text(("xpath", self.table_element + "/tr[1]/td[1]"))
        # Click Leave Pending Approval(Days) Link and switch to Leave List Page
        self.driver.implicitly_wait(2)
        self.click(("xpath", self.table_link + "/td[3]/a"))
        self.driver.implicitly_wait(2)
        self.wait_unit_el_present(self.list_employee)
        displaylist_employee = self.get_element_attribute(self.list_employee, "value")
        #Test link in Leave Pending Approval(Days)-assert display name
        assert displaylist_employee == queryout_employee
        self.driver.implicitly_wait(2)
        displaylist_from = self.get_element_attribute(self.list_from, "value")
        #Test link in Leave Pending Approval(Days)-assert leave list from
        assert displaylist_from in datefrom
        self.driver.implicitly_wait(2)
        displaylist_to = self.get_element_attribute(self.list_to, "value")
        #Test link in Leave Pending Approval(Days)-assert leave list to
        assert displaylist_to in datefrom
        self.driver.implicitly_wait(2)
        displaylist_pendingapproval = self.get_element_attribute(self.list_pendingapproval, "checked")
        #Test link in Leave Pending Approval(Days)-assert pending approval checked
        assert displaylist_pendingapproval == 'true'
        self.back_browser()
        Log.info("Test link in Leave Pending Approval(Days) - passed")

    def check_LeaveList_ScheduledLink(self, datefrom):
        """
        Test link in Leave Scheduled(Days)-click link
        """
        queryout_employee = self.get_element_text(("xpath", self.table_element + "/tr[1]/td[1]"))
        self.driver.implicitly_wait(2)
        self.click(("xpath", self.table_link + "/td[4]/a"))
        self.driver.implicitly_wait(2)
        self.wait_unit_el_present(self.list_employee)
        displaylist_employee = self.get_element_attribute(self.list_employee, "value")
        #Test link in Leave Scheduled(Days)-assert display name
        assert displaylist_employee == queryout_employee
        self.driver.implicitly_wait(2)
        displaylist_from = self.get_element_attribute(self.list_from, "value")
        # Test link in Leave Scheduled(Days)-assert leave list from
        assert displaylist_from in datefrom
        self.driver.implicitly_wait(2)
        displaylist_to = self.get_element_attribute(self.list_to, "value")
        # Test link in Leave Scheduled(Days)-assert leave list to
        assert displaylist_to in datefrom
        self.driver.implicitly_wait(2)
        displaylist_scheduled = self.get_element_attribute(self.list_scheduled, "checked")
        # Test link in Leave Scheduled(Days)-assert scheduled checked
        assert displaylist_scheduled == 'true'
        self.back_browser()
        Log.info("Test link in Leave Scheduled(Days) - passed")

    def check_leaveList_TakenLink(self, datefrom):
        """
        Test link in Leave Taken(Days)-click link
        """
        queryout_employee = self.get_element_text(("xpath", self.table_element + "/tr[1]/td[1]"))
        self.driver.implicitly_wait(2)
        self.click(("xpath", self.table_link + "/td[5]/a"))
        self.driver.implicitly_wait(2)
        self.wait_unit_el_present(self.list_employee)
        displaylist_employee = self.get_element_attribute(self.list_employee, "value")
        # Test link in Leave Taken(Days)-assert display name
        assert displaylist_employee == queryout_employee
        self.driver.implicitly_wait(2)
        displaylist_from = self.get_element_attribute(self.list_from, "value")
        # Test link in Leave Taken(Days)-assert leave list from
        assert displaylist_from in datefrom
        self.driver.implicitly_wait(2)
        displaylist_to = self.get_element_attribute(self.list_to, "value")
        # Test link in Leave Taken(Days)-assert leave list to
        assert displaylist_to in datefrom
        self.driver.implicitly_wait(2)
        displaylist_taken = self.get_element_attribute(self.list_taken, "checked")
        # Test link in Leave Taken(Days)-assert scheduled checked
        assert displaylist_taken == 'true'
        self.back_browser()
        Log.info("Test link in Leave Taken(Days) - passed")