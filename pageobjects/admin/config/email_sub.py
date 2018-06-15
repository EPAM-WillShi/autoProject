# -*- coding: utf-8 -*-
"""
Created on 2018��4��26��

@author: Angelia_Yao
"""

from pageobjects.admin.admin import Admin
from lib.log import Log


class EmailSub(Admin):
    """
    Notification components
    """
    sub_title = ('xpath', '//h1[text()="Subscribers : Leave Applications"]')
    add_subtitle = ('xpath', '//h1[@id="subscriberHeading"]')
    edit_btn = ('id', 'btnEdit')
    save_btn = ('id', 'btnSave')
    lea_app = ('xpath', '//a[text()="Leave Applications"]')
    lea_app_box = ('id', 'ohrmList_chkSelectRecord_1')
    lea_ass = ('xpath', '//a[text()="Leave Assignments"]')
    lea_ass_box = ('id', 'ohrmList_chkSelectRecord_2')
    lea_approvals = ('xpath', '//a[text()="Leave Approvals"]')
    lea_approvals_box = ('id', 'ohrmList_chkSelectRecord_3')
    lea_cancel = ('xpath', '//a[text()="Leave Cancellations"]')
    lea_cancel_box = ('id', 'ohrmList_chkSelectRecord_4')
    lea_rejections = ('xpath', '//a[text()="Leave Rejections"]')
    lea_rejections_box = ('id', 'ohrmList_chkSelectRecord_5')
    checkboxes = ('xpath', '//input[@type="checkbox"]')
    sub_addbtn = ('id', 'btnAdd')
    sub_delbtn = ('id', 'btnDelete')
    sub_backbtn = ('id', 'btnBack')
    sub_name = ('id', 'subscriber_name')
    sub_email = ('id', 'subscriber_email')
    sub_savebtn = ('id', 'btnSave')
    sub_cancelbtn = ('id', 'btnCancel')
    sub_table = ('xpath', '//table[@id="resultTable"]')
    add_record = ('xpath', '//table[@id="resultTable"]/tbody/tr/td[text()="anne_tang@epam.com"]')
    record_box = ('xpath', '//tr/td[1]')
    del_OK = ('xpath', '//input[@id="dialogDeleteBtn"]')
    del_cancel = ('xpath', '//input[@class="btn reset"][@value="Cancel"]')


    def __init__(self, browser):
        super(EmailSub, self).__init__(browser)

    # def switch_menu(self):
    #     """
    #     Back to Email Configuration page
    #     """
    #     self.click_menu("Admin")
    #     self.click_menu("Configuration")
    #     self.click_menu("Email Subscriptions")

    def enable_notification(self):
        self.click(self.edit_btn)
        self.click(self.lea_app_box)
        self.click(self.lea_ass_box)
        self.click(self.lea_approvals_box)
        self.click(self.lea_cancel_box)
        self.click(self.lea_rejections_box)
        self.click(self.save_btn)
        self.check_element_selected(self.lea_app_box)
        self.check_element_selected(self.lea_ass_box)
        self.check_element_selected(self.lea_approvals_box)
        self.check_element_selected(self.lea_cancel_box)
        self.check_element_selected(self.lea_rejections_box)
        Log.info("enable notification successfully")

    def disable_notification(self):
        self.click(self.edit_btn)
        self.click(self.lea_app_box)
        self.click(self.lea_ass_box)
        self.click(self.lea_approvals_box)
        self.click(self.lea_cancel_box)
        self.click(self.lea_rejections_box)
        self.click(self.save_btn)
        Log.info("disable notification successfully")

    def add_subscribers_leave_app(self, ptitle1, ptitle2, name, email):
        self.click(self.lea_app)
        assert ptitle1 == self.get_element_text(self.sub_title)
        Log.info("Arrive Subscribers : Leave Applications page")
        self.click(self.sub_addbtn)
        assert ptitle2 == self.get_element_text(self.add_subtitle)
        Log.info("Arrive Add Subscriber page")
        self.input_text(name, self.sub_name)
        self.input_text(email, self.sub_email)
        self.click(self.sub_cancelbtn)
        self.click(self.sub_addbtn)
        self.input_text(name, self.sub_name)
        self.input_text(email, self.sub_email)
        self.click(self.sub_savebtn)
        Log.info("add subscribers successfully")

    def validate_add_suc(self, value):
        # validate add successfully
        lst_result = self.get_element_text(self.sub_table).encode('utf-8').split('\n')
        # print lst_result
        for i in lst_result:
            if i == value:
                print 'pass'
                break

    def delete_record(self):
        self.click(self.record_box)
        self.click(self.sub_delbtn)
        self.sleep(3)
        self.click(self.del_cancel)
        self.click(self.sub_delbtn)
        self.sleep(3)
        self.click(self.del_OK)
        self.sleep(2)
        self.click(self.sub_backbtn)
        Log.info("delete subscribers successfully")

    def validate_delete(self, value):
        lst_result = self.get_element_text(self.sub_table).encode('utf-8').split('\n')
        for i in lst_result:
            if i == value:
                print 'failed'
                break
















