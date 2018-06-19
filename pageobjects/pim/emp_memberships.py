# -*- coding: utf-8 -*-

from lib.log import Log
from decimal import *
from pageobjects.pim.employee_list import EmployeeList


class Memberships(EmployeeList):
    """
    Employee list - Job
    """
    mem_flag = ('XPATH', '//h1[text()="Assigned Memberships"]')
    add_btn = ('ID', 'btnAddMembershipDetail')
    add_mem_flag = ('ID', 'membershipHeading')
    assigned_flag = ('XPATH', '//h1[contains(text(), "Memberships")]')

    mem_ship = ('ID', 'membership_membership')
    sub_paid_by = ('ID', 'membership_subscriptionPaidBy')
    sub_amount = ('ID','membership_subscriptionAmount')
    currency = ('ID', 'membership_currency')
    sub_com_date = ('ID', 'membership_subscriptionCommenceDate')
    sub_renew_date = ('ID', 'membership_subscriptionRenewalDate')
    save_btn = ('ID', 'btnSaveMembership')
    message = ('XPATH', '//*[@class="message success fadable"]')

    chart_mem_ship = '//td[2]/a[contains(text(),"{}")]'
    subscription_paid_by = '//td[2]/a[contains(text(),"{}")]/../../td[3]'
    subscription_amount = '//td[2]/a[contains(text(),"{}")]/../../td[4]'
    subscription_currency = '//td[2]/a[contains(text(),"{}")]/../../td[5]'
    subscription_commence_date = '//td[2]/a[contains(text(),"{}")]/../../td[6]'
    subscription_renew_data = '//td[2]/a[contains(text(),"{}")]/../../td[7]'
    chk_box = '//td[2]/a[contains(text(),"{}")]/../../td[1]//input'
    del_btn = ('ID', 'delMemsBtn')

    add_attach_btn = ('ID', 'btnAddAttachment')
    browser_btn = ('ID', 'ufile')
    comment = ('ID', 'txtAttDesc')
    upload_btn = ('ID', 'btnSaveAttachment')
    cancel_attach_btn = ('ID', 'cancelButton')
    attach_names = ('XPATH', '//*[@id="tblAttachments"]//td[2]')
    attach_des = '//*[@id="tblAttachments"]//td[2]/a[normalize-space(text())= "{}"]/../../td[3]'
    del_attach_btn = ('ID', 'btnDeleteAttachment')
    attach_checkbox = '//*[@id="tblAttachments"]//td[2]/a[normalize-space(text())= "{}"]/../..//input'

    def __int__(self, browser):
        super(Memberships, self).__int__(browser)
        self.switch_main_menu("PIM")
        self.click_menu("Employee List")
        Log.info("Arrive Employee List page")

    def open_memberships_page_via_creating_emp(self, first_name, last_name):
        """
        Open Membership page under Employee List by creating a new employee
        """
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Memberships")
        page_ele = self.get_element(self.mem_flag)
        if page_ele is not None:
            Log.info("Arrive Membership_page")

    def add_membership(self, membership, pay, amount, currency, com_date, renew_date, abb_currency):
        """
        Add membership
        """
        self.click(self.add_btn)
        assert self.get_element(self.add_mem_flag).is_displayed()
        # assert "Add Membership" == self.get_element_text(self.add_mem_flag).encode("utf-8")
        self.set_combox_value(membership, self.mem_ship)
        self.set_combox_value(pay, self.sub_paid_by)
        self.input_text(amount, self.sub_amount)
        self.set_combox_value(currency, self.currency)
        self.input_text(com_date, self.sub_com_date)
        self.input_text(renew_date, self.sub_renew_date)
        self.click(self.save_btn)
        assert self.get_element_text(self.assigned_flag).encode("utf-8") == "Assigned Memberships"
        assert self.get_element(("XPATH", self.chart_mem_ship.format(membership))).is_displayed()
        assert self.get_element_text(("XPATH", self.subscription_paid_by.format(membership))) == pay
        sub_amount = self.get_element_text(("XPATH", self.subscription_amount.format(membership))).encode("utf-8").replace(",", "")
        assert Decimal(sub_amount) == Decimal(amount)
        assert self.get_element_text(("XPATH", self.subscription_currency.format(membership))) == abb_currency
        assert self.get_element_text(("XPATH", self.subscription_commence_date.format(membership))) == com_date
        assert self.get_element_text(("XPATH", self.subscription_renew_data.format(membership))) == renew_date

    def edit_membership(self, membership, modified_pay, modified_amount):
        """
        Edit membership
        """
        chat_mem = ('LINK_TEXT', membership)
        self.click(chat_mem)
        assert self.get_element_text(self.add_mem_flag).encode("utf-8") == "Edit Membership"
        self.set_combox_value(modified_pay, self.sub_paid_by)
        self.input_text(modified_amount, self.sub_amount)
        self.click(self.save_btn)
        assert self.get_element_text(("XPATH", self.subscription_paid_by.format(membership))) == modified_pay
        sub_amount = self.get_element_text(("XPATH", self.subscription_amount.format(membership))).encode("utf-8").replace(",", "")
        assert Decimal(sub_amount) == Decimal(modified_amount)

    def delete_membership(self, membership):
        """
        Delete membership
        """
        checkbox = ("XPATH", self.chk_box.format(membership))
        self.click(checkbox)
        self.click(self.del_btn)

    def verify_membership_success(self, return_message):
        """
        Assert the result of current operation

        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)

    def cancel_adding_attachment(self, filename, description):
        """
        Cancel adding an attachment
        """
        self.click(self.add_attach_btn)
        self.upload_file(filename, self.browser_btn)
        self.input_text(description, self.comment)
        self.click(self.cancel_attach_btn)
        assert self.get_element(('LINK_TEXT', filename)) is None
        Log.info("Cancelling to attach a file")

    def add_attachment(self, filename, description):
        """
        add attachment
        """
        self.click(self.add_attach_btn)
        self.upload_file(filename, self.browser_btn)
        self.input_text(description, self.comment)
        self.click(self.upload_btn)
        attachment_description = self.attach_des.format(filename)
        assert filename in self.get_elements_texts(self.attach_names)
        assert self.get_element_text(('XPATH', attachment_description)).encode("utf-8") == description

    def delete_attachment(self,filename):
        """
        delete_attachment
        """
        checkbox =('XPATH', self.attach_checkbox.format(filename))
        self.click(checkbox)
        self.click(self.del_attach_btn)










