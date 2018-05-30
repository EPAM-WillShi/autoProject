# -*- coding: utf-8 -*-

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
    passport_radio = ('xpath', '//label[text()="Passport"]')
    visa_radio = ('xpath', '//label[text()="Visa"]')
    immigration_number = ('id', 'immigration_number')
    issued_date = ('id', 'immigration_passport_issue_date')
    expired_date = ('id', 'immigration_passport_expire_date')
    eligible_status = ('id', 'immigration_i9_status')
    issued_by = ('id', 'immigration_country')
    eligible_review_date = ('id', 'immigration_i9_review_date')
    comments = ('id', 'immigration_comments')
    add_attachment_btn = ('id', 'btnAddAttachment')
    upload_file = ('id', 'ufile')
    attachment_comment = ('id', 'txtAttDesc')
    upload_btn = ('id', 'btnSaveAttachment')

    def __init__(self, browser):
        super(Immigration, self).__init__(browser)

    def open_immigration_page_via_creating_emp(self, first_name, last_name):
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Immigration")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Immigration_page")

    def open_immigration_page_via_editing_emp(self, first_name, last_name):
        self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Immigration")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Immigration_page")





