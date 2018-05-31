# -*- coding: utf-8 -*-

from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList
from selenium.webdriver.support.ui import Select


class Dependents(EmployeeList):
    """
    Employee list - Assigned Dependents page elements
    """
    dep_success_flag = ('xpath', '//h1[text()="Assigned Dependents"]')
    dep_add_btn = ('id', 'btnAddDependent')
    dep_delete_btn = ('id', 'delDependentBtn')
    dep_save_btn = ('id', 'btnSaveDependent')
    dep_cancel_btn = ('id', 'btnCancel')
    dep_name_txt = ('id', 'dependent_name')
    dep_relationship_drop = ('id', 'dependent_relationshipType')
    dep_specify_txt = ('id', 'dependent_relationship')
    dep_birth_date = ('id', 'dependent_dateOfBirth')
    dep_add_attachment_btn = ('id', 'btnAddAttachment')
    dep_select_file = ('id', 'ufile')
    dep_attachment_comment = ('id', 'txtAttDesc')
    dep_upload_btn = ('id', 'btnSaveAttachment')
    dep_upload_cancel_btn = ('id', 'cancelButton')
    dep_the_first_dependents_checkbox = ('xpath', '//tr[1]/td[1]/input')
    dep_the_first_dependents_name = ('xpath', '//tr[1]/td[2]/a')

    def __init__(self, browser):
        super(Dependents, self).__init__(browser)

    def open_dependents_page_via_creating_emp(self, first_name, last_name):
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Dependents")
        page_ele = self.get_element(self.dep_success_flag)
        if page_ele is not None:
            Log.info("Arrive Dependents_page")

    def open_dependents_page_via_editing_emp(self, first_name, last_name):
        self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Dependents")
        page_ele = self.get_element(self.dep_success_flag)
        if page_ele is not None:
            Log.info("Arrive Dependents_page")

    def add_dependents_without_specify(self, name, relationship, date_of_birth):
        self.click(self.dep_add_btn)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.set_combox_value(relationship, self.dep_relationship_drop)
        self.clear_text(self.dep_birth_date)
        self.input_text(date_of_birth, self.dep_birth_date)
        self.click(self.dep_save_btn)

    def add_dependents_with_specify(self, name, relationship, please_specify, date_of_birth):
        self.click(self.dep_add_btn)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.set_combox_value(relationship, self.dep_relationship_drop)
        self.clear_text(self.dep_specify_txt)
        self.input_text(please_specify, self.dep_specify_txt)
        self.clear_text(self.dep_birth_date)
        self.input_text(date_of_birth, self.dep_birth_date)
        self.click(self.dep_save_btn)

    def edit_the_first_dependents_save(self, name):
        self.click(self.dep_the_first_dependents_name)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.click(self.dep_save_btn)

    def edit_the_first_dependents_cancle(self, name):
        self.click(self.dep_the_first_dependents_name)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.click(self.dep_cancel_btn)

    def delete_the_first_dependents(self):
        self.click(self.dep_the_first_dependents_checkbox)
        self.click(self.dep_delete_btn)