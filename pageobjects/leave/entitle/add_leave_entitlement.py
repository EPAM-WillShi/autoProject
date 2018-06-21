# -*- coding: utf-8 -*-
"""
Created on 2018/6/10
@author: Dora Zhu
"""
from decimal import *
from lib.log import Log
from pageobjects.leave.leave import Leave


class AddLeaveEntitlement(Leave):
    """
    Add Leave Entitlement page functions
    """
    chek_box = ('ID', 'entitlements_filters_bulk_assign')
    emp = ('ID', 'entitlements_employee_empName')
    leave_type = ('ID', 'entitlements_leave_type')
    leave_period = ('ID', 'period')
    entitle = ('ID', 'entitlements_entitlement')
    save_btn = ('ID', 'btnSave')
    message = ('XPATH', "//*[@class='message success fadable']")

    valid_from = ('XPATH', '//td[3]/a')
    valid_to = ('XPATH', '//td[4]/a')
    days = ('XPATH', '//td[5]/a')

    flag = ('XPATH', '//h3[text()="OrangeHRM - Matching Employees"]')
    list_name = '//td[1][normalize-space(text())= "{}"]'
    old_entitlement = '//td[1][normalize-space(text())= "{}"]/../td[2]'
    new_entitlement = '//td[1][normalize-space(text())= "{}"]/../td[3]'
    # old_entitlement = '//td[1][text()= "{}"]/../td[2]'
    # new_entitlement = '//td[1][text()= "{}"]/../td[3]'

    confirm_btn = ('ID', 'dialogConfirmBtn')

    def __init__(self, browser):
        super(AddLeaveEntitlement, self).__init__(browser)
        self.click_menu("Entitlements")
        self.click_menu("Add Entitlements")
        Log.info("Arrive Leave Add Entitlements page")

    def add_entitlement_for_individual(self, first_name, last_name, leave_type, leave_period, entitlement1):
        """
        Add entitlement for the created employee

        """
        emp_name = first_name + " " + last_name
        self.sleep(2)
        self.input_text(emp_name, self.emp)
        self.sleep(2)
        self.press_enter_key(self.emp)
        self.set_combox_value(leave_type, self.leave_type)
        self.set_combox_value(leave_period, self.leave_period)
        self.input_text(entitlement1, self.entitle)
        self.click(self.save_btn)
        pos = leave_period.find(" "+"-"+ " ")
        leave_from = leave_period[0:pos]
        assert self.get_element_text(self.valid_from) == leave_from
        leave_to = leave_period[pos+3:]
        assert self.get_element_text(self.valid_to) == leave_to
        assert Decimal(self.get_element_text(self.days)) == Decimal(entitlement1)

    def assert_message(self, return_message):
        """
        Assert the result of current operation

        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)

    def add_entitlement_for_multiple_employees(self, first_name, last_name, leave_type, leave_period,
                                               entitlement1, entitlement2):
        """
        Add entitlement for multiple employees

        """
        self.click(self.chek_box)
        self.set_combox_value(leave_type, self.leave_type)
        self.set_combox_value(leave_period, self.leave_period)
        self.input_text(entitlement2, self.entitle)
        self.click(self.save_btn)
        emp_name = first_name + " " + last_name
        self.wait_unit_el_present(('XPATH', self.list_name.format(emp_name)))
        assert Decimal(self.get_element_text(('XPATH', self.old_entitlement.format(emp_name)))) == Decimal(entitlement1)
        all_entitlement = Decimal(entitlement1) + Decimal(entitlement2)
        assert Decimal(self.get_element_text(('XPATH', self.new_entitlement.format(emp_name)))) == all_entitlement
        self.click(self.confirm_btn)






