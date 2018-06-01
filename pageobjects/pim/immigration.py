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

    def __init__(self, browser):
        super(Immigration, self).__init__(browser)

    def open_immigration_page_via_creating_emp(self, first_name, last_name):
        """
        Go to Immigration page via creating an employee
        """
        try:
            self.add_employee(first_name, last_name)
        except Exception:
            BaseException("Cannot create employee successfully.")
        self.switch_employee_detail_page("Immigration")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Immigration page via creating emp")
        else:
            Log.info("Cannot arrive Immigration page via creating emp")

    def open_immigration_page_via_editing_emp(self, first_name, last_name):
        """
        Go to Immigration page via editing an employee
        """
        try:
            self.click_employee_to_edit(first_name, last_name)
        except:
            self.add_employee(first_name, last_name)
            self.click_menu("Employee List")
            self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Immigration")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Immigration page via editing emp")
        else:
            Log.info("Cannot arrive Immigration page via editing emp")

    def input_immigration_details(self, document, number, issued_date, expiry_date,
                                  eligible_status, issued_by, eligible_review_date, comments):
        """
        Input the immigration details
        """
        document = document.title()
        document_ele = self.document_radio.format(document)
        self.click(('xpath', document_ele))
        self.input_text(number, self.immigration_number)
        if issued_date is not None:
            self.input_text(issued_date, self.issued_date_ele)
            self.press_enter_key(self.issued_date_ele)
        if expiry_date is not None:
            self.input_text(expiry_date, self.expired_date_ele)
            self.press_enter_key(self.expired_date_ele)
        if eligible_status is not None:
            self.input_text(eligible_status, self.eligible_status_ele)
        if issued_by is not None:
            self.set_combox_value(issued_by, self.issued_by_ele)
        if eligible_review_date is not None:
            self.input_text(eligible_review_date, self.eligible_review_date_ele)
            self.press_enter_key(self.eligible_review_date_ele)
        if comments is not None:
            self.input_text(comments, self.comments_ele)

    def add_immigration(self, document, number, issued_date, expiry_date,
                        eligible_status, issued_by, eligible_review_date, comments):
        """
        Add an immigration record
        """
        self.click(self.add_btn)
        self.input_immigration_details(document, number, issued_date, expiry_date,
                                       eligible_status, issued_by, eligible_review_date, comments)
        self.click(self.save_btn)
        Log.info("The immigration record is added.")

    def cancel_add_immigration(self, document, number, issued_date, expiry_date,
                               eligible_status, issued_by, eligible_review_date, comments):
        """
        Cancel the immigration record creation
        """
        self.click(self.add_btn)
        self.input_immigration_details(document, number, issued_date, expiry_date,
                                       eligible_status, issued_by, eligible_review_date, comments)
        self.click(self.cancel_btn)
        Log.info("Cancel the immigration record creation.")

    def edit_immigration(self, old_document, document, number, issued_date, expiry_date,
                         eligible_status, issued_by, eligible_review_date, comments):
        """
        Edit an immigration record
        """
        self.click(('link_text', old_document))
        self.input_immigration_details(document, number, issued_date, expiry_date,
                                       eligible_status, issued_by, eligible_review_date, comments)
        self.click(self.save_btn)
        Log.info("The immigration record is edited.")

    def cancel_edit_immigration(self, old_document, document, number, issued_date, expiry_date,
                         eligible_status, issued_by, eligible_review_date, comments):
        """
        Cancel the immigration record editing
        """
        self.click(('link_text', old_document))
        self.input_immigration_details(document, number, issued_date, expiry_date,
                                       eligible_status, issued_by, eligible_review_date, comments)
        self.click(self.cancel_btn)
        Log.info("Cancel the immigration record editing.")

    def check_immigration_details(self, document, number, issued_date, expiry_date, issued_by):
        """
        Check the immigration details
        """
        expected_text = document + " " + number + " " + issued_by + " " + issued_date + " " + expiry_date
        check_details = self.check_all_values.format(number)
        actual_text = self.get_element_text(('xpath', check_details))
        assert actual_text == expected_text
        Log.info("The immigration record is correct.")

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

    def delete_immigration(self, document):
        """
        Delete an immigration record
        """
        check_immigration = self.check_one_ele.format(document)
        self.click(('xpath', check_immigration))
        self.click(self.delete_btn)
        Log.info("The immigration record is deleted.")

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











