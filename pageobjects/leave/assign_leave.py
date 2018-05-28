# -*- coding: utf-8 -*-
"""
Created by Tina Lu
"""
from lib.log import Log
from pageobjects.leave.leave import Leave
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.pim.add_employee import AddEmployee


class AssignLeave(Leave):
    """
    Assign leave page main components
    """
    employee_name = ("id", "assignleave_txtEmployee_empName")
    leave_type = ("id", "assignleave_txtLeaveType")
    leave_blance = ("id", "assignleave_leaveBalance")
    view_detail = ("id", "leaveBalance_details_link")
    from_date = ("id", "assignleave_txtFromDate")
    to_date = ("id", "assignleave_txtToDate")
    partial_days = ("id", "assignleave_partialDays")
    duration = ("id", "assignleave_duration_duration")
    first_duration = ("id", "assignleave_firstDuration_duration")
    time_from = ("id", "assignleave_firstDuration_time_from")
    time_to = ("id", "assignleave_firstDuration_time_to")
    comment = ("id", "assignleave_txtComment")
    assign_btn = ("id", "assignBtn")
    popup_employee_name = ("id", "popup_emp_name")
    popup_leave_type = ("id", "popup_leave_type")
    blance_day = ("id", "balance_as_of")
    scheduled_day = ("id", "balance_scheduled")
    balance_total = ("id", "balance_total")
    confirm_btn = ("id", "confirmOkButton")
    multiperiod_employee = ("id", "multiperiod_emp_name")
    multiperiod_type = ("id", "multiperiod_leave_type")

    view_detail_xpath = ("xpath","//a[@id='leaveBalance_details_link']")
    partial_days_xpath = ("xpath", "//select[@id='assignleave_partialDays']")
    confirm_title = ("xpath", "//h3[text()='OrangeHRM - Confirm Leave Assignment']")
    details_OK_btn = ("xpath", "//div[@id='balance_details']/div[3]/input[@id='closeButton']")
    multiperiod_OK_btn = ("xpath", "//div[@id='multiperiod_balance']/div[3]/input[@id='closeButton']")
    overlapping_title = ("xpath","//h1[text()='Overlapping Leave Request Found']")

    overlapping_table_xpath = "//div[@class='inner']/table/tbody/tr[1]"
    leave_date_xpath = "//div[@id='multiperiod_balance']/div[@class='modal-body']/table/tbody"

    def __init__(self, browser):
        super(AssignLeave, self).__init__(browser)

    def select_menu(self):
        """
        Go to Assign Leave page
        """
        self.switch_main_menu("leave")
        self.click_menu("Assign Leave")
        Log.info("Arrive Assign Leave page")

    def create_employee(self, first_name, last_name):
        """
        Go to PIM, create a new employee
        """
        self.addemployee = AddEmployee(self.driver)
        self.addemployee.add_user_employee(first_name, last_name)

    def delete_employee(self, first_name, last_name):
        """
        Go to PIM, delete an employee
        """
        self.employeelist = EmployeeList(self.driver)
        self.employeelist.delete_employee(first_name + " " + last_name)

    def select_name_type(self, name, leave_type):
        """
        Select Employee Name and Leave Type
        """
        self.clear_text(self.employee_name)
        self.input_text(name,self.employee_name)
        self.press_enter_key(self.employee_name)
        self.set_combox_value(leave_type, self.leave_type)
        self.wait_unit_el_present(self.view_detail_xpath)

    def input_samedate_duration_comment(self, date, duration, comment):
        """
        Input From Date, To Date, Duration and comment
        """
        self.clear_text(self.from_date)
        self.input_text(date, self.from_date)
        self.press_enter_key(self.from_date)
        self.clear_text(self.to_date)
        self.input_text(date, self.to_date)
        self.press_enter_key(self.to_date)
        self.set_combox_value(duration, self.duration)
        self.input_text(comment, self.comment)
        self.sleep(2)

    def input_multiperiod_partial(self, datefrom, dateto, partialdays):
        """
        Input From Date, To Date and partial days
        """
        self.clear_text(self.from_date)
        self.input_text(datefrom, self.from_date)
        self.press_enter_key(self.from_date)
        self.clear_text(self.to_date)
        self.input_text(dateto, self.to_date)
        self.press_enter_key(self.to_date)
        self.wait_unit_el_present(self.partial_days_xpath)
        self.set_combox_value(partialdays, self.partial_days)

    def input_duration_time_comment(self, duration, timefrom, timeto, comment):
        """
        Input duration, time and comment
        """
        self.set_combox_value(duration, self.first_duration)
        self.set_combox_value(timefrom, self.time_from)
        self.set_combox_value(timeto, self.time_to)
        self.input_text(comment, self.comment)
        self.sleep(2)

    def assign(self):
        """
        Assign and confirm if confirm dialog pops up
        """
        self.click(self.assign_btn)
        element = self.get_element(self.confirm_title)
        if element.is_displayed():
            self.click(self.confirm_btn)

        self.wait_unit_el_present(self.view_detail_xpath)
        Log.info("Assign new leave")

    def verify_balance_samedate(self, employee, leave_type, date):
        """
        Open view details and verify leave balance for same date set
        """
        self.click(self.view_detail)
        self.wait_unit_el_present(self.details_OK_btn)

        assert employee == self.get_element_text(self.popup_employee_name).encode("utf-8")
        assert leave_type == self.get_element_text(self.popup_leave_type).encode("utf-8")
        assert date == self.get_element_text(self.blance_day).encode("utf-8")
        assert "-1.00" == self.get_element_text(self.balance_total).encode("utf-8")
        assert self.get_element_text(self.leave_blance)[:5] == \
               self.get_element_text(self.balance_total).encode("utf-8")
        self.click(self.details_OK_btn)
        self.sleep(1)
        Log.info("Assign leave for same date successfully")

    def verify_balance_multiperiod(self, employee, leave_type, datefrom, dateto):
        """
        Open view details and verify leave balance for different date set
        """
        assert "Balance not sufficient" == self.get_element_text(self.view_detail)
        self.click(self.view_detail)
        self.wait_unit_el_present(self.multiperiod_OK_btn)

        assert employee == self.get_element_text(self.multiperiod_employee).encode("utf-8")
        assert leave_type == self.get_element_text(self.multiperiod_type).encode("utf-8")
        assert datefrom == self.get_element_text(("xpath", self.leave_date_xpath + "/tr[1]/td[3]")).encode("utf-8")
        assert dateto == self.get_element_text(("xpath", self.leave_date_xpath + "/tr[2]/td[3]")).encode("utf-8")
        assert "-3.00" == self.get_element_text(self.leave_blance)[:5]
        assert self.get_element_text(self.leave_blance)[:5] == \
               self.get_element_text(("xpath", self.leave_date_xpath + "/tr[1]/td[2]")).encode("utf-8")
        self.sleep(1)
        self.click(self.multiperiod_OK_btn)
        Log.info("Assign leave for different date successfully")

    def check_overlapping(self, date, leave_type):
        """
        Verify overlapping
        """
        assert self.get_element(self.overlapping_title).is_displayed()
        assert "-1.00" == self.get_element_text(self.leave_blance)[:5]
        assert date == self.get_element_text(("xpath", self.overlapping_table_xpath+ "/td[1]")).encode("utf-8")
        assert leave_type == self.get_element_text(("xpath",
                                                    self.overlapping_table_xpath + "/td[3]")).encode("utf-8")
        Log.info("Overlapping is correct")
