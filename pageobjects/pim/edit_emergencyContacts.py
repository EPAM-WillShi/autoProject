# -*- coding: utf-8 -*-

from pageobjects.pim.employee_list import EmployeeList
from lib.log import Log

class EditEmergencyContacts(EmployeeList):

    success_flag = ('xpath', '//h1[text()="Assigned Emergency Contacts"]')

    # add emergency contacts
    add_btn_emg = ('id', 'btnAddContact')
    emg_name = ('id', 'emgcontacts_name')
    emg_relationship = ('id', 'emgcontacts_relationship')
    emg_home_phone = ('id', 'emgcontacts_homePhone')
    emg_mobile = ('id', 'emgcontacts_mobilePhone')
    emg_work_phone = ('id', 'emgcontacts_workPhone')
    save_btn_emg = ('id', 'btnSaveEContact')
    message = ('xpath', "//*[contains(@class,'success')]")

    # add attachment
    add_btn_attach = ('id', 'btnAddAttachment')
    attach_ele = ('id', 'ufile')
    attach_commt = ('id', 'txtAttDesc')
    upload_btn = ('id', 'btnSaveAttachment')

    # edit emergency contacts
    edit_contacts = '//*[@id="emgcontact_list"]//tr[./td[2]/a[text()="{}"]]//td[2]'

    # delete emergency contacts
    delete_check = '//*[@id="emgcontact_list"]//tr[./td/a[text()="{}"]]//input'
    delete_btn = ('id', 'delContactsBtn')

    def __init__(self, browser):
        super(EditEmergencyContacts, self).__init__(browser)

    def open_emergency_page_via_creating_emp(self, first_name, last_name):
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Emergency Contacts")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Emergency Contacts page")

    def open_emergency_page_via_editing_emp(self, first_name, last_name):
        self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Emergency Contacts")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Emergency Contacts page")

    def add_emg_contacts(self, name, relationship, homephone, mobile, workphone):
        """
        Add emergency contact
        """
        self.click(self.add_btn_emg)
        self.input_text(name, self.emg_name)
        self.input_text(relationship, self.emg_relationship)
        self.input_text(homephone, self.emg_home_phone)
        self.input_text(mobile, self.emg_mobile)
        self.input_text(workphone, self.emg_work_phone)
        self.click(self.save_btn_emg)

    def add_attach(self, attachment, commt):
        """
        Add attachment
        """
        self.click(self.add_btn_attach)
        self.upload_file(attachment, self.attach_ele)
        self.input_text(commt, self.attach_commt)
        self.click(self.upload_btn)

    def assert_message(self, return_message):
        """
        Assert the result of current operation
        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)

    def edit_emg_contacts(self, name, upname, relationship, homephone):
        """
        Edit emergency contact
        """
        contact = self.edit_contacts.format(name)
        self.click(('xpath', contact))
        self.input_text(upname, self.emg_name)
        self.input_text(relationship, self.emg_relationship)
        self.input_text(homephone, self.emg_home_phone)
        self.click(self.save_btn_emg)

    def delete_emg_contacts(self, name):
        """
        Delete emergency contact
        """
        checkbox = self.delete_check.format(name)
        ielement = ('XPATH', checkbox)
        self.click(ielement)
        self.click(self.delete_btn)

































