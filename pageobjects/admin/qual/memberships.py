# -*- coding: utf-8 -*-
"""
Created on 2018-06-04

@author: Dora Zhu
"""

from lib.log import Log
from pageobjects.admin.admin import Admin


class QualityMemberships(Admin):
    """
    Memberships page functions
    """
    add_btn = ('ID', 'btnAdd')
    name = ('ID', 'membership_name')
    save_btn = ('ID', 'btnSave')

    def __init__(self, browser):
        super(QualityMemberships, self).__init__(browser)
        self.click_menu("Qualifications")
        self.click_menu("Memberships")
        Log.info("Arrive Admin Memberships page")

    def add_quality_membership(self, add_name):
        """
        Add a membership

        """
        self.click(self.add_btn)
        self.input_text(add_name, self.name)
        self.click(self.save_btn)

