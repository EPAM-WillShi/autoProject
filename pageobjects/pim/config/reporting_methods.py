# -*- coding: utf-8 -*-
"""
Created on 2018/6/6
@author: Yolanda Zhang
"""
from lib.log import Log
from pageobjects.pim.pim import PIM

class Report_method(PIM):

    delete_btn = ('id',"btnDel")
    add_btn = ('id',"btnAdd")
    method_name = ('id',"reportingMethod_name")
    save_btn = ('id',"btnSave")
    delete_checkbox = "//a[contains(text(), '{}')]/../preceding-sibling::td"
    message = ('xpath', "//div[contains(@class,'success')]")

    def __init__(self, browser):
        super(Report_method, self).__init__(browser)
        self.click_menu("Configuration")
        self.click_menu("Reporting Methods")
        Log.info("Arrive reporting methods page!")

    def add_report_method(self, name):
        self.click(self.add_btn)
        self.input_text(name, self.method_name)
        self.click(self.save_btn)
        Log.info("Add reporting methods successfully!")

    def delete_report_method(self,name):
        delete_ele = self.delete_checkbox.format(name)
        iele = ('xpath', delete_ele)
        self.click(iele)
        self.click(self.delete_btn)
        Log.info("Delete reporting method successfully!")
