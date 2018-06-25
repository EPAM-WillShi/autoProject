# -*- coding: utf-8 -*-
"""
Created on 2018/5/29
@author: Molly Xue
"""

from pageobjects.admin.admin import Admin
from lib.log import Log


class EmploymentStatus(Admin):
    """
    Employment Status page
    """

    # Define declaration for Employment status page
    add_btn = ('ID', 'btnAdd')
    delete_btn = ('ID', 'btnDelete')
    select_all_checkbox = ('ID', 'ohrmList_chkSelectAll')

    # Define declaration for Add Employee Status Page
    save_btn = ('ID', 'btnSave')
    empstatus_namefield = ('ID', 'empStatus_name')
    empstatus_valid_flag = ('xpath', "//span[@class='validation-error']")
    cancel_btn = ('ID', 'btnCancel')

    # Define declaration for confirmation dialog
    dialog_delete_btn = ('ID', 'dialogDeleteBtn')
    dialog_reset_btn = ('xpath', "//input[@class='btn reset']")

    # Define declaration for Employment Status table
    empstatus_namelist = ("xpath", "//tbody/tr/td[2]/a")
    success_flag = ("xpath", "//*[@class='message success fadable']")
    del_element = '//a[text()="{}"] /../../ td[1]/input'

    def __init__(self, browser):
        super(EmploymentStatus, self).__init__(browser)

    def select_menu(self):
        """
        Go to Employment Status page
        """
        self.driver.implicitly_wait(3)
        self.click_menu("Job")
        self.driver.implicitly_wait(3)
        self.click_menu("Employment Status")
        Log.info("Arrive Employment Status page")

    def check_if_emp_status_exist(self, esname):
        """
        Check if the employment status exist
        """
        names = self.get_elements_texts(self.empstatus_namelist)
        for name in names:
            if esname == name:
                return esname
                break
        return None

    def check_if_emp_status_valid(self, esname):
        """
        Check valid employment status field allowed
        """

        self.click(self.add_btn)
        self.clear_text(self.empstatus_namefield)
        self.input_text(esname, self.empstatus_namefield)
        length = len(esname)
        if length == 0:
            self.click(self.save_btn)
            assert "Required" in self.get_element_text(self.empstatus_valid_flag)
            Log.info("Input employment status as NULL is not allowed")
        elif length > 50:
            self.click(self.save_btn)
            assert "Should be less than 50 characters" in self.get_element_text(self.empstatus_valid_flag)
            Log.info("Input employment status more than 50 characters is not allowed")
            self.clear_text(self.empstatus_namefield)
        else:
            Log.info("Input employment status less than or equal to 50 characters is allowed")
        self.click(self.cancel_btn)

    def add_employee_status(self, employment_status_name):
        """
        Try to add a employment status via click save button
        """
        Log.info("Start to add employment status function via click Add button")
        self.click(self.add_btn)
        self.clear_text(self.empstatus_namefield)
        self.input_text(employment_status_name, self.empstatus_namefield)
        self.sleep(2)
        self.click(self.save_btn)
        if self.get_element_text(self.success_flag) is not None:
            assert "Successfully Saved" in self.get_element_text(self.success_flag)
            Log.info("Create employment status Successfully")
        else:
            raise Exception("Didn't get the message about Successfully Saved")

    def edit_employee_status(self, exist_name, edit_name):
        """
         Try to edit exist employment status
        """
        Log.info("Start to edit exist employment status")
        status_name_list = self.get_elements_texts(self.empstatus_namelist)
        if exist_name in status_name_list:
            edit_element = ('LINK_TEXT', exist_name)
            self.click(edit_element)
            self.sleep(2)
            self.clear_text(self.empstatus_namefield)
            self.sleep(2)
            self.input_text(edit_name, self.empstatus_namefield)
            if edit_name == '':
                self.sleep(2)
                Log.info("Your edit name is NULL")
            elif edit_name not in status_name_list:
                self.sleep(2)
                self.click(self.save_btn)
                assert "Successfully Saved" in self.get_element_text(self.success_flag)
                Log.info("Edit exist employment status Successfully")
            else:
                self.sleep(2)
                self.clear_text(self.empstatus_namefield)
                Log.info("The edit_name is conflict with current exist employee status")
        else:
            Log.info("There's no special employment status need to edit.")

    def delete_employee_status(self, employment_status_name):
        """
        Try to delete exist employment status, user created but not default ones
        """
        Log.info("Start to delete employment status record")
        check_epstatus_name = self.check_if_emp_status_exist(employment_status_name)
        if check_epstatus_name == employment_status_name:
            checkbox = self.del_element.format(employment_status_name)
            self.click(('XPATH', checkbox))
            self.sleep(2)
            self.click(self.delete_btn)
            self.sleep(2)
            self.click(self.dialog_delete_btn)
            assert "Successfully Deleted" in self.get_element_text(self.success_flag)
            Log.info("Employment status record is deleted Successfully!")
        else:
            Log.info("No exist employee status need to delete")

    def delete_muluser_employee_status(self, default_status_list):
        """
        Try delete all user new created employee status and keep default ones
        """
        Log.info("Start to delete all user defined employee status and keep ones")
        self.click(self.select_all_checkbox)
        self.sleep(2)
        def_epstatus_num = len(default_status_list)
        for i in range(0, int(def_epstatus_num)):
            default_status = default_status_list[i]
            ele = str(default_status)
            checkbox = self.del_element.format(ele)
            self.click(('XPATH',checkbox))
            self.sleep(2)
            i += 1
        self.click(self.delete_btn)
        self.sleep(2)
        self.click(self.dialog_delete_btn)
        assert "Successfully Deleted" in self.get_element_text(self.success_flag)
        Log.info("Employment status user records are deleted Successfully without any default ones!")

