# -*- coding: utf-8 -*-
import os
from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList


class ContactDetails(EmployeeList):
    """
    Edit contact details page elements
    """
    success_flag = ('xpath', "//h1[text()='Contact Details']")
    contact_details = ("xpath", "//*[@id='sidenav']/li[2]/a")
    btn_edit = ("id", "btnSave")
    contact_street1 = ("id", "contact_street1")
    contact_street2 = ("id", "contact_street2")
    contact_city = ("id", "contact_city")
    contact_province = ("id", "contact_province")
    contact_zipcode = ("id", "contact_emp_zipcode")
    contact_country = ("id", "contact_country")
    hm_telephone = ("id", "contact_emp_hm_telephone")
    contact_mobile = ("id", "contact_emp_mobile")
    work_telephone = ("id", "contact_emp_work_telephone")
    work_email = ("id", "contact_emp_work_email")
    oth_email = ("id", "contact_emp_oth_email")
    btn_save = ("id", "btnSave")
    message = ('XPATH', "//*[@class='message success fadable']")

    def __init__(self, browser):
        super(ContactDetails, self).__init__(browser)

    def open_contact_details_page_via_creation(self, first_name, last_name):
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Contact Details")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive contact details page")

    def open_contact_details_page_via_edition(self, first_name, last_name):
        self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Contact Details")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive contact details page")

    def click_edit_button(self):
        self.click(self.btn_edit)

    def edit_contact_street1(self, street1):
        self.click(self.contact_street1)
        self.input_text(street1, self.contact_street1)
        Log.info("Edit contact street1")

    def edit_contact_street2(self, street2):
        self.click(self.contact_street2)
        self.input_text(street2, self.contact_street2)
        Log.info("Edit contact street2")

    def edit_contact_city(self, city):
        self.click(self.contact_city)
        self.input_text(city, self.contact_city)
        Log.info("Edit contact city")

    def edit_contact_province(self, province):
        self.click(self.contact_province)
        self.input_text(province, self.contact_province)
        Log.info("Edit contact province")

    def edit_contact_zipcode(self, zipcode):
        self.click(self.contact_zipcode)
        self.input_text(zipcode, self.contact_zipcode)
        Log.info("Edit contact zipcode")

    def edit_contact_country(self, country):
        self.click(self.contact_country)
        self.input_text(country, self.contact_country)
        Log.info("Edit contact country")

    def edit_hm_telephone(self, hometel):
        self.click(self.hm_telephone)
        self.input_text(hometel, self.hm_telephone)
        Log.info("Edit contact home telephone")

    def edit_contact_mobile(self, mobile):
        self.click(self.contact_mobile)
        self.input_text(mobile, self.contact_mobile)
        Log.info("Edit contact mobile")

    def edit_work_telephone(self, worktel):
        self.click(self.work_telephone)
        self.input_text(worktel, self.work_telephone)
        Log.info("Edit work telephone")

    def edit_work_email(self, workemail):
        self.click(self.work_email)
        self.input_text(workemail, self.work_email)
        Log.info("Edit work email")

    def edit_other_email(self, othemail):
        self.click(self.oth_email)
        self.input_text(othemail, self.oth_email)
        Log.info("Edit other email")

    def click_save_button(self):
        self.click(self.btn_save)
        Log.info("Save the change")

    def assert_message(self, return_message):
        """
        Assert the result of current operation
        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)













