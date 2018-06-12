# -*- coding: utf-8 -*-
"""
Created by Linda
"""
from lib.log import Log
from pageobjects.leave.leave import Leave


class AssignLeave(Leave):
    """
    Assign leave page main components
    """
    assign_btn = ("id", "assignBtn")
    employee_name = ("id", "assignleave_txtEmployee_empName")
    leave_type = ("id", "assignleave_txtLeaveType")

    leave_balance = ("id", "assignleave_leaveBalance")
    view_detail = ("xpath", '//div[@id="assignleave_leaveBalance"]/a[@id="leaveBalance_details_link"]')

    employee_name_details = ('id', 'popup_emp_name')
    leave_type_details = ('id', 'popup_leave_type')
    as_of_date_details = ('id', 'balance_as_of')
    entitled_details = ('id', 'balance_entitled')
    taken_details = ('id', 'balance_taken')
    scheduled_details = ('id', 'balance_scheduled')
    pending_approval_details = ('id', 'balance_pending')
    balance_details = ('xpath', '//td[2]')
    details_OK_btn = ("xpath", '//div[@id="balance_details"]//input[@id="closeButton"]')

    from_date = ("id", "assignleave_txtFromDate")
    to_date = ("id", "assignleave_txtToDate")
    comment = ("id", "assignleave_txtComment")

    duration = ("id", "assignleave_duration_duration")
    half_day = ('id', 'assignleave_duration_ampm')
    time_from = ('id', 'assignleave_duration_time_from')
    time_to = ('id', 'assignleave_duration_time_to')
    time_duration = ('xpath', '//span[@id="assignleave_duration_specify_time_content"]//input')

    partial_days = ("id", "assignleave_partialDays")
    first_duration = ('id', 'assignleave_firstDuration_duration')
    first_half_day = ('id', 'assignleave_firstDuration_ampm')
    first_time_from = ('id', 'assignleave_firstDuration_time_from')
    first_time_to = ('id', 'assignleave_firstDuration_time_to')
    first_time_duration = ('xpath', '//span[@id="assignleave_firstDuration_specify_time_content"]//input')
    second_duration = ('id', 'assignleave_secondDuration_duration')
    second_half_day = ('id', 'assignleave_secondDuration_ampm')
    second_time_from = ('id', 'assignleave_secondDuration_time_from')
    second_time_to = ('id', 'assignleave_secondDuration_time_to')
    second_time_duration = ('xpath', '//span[@id="assignleave_secondDuration_specify_time_content"]//input')
    success_flag = ('class', 'message success fadable')
    details_windows = ('xpath', '//h3[text()="OrangeHRM - Leave Balance Details"]')
    ok_button = ("id", "confirmOkButton")

    def __init__(self, browser):
        super(AssignLeave, self).__init__(browser)
        self.click_menu("Assign Leave")
        Log.info("Arrive Assign Leave page")

    def select_menu(self):
        """
        Go to Assign Leave page
        """
        self.switch_main_menu("leave")
        self.click_menu("Assign Leave")
        Log.info("Arrive Assign Leave page")

    def select_name_and_type(self, leave_type, *args):
        """
        Select Employee Name and Leave Type
        """
        self.set_combox_value(leave_type, self.leave_type)
        args = "".join(args)
        if args != "":
            self.input_text(args, self.employee_name)
        self.press_enter_key(self.employee_name)

    def check_leave_balance(self):
        """
        Get the data of leave balance and return the data
        """
        self.sleep(2)
        leave_balance = self.get_element_text(self.leave_balance)
        return leave_balance

    def check_leave_balance_details(self):
        """
        Click 'view details' and then get the data of leave balance details and return the data
        """
        self.click(self.view_detail)
        while self.get_element_text(self.details_windows) is None:
            self.sleep(1)
            Log.info("Sleep 1 second")
            self.click(self.view_detail)
        employee_name = self.get_element_text(self.employee_name_details)
        leave_type = self.get_element_text(self.leave_type_details)
        balance_details = self.get_elements_texts(self.balance_details)
        actual_result = employee_name + leave_type + "".join(balance_details)
        self.click(self.details_OK_btn)
        return actual_result

    def input_date(self, from_date, to_date):
        """
        Input From Date, To Date
        """
        self.get_element(self.from_date)
        self.input_text(from_date, self.from_date)
        self.press_enter_key(self.from_date)
        self.input_text(to_date, self.to_date)
        self.press_enter_key(self.to_date)

    def input_comment(self, comment):
        """
        Input Comment
        """
        self.input_text(comment, self.comment)

    def input_duration(self, duration, half_day, time_from, time_to, time_duration):
        """
        Input duration
        """
        self.sleep(1)
        if duration == "Full Day":
            self.set_combox_value(duration, self.duration)
        elif duration == "Half Day":
            self.set_combox_value(duration, self.duration)
            self.set_combox_value(half_day, self.half_day)
        else:
            self.set_combox_value(duration, self.duration)
            self.set_combox_value(time_from, self.time_from)
            self.set_combox_value(time_to, self.time_to)
            actual_time_duration = self.get_element_attribute(self.time_duration, "value")
            assert time_duration == actual_time_duration
            Log.info("Time duration is % s" % actual_time_duration)

    def input_partial_day(self, partial_day, first_duration, first_half_day, first_time_from, first_time_to,
                          first_time_duration, second_duration, second_half_day, second_time_from,
                          second_time_to, second_time_duration):
        """
        Input partial day
        """
        self.sleep(1)
        if partial_day is None:
            self.set_combox_value(partial_day, self.partial_days)
        elif partial_day == "Start and End Day":
            self.set_combox_value(partial_day, self.partial_days)
            if first_duration == "Half Day":
                self.set_combox_value(first_duration, self.first_duration)
                self.set_combox_value(first_half_day, self.first_half_day)
            else:
                self.set_combox_value(first_duration, self.first_duration)
                self.set_combox_value(first_time_from, self.first_time_from)
                self.set_combox_value(first_time_to, self.first_time_to)
                actual_first_time_duration = self.get_element_attribute(self.first_time_duration, "value")
                assert first_time_duration == actual_first_time_duration
                Log.info("Time duration is % s" % actual_first_time_duration)
            if second_duration == "Half Day":
                self.set_combox_value(second_duration, self.second_duration)
                self.set_combox_value(second_half_day, self.second_half_day)
            else:
                self.set_combox_value(second_duration, self.second_duration)
                self.set_combox_value(second_time_from, self.second_time_from)
                self.set_combox_value(second_time_to, self.second_time_to)
                actual_second_time_duration = self.get_element_attribute(self.second_time_duration, "value")
                assert second_time_duration == actual_second_time_duration
                Log.info("Time duration is % s" % actual_second_time_duration)
        else:
            self.set_combox_value(partial_day, self.partial_days)
            if first_duration == "Half Day":
                self.set_combox_value(first_duration, self.first_duration)
                self.set_combox_value(first_half_day, self.first_half_day)
            else:
                self.set_combox_value(first_duration, self.first_duration)
                self.set_combox_value(first_time_from, self.first_time_from)
                self.set_combox_value(first_time_to, self.first_time_to)
                actual_first_time_duration = self.get_element_attribute(self.first_time_duration, "value")
                assert first_time_duration == actual_first_time_duration
                Log.info("Time duration is % s" % actual_first_time_duration)

    def assign(self):
        """
        Assign leave
        """
        self.click(self.assign_btn)
        self.click(self.ok_button)
        Log.info("Assign leave")

