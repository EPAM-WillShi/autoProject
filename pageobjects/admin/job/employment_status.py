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

    # Define declaration for Employment Status status page
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
    edit_record = ('link_text', 'test employment status')
    delete_record = ("xpath", "//a[contains(text(),'test employment status')]/../../td[1]/input")
    success_flag = ("xpath", "//*[@class='message success fadable']")


    def __init__(self,browser):
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
        self.sleep(3)
        self.click(self.save_btn)
        assert "Successfully Saved" in self.get_element_text(self.success_flag)
        Log.info("Create employment status Successfully")


    # def add_employee_status(self, employment_status_name):
    #     """
    #     Try to add a new employment status via clicking save button
    #     """
    #     Log.info("Start to add employment status function via click Add button")
    #     check_epstatus_name = self.check_if_emp_status_exist(employment_status_name)
    #     if check_epstatus_name is None:
    #         self.click(self.add_btn)
    #         self.clear_text(self.empstatus_namefield)
    #         self.input_text(employment_status_name, self.empstatus_namefield)
    #         self.sleep(3)
    #         self.click(self.save_btn)
    #         assert "Successfully Saved" in self.get_element_text(self.success_flag)
    #         Log.info("Create new employment status Successfully")

    def edit_employee_status(self, edit_name):
        """
         Try to edit exist employment status
        """
        Log.info("Start to edit exist employment status")
        self.click(self.edit_record)
        self.sleep(3)
        self.clear_text(self.empstatus_namefield)
        self.input_text(edit_name, self.empstatus_namefield)
        self.sleep(3)
        self.click(self.save_btn)
        assert "Successfully Saved" in self.get_element_text(self.success_flag)
        Log.info("Edit exist employment status Successfully")

    def delete_employee_status(self, employment_status_name):
        """
        Try to delete exist employment status
        """
        Log.info("Start to delete employment status record")
        check_epstatus_name = self.check_if_emp_status_exist(employment_status_name)
        if check_epstatus_name == employment_status_name:
            self.sleep(3)
            self.click(self.delete_record)
            self.sleep(3)
            self.click(self.delete_btn)
            self.sleep(3)
            self.click(self.dialog_delete_btn)
            assert "Successfully Deleted" in self.get_element_text(self.success_flag)
            Log.info("Employment status record is deleted Successfully!")
