# -*- coding: utf-8 -*-
"""
Created on 2018/6/13
@author: Molly Xue
"""

from pageobjects.admin.admin import Admin
from lib.log import Log


class JobCategories(Admin):
    """
    Job Categories page
    """
    # Define declaration for Job Categories page
    add_btn = ('ID', 'btnAdd')
    delete_btn = ('ID', 'btnDelete')
    select_all_checkbox = ('ID', 'ohrmList_chkSelectAll')

    # Define declaration for Add Job Category Page
    save_btn = ('ID', 'btnSave')
    jobcategory_namefield = ('ID', 'jobCategory_name')
    jobcategory_valid_flag = ('xpath', "//span[@class='validation-error']")
    cancel_btn = ('ID', 'btnCancel')

    # Define declaration for confirmation dialog
    dialog_delete_btn = ('ID', 'dialogDeleteBtn')
    dialog_reset_btn = ('xpath', "//input[@class='btn reset']")

    # Define declaration for Job Category table
    jobcategory_list = ("xpath", "//tbody/tr/td[2]/a")
    no_records_msg = ('xpath', '//tbody/tr/td')
    success_flag = ("xpath", "//*[@class='message success fadable']")
    del_element = '//a[text()="{}"] /../../ td[1]/input'

    def __init__(self,browser):
        super(JobCategories, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Job Categories")
        Log.info("Arrive Admin Job Categories page")

    def check_if_job_category_exist(self, jobcategory):
        """
        Check if the job category exist
        """
        jobcate_names = self.get_elements_texts(self.jobcategory_list)
        for jobcate_name in jobcate_names:
            if jobcategory == jobcate_name:
                return jobcategory
                break
        return None

    def check_if_job_category_valid(self, jobcategory):
        """
        Check valid job category field allowed
        """

        self.click(self.add_btn)
        self.clear_text(self.jobcategory_namefield)
        self.input_text(jobcategory, self.jobcategory_namefield)
        length = len(jobcategory)
        if length == 0:
            self.click(self.save_btn)
            assert "Required" in self.get_element_text(self.jobcategory_valid_flag)
            Log.info("Input job category as NULL is not allowed")
        elif length > 50:
            self.click(self.save_btn)
            assert "Should be less than 50 characters" in self.get_element_text(self.jobcategory_valid_flag)
            Log.info("Input job category more than 50 characters is not allowed")
            self.clear_text(self.jobcategory_namefield)
        else:
            Log.info("Input job category less than or equal to 50 characters is allowed")
        self.click(self.cancel_btn)

    def add_job_category(self, job_category):
        """
        Try to add a job category via click save button
        """
        Log.info("Start to add job category function via click Add button")
        self.click(self.add_btn)
        self.clear_text(self.jobcategory_namefield)
        self.input_text(job_category, self.jobcategory_namefield)
        self.sleep(2)
        self.click(self.save_btn)
        assert "Successfully Saved" in self.get_element_text(self.success_flag)
        Log.info("Create job category Successfully")

    def edit_job_category(self, exist_jobcate, edit_jobcate):
        """
         Try to edit exist job category
        """
        Log.info("Start to edit exist job category")
        jobcate_names = self.get_elements_texts(self.jobcategory_list)
        if exist_jobcate in jobcate_names:
            edit_element = ('LINK_TEXT', exist_jobcate)
            self.click(edit_element)
            self.sleep(2)
            self.clear_text(self.jobcategory_namefield)
            self.sleep(2)
            self.input_text(edit_jobcate, self.jobcategory_namefield)
            if edit_jobcate == '':
                self.sleep(2)
                Log.info("Your edit job category is NULL")
            elif edit_jobcate not in jobcate_names:
                self.sleep(2)
                self.click(self.save_btn)
                assert "Successfully Saved" in self.get_element_text(self.success_flag)
                Log.info("Edit exist job category Successfully")
            else:
                self.sleep(2)
                self.clear_text(self.jobcategory_namefield)
                Log.info("The edit job category is conflict with current exist job categorys")
        else:
            Log.info("There's no special job category need to edit.")

    def delete_job_category(self, jobcate_name):
        """
        Try to delete exist employment status, user created but not default ones
        """
        Log.info("Start to delete job category record")
        check_jobcate_names = self.check_if_job_category_exist(jobcate_name)
        if check_jobcate_names == jobcate_name:
            checkbox = self.del_element.format(jobcate_name)
            self.click(('XPATH', checkbox))
            self.sleep(2)
            self.click(self.delete_btn)
            self.sleep(2)
            self.click(self.dialog_delete_btn)
            assert "Successfully Deleted" in self.get_element_text(self.success_flag)
            Log.info("Job category record is deleted Successfully!")
        else:
            Log.info("No exist job category need to delete")

    def delete_all_job_category(self):
        """
        Try delete all job category
        """
        Log.info("Start to delete all job categorys")
        Check_no_record_found = self.get_element_text(self.no_records_msg)
        if Check_no_record_found == "No Records Found":
            Log.info("None job categories existed, no need delete action")
        else:
            self.click(self.select_all_checkbox)
            self.sleep(2)
            self.click(self.delete_btn)
            self.sleep(2)
            self.click(self.dialog_delete_btn)
            assert "Successfully Deleted" in self.get_element_text(self.success_flag)
            Log.info("All job categories are deleted successfully")
        Log.info("Run delete all job category action completed")