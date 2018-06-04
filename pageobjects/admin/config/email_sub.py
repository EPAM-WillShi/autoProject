# -*- coding: utf-8 -*-
'''
Created on 2018��4��26��

@author: Angelia_Yao
'''
from pageobjects.admin.admin import Admin
from lib.log import Log


class EmailSub(Admin):
    """
    Notification components
    """
    edit_btn = ('id', 'btnEdit')
    save_btn = ('id', 'btnSave')
    lea_app = ('xpath', '//a[text()="Leave Applications"]')
    lea_app_box = ('id', 'ohrmList_chkSelectRecord_1')
    lea_ass = ('xpath', '//a[text()="Leave Assignments"]')
    lea_ass_box = ('id','ohrmList_chkSelectRecord_2' )
    lea_approvals = ('xpath', '//a[text()="Leave Approvals"]')
    lea_approvals_box = ('id','ohrmList_chkSelectRecord_3' )
    lea_cancel = ('xpath', '//a[text()="Leave Cancellations"]')
    lea_cancel_box = ('id','ohrmList_chkSelectRecord_4' )
    lea_rejections = ('xpath', '//a[text()="Leave Rejections"]')
    lea_rejections_box = ('id','ohrmList_chkSelectRecord_5' )
    checkboxes = ('xpath', '//input[@type="checkbox"]')

    def __init__(self, browser):
        super(Admin, self).__init__(browser)

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

    def disable_notification(self):
        self.click(self.edit_btn)
        self.click(self.lea_app_box)
        self.click(self.lea_ass_box)
        self.click(self.lea_approvals_box)
        self.click(self.lea_cancel_box)
        self.click(self.lea_rejections_box)
        self.click(self.save_btn)


