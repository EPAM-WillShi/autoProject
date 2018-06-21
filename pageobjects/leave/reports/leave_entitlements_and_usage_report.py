# -*- coding: utf-8 -*-

import random
from lib.log import Log
from pageobjects.leave.leave import Leave


class Report(Leave):
    """
    Report page elements
    """
    menu = ('id', 'menu_leave_viewLeaveBalanceReport')
    success_flag = ('xpath', '//h1[text()="Leave Entitlements and Usage Report"]')
    """
    Search elements
    """
    generate_for = ('id', 'leave_balance_report_type')
    leave_type = ('id', 'leave_balance_leave_type')
    leave_type_option = ('xpath', '//*[@id="leave_balance_leave_type"]/option')
    from_date = ('id', 'period')
    from_date_option = ('xpath', '//*[@id="period"]/option')
    job_title = ('id', 'leave_balance_job_title')
    job_title_option = ('xpath', '//*[@id="leave_balance_job_title"]/option')
    location = ('id', 'leave_balance_location')
    location_option = ('xpath', '//*[@id="leave_balance_location"]/option')
    sub_unit = ('id', 'leave_balance_sub_unit')
    sub_unit_option = ('xpath', '//*[@id="leave_balance_sub_unit"]/option')
    include_past_employees = ('id', 'leave_balance_include_terminated')
    employee = ('id', 'leave_balance_employee_empName')
    view_btn = ('id', 'viewBtn')
    """
    List elements
    """

    def __init__(self, browser):
        super(Report, self).__init__(browser)
        self.click_menu('Reports')
        self.wait_unit_el_present(self.menu)
        self.click(self.menu)
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Leave Entitlements and Usage Report page.")
        else:
            Log.info("Cannot arrive Leave Entitlements and Usage Report page.")

    def search_by_leave_type(self):
        self.set_combox_value('Leave Type', self.generate_for)
        self.wait_unit_el_present(self.leave_type)
        leave_type_value = self.get_random_data(self.leave_type_option)
        self.set_combox_value(leave_type_value, self.leave_type)
        from_date_value = self.get_random_data(self.from_date_option)
        self.set_combox_value(from_date_value, self.from_date)
        job_title_value = self.get_random_data(self.job_title_option)
        self.set_combox_value(job_title_value, self.job_title)
        location_value = self.get_random_data(self.location_option)
        self.set_combox_value(location_value, self.location)
        sub_unit_value = self.get_random_data(self.sub_unit_option)
        self.set_combox_value(sub_unit_value, self.sub_unit)
        past_employees = random.choice([0, 1])
        if past_employees == 1:
            self.click(self.include_past_employees)
        self.click(self.view_btn)

    def search_by_employee(self):
        self.set_combox_value('Employee', self.generate_for)
        self.wait_unit_el_present(self.employee)
        self.clear_text(self.employee)
        self.input_text('a', self.employee)
        try:
            self.press_enter_key(self.employee)
        except Exception:
            BaseException("Cannot find employee")
        from_date_value = self.get_random_data(self.from_date_option)
        self.set_combox_value(from_date_value, self.from_date)
        self.click(self.view_btn)


