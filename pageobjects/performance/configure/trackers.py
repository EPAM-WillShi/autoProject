# -*- coding: utf-8 -*-
'''
Created on 2018��4��27��

@author: Angelia_Yao
'''
from pageobjects.performance.performance import Performance
from lib.log import Log


class Trackers(Performance):
    """
    Performance Trackers page objects
    """
    head_title = ('xpath', '//h1[text()="Performance Trackers"]')
    add_btn = ('id', 'btnAdd')
    delete_btn = ('id', 'btnDelete')
    tracker_name = ('name', 'addPerformanceTracker[tracker_name]')
    epm_name = ('name', 'addPerformanceTracker[employeeName][empName]')
    review_addbtn = ('id', 'btnAssignEmployee')
    review_rembtn = ('id', 'btnRemoveEmployee')
    save_btn = ('xpath', './/input[@name="btnSave"]')
    cancel_btn = ('xpath', './/input[@name="btnCancel"]')
    ava_review = ('xpath', './/select[@name="addPerformanceTracker[availableEmp][]"]')
    assgin_review = ('xpath', './/select[@name="addPerformanceTracker[assignedEmp][]"]')
    new_add =('xpath', './/table[@id="resultTable"]//tbody/tr[./td[2]//a[text()="Robert Craig"]][./td[3]//a[text()="test"]]')
    record_checkbox = ('xpath', './/table[@id="resultTable"]//tbody/tr[./td[2]//a[text()="Robert Craig"]][./td[3]//a[text()="test"]]/td[1]')
    del_cancel = ('xpath', '//div[@class="modal-footer"]/input[@class="btn reset"]')
    del_OK = ('id', 'dialogDeleteBtn')
    # add1 = 'xpath'
    # add2 = './/input[@type="checkbox"]'



    def __init__(self, browser):
        """
        Arrive user to Performance Page
        """
        super(Trackers, self).__init__(browser)
        self.click_menu("Configure")
        self.click_menu("Trackers")
        self.wait_unit_el_present(self.head_title)

    def add_pertracker(self, value1, value2, value3):
        self.click(self.add_btn)
        self.input_text(value1, self.tracker_name)
        self.input_text(value2, self.epm_name)
        # self.set_combox_value(value3, self.ava_review)
        self.select_random_list(self.ava_review)
        self.click(self.review_addbtn)
        self.click(self.save_btn)
        Log.info("add successfully")

    def validate_added_tracker(self, keys):
        self.is_element_visible(keys)
        Log.info("record display")

    def select_checkbox(self, keys):
        self.wait_unit_el_present(keys)
        self.click(keys)

    def delete_added_tracker(self, keys1, keys2, keys3):
        self.click(keys1)
        self.sleep(3)
        self.click(keys2)
        self.click(keys1)
        self.sleep(3)
        self.click(keys3)

    def check_delete_record(self, keys):
        text = self.get_element_text(keys)
        if text is not None:
            Log.info("delete tracker failed! ")

        else:
            Log.info("delete tracker successfully")


