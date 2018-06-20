# -*- coding: utf-8 -*-

from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList



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
    dep_delete_attachment_btn = ('id', 'btnDeleteAttachment')
    dep_save_CommentOnly_btn = ('id', 'btnCommentOnly')
    dep_the_first_dependents_checkbox = ('xpath', '//table[@id="dependent_list"]/tbody/tr[1]/td[1]/input')
    dep_the_first_dependents_name = ('xpath', '//table[@id="dependent_list"]/tbody/tr[1]/td[2]/a')
    dep_the_first_attachments_checkbox = ('xpath', '//table[@id="tblAttachments"]/tbody/tr[1]/td[1]/input')
    dep_the_first_attachments_name = ('xpath', '//table[@id="tblAttachments"]/tbody/tr[1]/td[2]/a')
    dep_the_first_attachments_edit = ('xpath', '//table[@id="tblAttachments"]/tbody/tr[1]/td[8]/a')
    the_first_record = '//table[@id="dependent_list"]/tbody/tr[1]'

    def __init__(self, browser):
        super(Dependents, self).__init__(browser)

    def open_dependents_page_via_creating_emp(self, first_name, last_name):
        """
        Go to Dependents via creating an employee
        """
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Dependents")
        page_ele = self.get_element(self.dep_success_flag)
        if page_ele is not None:
            Log.info("Arrive Dependents page via creating emp")
        else:
            Log.info("Cannot arrive Dependents page via creating emp")

    def open_dependents_page_via_editing_emp(self, first_name, last_name):
        """
        Go to Dependents via editing an employee
        """
        try:
            self.click_employee_to_edit(first_name, last_name)
        except:
            self.add_employee(first_name, last_name)
            self.click_menu("Employee List")
            self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Dependents")
        page_ele = self.get_element(self.dep_success_flag)
        if page_ele is not None:
            Log.info("Arrive Dependents page via editing emp")
        else:
            Log.info("Cannot arrive Dependents page via editing emp")

    def add_dependents_without_specify(self, name, relationship, date_of_birth):
        """
        Add a dependent with type child
        """
        self.click(self.dep_add_btn)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.set_combox_value(relationship, self.dep_relationship_drop)
        self.clear_text(self.dep_birth_date)
        self.input_text(date_of_birth, self.dep_birth_date)
        self.click(self.dep_save_btn)
        Log.info("The child type dependent record is added.")

    def check_dependents_list(self, name, relationship, date_of_birth):
        expected_text = name + " " + str.lower(relationship) + " " + date_of_birth
        actual_text = self.get_element_text(('xpath', self.the_first_record))
        if actual_text == expected_text:
            Log.info("The record is correct.")
        else:
            Log.info("The record is incorrect.")

    def add_dependents_with_specify(self, name, relationship, please_specify, date_of_birth):
        """
        Add a dependent with type other
        """
        self.click(self.dep_add_btn)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.set_combox_value(relationship, self.dep_relationship_drop)
        self.clear_text(self.dep_specify_txt)
        self.input_text(please_specify, self.dep_specify_txt)
        self.clear_text(self.dep_birth_date)
        self.input_text(date_of_birth, self.dep_birth_date)
        self.click(self.dep_save_btn)
        Log.info("The other type dependent record is added.")

    def edit_the_first_dependents_save(self, name):
        """
        Edit the first dependent and save
        """
        self.click(self.dep_the_first_dependents_name)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.click(self.dep_save_btn)
        Log.info("The dependent is edited.")

    def edit_the_first_dependents_cancel(self, name):
        """
        Edit the first dependent and cancel
        """
        self.click(self.dep_the_first_dependents_name)
        self.clear_text(self.dep_name_txt)
        self.input_text(name, self.dep_name_txt)
        self.click(self.dep_cancel_btn)
        Log.info("The dependent edit is canceled.")

    def delete_the_first_dependents(self):
        """
        Delete the first dependent
        """
        self.click(self.dep_the_first_dependents_checkbox)
        self.click(self.dep_delete_btn)
        Log.info("The dependent is deleted.")

    def add_attachments_upload(self, attachments, comment):
        """
        Add an attachment and save
        """
        self.click(self.dep_add_attachment_btn)
        self.upload_file(attachments, self.dep_select_file)
        self.input_text(comment, self.dep_attachment_comment)
        self.click(self.dep_upload_btn)
        Log.info("The attachment is added.")

    def add_attachments_cancel(self, attachments, comment):
        """
        Add an attachment and cancel
        """
        self.click(self.dep_add_attachment_btn)
        self.upload_file(attachments, self.dep_select_file)
        self.input_text(comment, self.dep_attachment_comment)
        self.click(self.dep_upload_cancel_btn)
        Log.info("The attachment is canceled.")

    def edit_the_first_attachments(self, attachments, comment):
        """
        Edit an attachment
        """
        self.click(self.dep_the_first_attachments_edit)
        self.upload_file(attachments, self.dep_select_file)
        self.clear_text(self.dep_attachment_comment)
        self.input_text(comment, self.dep_attachment_comment)
        self.click(self.dep_upload_btn)
        Log.info("The attachment is edited.")

    def delete_the_first_attachments(self):
        """
        Delete an attachment
        """
        self.click(self.dep_the_first_attachments_checkbox)
        self.click(self.dep_delete_attachment_btn)
        Log.info("The attachment is deleted.")