# -*- coding: utf-8 -*-
"""
Created by Linda
"""
from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList


class Immigration(EmployeeList):
    """
    Employee list page elements
    """
    success_flag = ('xpath', '//h1[text()="Assigned Immigration Records"]')
    add_btn = ('id', 'btnAdd')
    delete_btn = ('id', 'btnDelete')
    save_btn = ('id', 'btnSave')
    cancel_btn = ('id', 'btnCancel')
    document_radio = '//label[text()="{}"]'
    immigration_number = ('id', 'immigration_number')
    issued_date_ele = ('id', 'immigration_passport_issue_date')
    expired_date_ele = ('id', 'immigration_passport_expire_date')
    eligible_status_ele = ('id', 'immigration_i9_status')
    issued_by_ele = ('id', 'immigration_country')
    eligible_review_date_ele = ('id', 'immigration_i9_review_date')
    comments_ele = ('id', 'immigration_comments')
    add_attachment_btn = ('id', 'btnAddAttachment')
    delete_attachment_btn = ('id', 'btnDeleteAttachment')
    check_one_attachment_ele = '//table[@id="tblAttachments"]//tr[./td[2]/a[normalize-space(text())="{}"]]//input'
    upload_attachment = ('id', 'ufile')
    attachment_comment = ('id', 'txtAttDesc')
    upload_btn = ('id', 'btnSaveAttachment')
    check_all_ele = ('id', 'immigrationCheckAll')
    check_all_values = '//div[@id="immidrationList"]//tr[./td[3][text()="{}"]]'
    edit_attachment_btn = ('XPATH', '//tr[1]/td[8]/a')
    save_comment_only_btn = ('ID', 'btnCommentOnly')
    check_one_ele = '//div[@id="immidrationList"]//tr[./td[2]/a[text()="{}"]]//td[1]'
    immigration_row_ele = '//div[@id="immidrationList"]//tr[./td[2]/a[text()="{}"]]'
    attachment_ele = '//table[@id="tblAttachments"]//td[2]/a[normalize-space(text())="{}"]'
    comment_ele = '//table[@id="tblAttachments"]//td[3][normalize-space(text())="{}"]'
    check_all_attachments = ('id', 'attachmentsCheckAll')
    cancel_attachment_btn = ('id', 'cancelButton')
    document_data = ('xpath', '//ul[@class="radio_list"]//label')
    issued_by_data = ('xpath', '//select[@id="immigration_country"]/option')
    person_page_ele = ('xpath', '//h1[text()="Personal Details"]')
    select_ele = ('xpath', '//td[2]/a')
    click_selected_ele = '//td[2]/a[text()="{}"]'
    random_record_ele = ('xpath', '//form[@id="frmImmigrationDelete"]//td[2]')

    def __init__(self, browser):
        super(Immigration, self).__init__(browser)

    def open_immigration_page_via_creating_emp(self, first_name, last_name):
        """
        Go to Immigration page via creating an employee
        """
        try:
            self.add_employee(first_name, last_name)
        except Exception, e:
            Log.error(e)
        self.switch_employee_detail_page("Immigration")
        page_ele = self.get_element(self.success_flag)
        assert page_ele is not None
        Log.info("Arrive Immigration page via creating emp")

    def open_immigration_page_via_editing_emp(self):
        """
        Go to Immigration page via editing an employee
        """
        try:
            select_data = self.get_random_data(self.select_ele)
            click_ele = self.click_selected_ele.format(select_data)
            self.click(('xpath', click_ele))
            assert self.get_element(self.person_page_ele) is not None
            Log.info("Arrive Personal Details page of id: %s" % select_data)
        except Exception, e:
            Log.error(e)
        self.switch_employee_detail_page("Immigration")
        page_ele = self.get_element(self.success_flag)
        assert page_ele is not None
        Log.info("Arrive Immigration page via editing emp")

    def input_immigration_details(self, document, number, **kwargs):
        """
        Input the immigration details
        """
        document = document.title()
        document_ele = self.document_radio.format(document)
        self.click(('xpath', document_ele))
        self.input_text(number, self.immigration_number)
        for k, v in kwargs.items():
            if k == "issued_date":
                self.input_text(kwargs[k], self.issued_date_ele)
                self.press_enter_key(self.issued_date_ele)
            if k == "expiry_date":
                self.input_text(kwargs[k], self.expired_date_ele)
                self.press_enter_key(self.expired_date_ele)
            if k == "eligible_status":
                self.input_text(kwargs[k], self.eligible_status_ele)
            if k == "issued_by":
                self.set_combox_value(kwargs[k], self.issued_by_ele)
            if k == "eligible_review_date":
                self.input_text(kwargs[k], self.eligible_review_date_ele)
                self.press_enter_key(self.eligible_review_date_ele)
            if k == "comments":
                self.input_text(kwargs[k], self.comments_ele)

    def cancel_immigration(self):
        """
        Cancel the operation
        """
        self.click(self.cancel_btn)
        Log.info("Cancel the operation.")

    def save_immigration(self):
        """
        Save the operation
        """
        self.click(self.save_btn)
        Log.info("The immigration record is saved.")

    def check_immigration_details(self, document, number, **kwargs):
        """
        Check the immigration details
        """
        check_details = self.check_all_values.format(number)
        actual_result = self.get_element_text(('xpath', check_details))
        if kwargs != {}:
            kwargs.update({"document": document, "number": number})
            expected_result = sorted(kwargs.items())
            actual_value = actual_result.split()
            actual_key = ["document", "number", "issued_by", "issued_date", "expiry_date"]
            actual_dict = dict(zip(actual_key, actual_value))
            actual_result = sorted(actual_dict.items())
        else:
            expected_result = document + " " + number
        try:
            assert actual_result == expected_result
            Log.info("The immigration record is correct.")
        except Exception, e:
            Log.info("The actual result: % s and the expected result: % s" % (actual_result, expected_result))
            Log.error(e)

    def check_immigration_exist(self, document):
        """
        Check if the immigration exists
        """
        immigration_row = self.immigration_row_ele.format(document)
        if self.get_element(('xpath', immigration_row)) is not None:
            Log.info("The immigration record exists.")
            return True
        else:
            Log.info("The immigration record doesn't exist.")
            return False

    def delete_immigration(self):
        """
        Delete an immigration record
        """
        old_record = self.get_random_data(self.random_record_ele)
        check_immigration = self.check_one_ele.format(old_record)
        self.click(('xpath', check_immigration))
        self.click(self.delete_btn)
        Log.info("The immigration record is deleted.")
        return old_record

    def delete_all_immigration(self):
        """
        Delete all immigration records
        """
        self.click(self.check_all_ele)
        self.click(self.delete_btn)

    def delete_attachment(self, attachment):
        """
        Delete an attachment
        """
        check_one_attachment = self.check_one_attachment_ele.format(attachment)
        self.click(('xpath', check_one_attachment))
        self.click(self.delete_attachment_btn)
        Log.info("The attachment is deleted.")

    def delete_all_attachments(self):
        """
        Delete all attachments
        """
        self.click(self.check_all_attachments)
        self.click(self.delete_attachment_btn)

    def input_attachment_details(self, attachment, comment):
        """
        Input attachment details
        """
        self.upload_file(attachment, self.upload_attachment)
        self.input_text(comment, self.attachment_comment)

    def add_attachment(self, attachment, comment):
        """
        Add an attachment
        """
        self.click(self.add_attachment_btn)
        self.input_attachment_details(attachment, comment)
        self.click(self.upload_btn)
        Log.info("The attachment is added.")

    def cancel_add_attachment(self, attachment, comment):
        """
        Cancel the attachment creation
        """
        self.click(self.add_attachment_btn)
        self.input_attachment_details(attachment, comment)
        self.click(self.cancel_attachment_btn)
        Log.info("Cancel the attachment creation.")

    def edit_attachment_comment_only(self, attachment, comment):
        """
        Edit the attachment - save comment only
        """
        self.click(self.edit_attachment_btn)
        self.input_attachment_details(attachment, comment)
        self.click(self.save_comment_only_btn)
        Log.info("The comment of the attachment is edited.")

    def edit_attachment(self, attachment, comment):
        """
        Edit the attachment
        """
        self.click(self.edit_attachment_btn)
        self.input_attachment_details(attachment, comment)
        self.click(self.upload_btn)
        Log.info("The attachment is edited.")

    def cancel_edit_attachment(self, attachment, comment):
        """
        Cancel the attachment editing
        """
        self.click(self.edit_attachment_btn)
        self.input_attachment_details(attachment, comment)
        self.click(self.cancel_attachment_btn)
        Log.info("Cancel the attachment editing.")

    def check_attachment(self, attachment, comment):
        """
        Check the attachment details
        """
        check_attachment = self.attachment_ele.format(attachment)
        check_comment = self.comment_ele.format(comment)
        assert self.get_element_text(('xpath', check_attachment)) == attachment
        assert self.get_element_text(('xpath', check_comment)) == comment
        Log.info("The attachment is correct.")

    def check_attachment_exists(self, attachment):
        """
        Check if the attachment exists
        """
        check_attachment = self.attachment_ele.format(attachment)
        get_attachment = self.get_element(('xpath', check_attachment))
        if get_attachment is not None:
            Log.info("The attachment exists.")
            return True
        else:
            Log.info("The attachment doesn't exist.")
            return False

    def click_add_btn(self):
        """
        Click Add button to add immigration page
        """
        self.click(self.add_btn)

    def click_existing_record(self):
        """
        Click an existing immigration record
        """
        existing_document = self.get_random_data(self.random_record_ele)
        immigration_row = self.immigration_row_ele.format(existing_document)
        record = self.get_element_text(('xpath', immigration_row))
        issued_by = record.split(" ")[2]
        self.click(('link_text', existing_document))
        return existing_document, issued_by

    def get_document_data(self):
        """
        Get random 'document' data
        """
        document_data = self.get_random_data(self.document_data)
        return document_data

    def get_issued_by_data(self):
        """
        Get random 'issued by' data
        """
        issued_by_data = self.get_random_data(self.issued_by_data)
        return issued_by_data














