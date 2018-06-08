# -*- coding: utf-8 -*-
"""
Created on 2018/6/6
@author: Joanna Li
"""
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lib.log import Log
from pageobjects.admin.admin import Admin
class Structure(Admin):
    """
    Structure page
    """
    # structure main page objects
    structure_title = ('xpath', "//h1[text()='Organization Structure']")
    edit_btn = ('ID', 'btnEdit')

    # add/edit/delete structure page object
    edit_link = ("class_name", "editLink")
    add_btn = ("class_name", "addButton")
    delete_btn = ("class_name", "deleteButton")
    delete_btn_path = "//a[text()='{}']/following-sibling::a[2]"
    structure_tree = ("id", "node_1")
    top1_namelink = "//li[@id='node_1']/a[@class='editLink']"
    top1_add_btn = "//li[@id='node_1']/a[@class='addButton']"
    message_text = ("id", "messageDiv")
    save_message = "Successfully Saved"
    delete_message = "Successfully Deleted"
    label_text = "display: none"
    label_flag = ("xpath", "//a[@class='editLink']")

    # dialog unit objects
    unit_id = ("id", "txtUnit_Id")
    unit_name = ("id", "txtName")
    unit_desc = ("id", "txtDescription")
    unit_save_btn = ("id", "btnSave")
    unit_ok_btn = ("id", "dialogYes")
    # unit_confirmation_title = ("xpath", "OrangeHRM - Confirmation Required")

    def __init__(self, browser):
        super(Structure, self).__init__(browser)
        self.click_menu("Organization")
        self.click_menu("Structure")
        self.wait_unit_el_present(self.structure_title)
        self.wait_unit_el_present(self.edit_btn)
        Log.info("Arrive at structure page and shows normally")

    def verify_init_structure(self):
        Log.info("Start to verify structure tree is disabled when come to from menu")
        assert self.is_label_structure()

    def add_top1_unit(self, unit_id, unit_name, unit_desc):
        Log.info("Start to add a unit of top 1")
        self.click(self.edit_btn)
        self.wait_unit_el_present(("xpath", self.top1_add_btn))
        assert self.get_element_attribute(self.edit_btn, "value") == 'Done'
        if not self.check_unitname_exists(unit_id + " : " + unit_name):
            self.click(("xpath", self.top1_add_btn))
            self.type_unit_fields(unit_id, unit_name, unit_desc)
            self.click(self.unit_save_btn)
            # assert self.get_element_text(self.message_text) == self.save_message
            self.click(self.edit_btn)
            self.sleep(3)
            assert self.is_label_structure()
            Log.info("Top 1 unit is added successfully")
        else:
            Log.info("The unit name have already exist, do nothing! please add one unit changing name")

    def check_unitname_exists(self, unit_name):
        is_exist = False
        eles = self.get_elements(self.edit_link)
        for ele in eles:
            if ele.text == unit_name:
                is_exist = True
                break
        return is_exist

    def type_unit_fields(self, unit_id, unit_name, unit_desc):
        Log.info("Start to input each field for unit")
        self.input_text(unit_id, self.unit_id)
        self.input_text(unit_name, self.unit_name)
        self.input_text(unit_desc, self.unit_desc)

    def is_label_structure(self):
        Log.info("Start to verify organization structure is disabled")
        is_label = False
        eles = self.get_elements(self.label_flag)
        for ele in eles:
            if self.label_text in ele.get_attribute("style"):
                is_label = True
                break
        return is_label

    def delete_unit(self, unit_idname):
        Log.info("Start to delete a unit in structure")
        self.click(self.edit_btn)
        self.wait_unit_el_present(("xpath", self.top1_add_btn))
        assert self.get_element_attribute(self.edit_btn, "value") == 'Done'
        selector = ('xpath', self.delete_btn_path.format(unit_idname))
        self.click(selector)
        self.click(self.unit_ok_btn)
        self.sleep(2)
        # assert self.get_element_text(self.message_text) == self.delete_message
        assert (not self.check_unitname_exists(unit_idname))
        self.click(self.edit_btn)
        self.sleep(3)
        assert self.is_label_structure()

    def edit_unit(self, orig_unit_id, orig_unit_name, unit_id, unit_name, unit_desc):
        Log.info("Start to edit a unit")
        self.click(self.edit_btn)
        self.wait_unit_el_present(("xpath", self.top1_add_btn))
        assert self.get_element_attribute(self.edit_btn, "value") == 'Done'
        if not self.check_unitname_exists(unit_id + " : " + unit_name):
            self.click(("xpath", self.top1_add_btn))
            self.type_unit_fields(unit_id, unit_name, unit_desc)
            self.click(self.unit_save_btn)
            # assert self.get_element_text(self.message_text) == self.save_message
            self.click(self.edit_btn)
            assert self.is_label_structure()
            Log.info("Top 1 unit is added successfully")
        else:
            Log.info("The unit name have already exist, do nothing! please add one unit changing name")







