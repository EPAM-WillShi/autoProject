# -*- coding: utf-8 -*-
from pageobjects.admin.admin import Admin
from lib.log import Log


class EmploymentStatus(Admin):
    """
    Employment Status page
    """
    add_btn = ('ID', 'btnAdd')
    save_btn = ('ID', 'btnSave')
    edit_btn = ('ID', 'btnEdit')
    delete_btn = ('ID', 'btnDelete')
    dialog_delete_btn = ('ID', 'dialogDeleteBtn')
    employment_status_name = ('ID', 'empStatus_name')
    edit_record = ('link_text', 'test employment status')
    success_flag = ("xpath", "//*[@class='message success fadable']")
    delete_record = ("xpath", "//a[contains(text(),'test employment status')]/../../td[1]/input")
    employee_status_names = ("xpath", "//tbody/tr/td[2]/a")

    def __init__(self,browser):
        super(EmploymentStatus, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Employment Status")
        Log.info("Arrive Employment Status page")

    def check_if_emp_status_exist(self, esname):
        """
        Check if the employee status exist
        """
        names = self.get_elements_texts(self.employee_status_names)
        for name in names:
            if esname == name:
                return esname
                break
        return None

    def add_employee_status(self, employment_status_name):
        """
        Click save button
        """
        Log.info("Add button is clicked")
        check_epstatus_name = self.check_if_emp_status_exist(employment_status_name)
        if check_epstatus_name is None:
            self.click(self.add_btn)
            self.clear_text(self.employment_status_name)
            self.input_text(employment_status_name, self.employment_status_name)
            self.sleep(3)
            self.click(self.save_btn)
            assert "Successfully Saved" in self.get_element_text(self.success_flag)
            Log.info("Save Successfully")

    def edit_employee_status(self, edit_name):
        """
         Edit element
        """
        Log.info("Start to edit employee status")
        self.click(self.edit_record)
        self.sleep(3)
        self.clear_text(self.employment_status_name)
        self.input_text(edit_name, self.employment_status_name)
        self.sleep(3)
        self.click(self.save_btn)
        assert "Successfully Saved" in self.get_element_text(self.success_flag)
        Log.info("Edit Successfully")

    def delete_employee_status(self, employment_status_name):
        """
        Click Delete button
        """
        Log.info("Start to delete employee status")
        check_epstatus_name = self.check_if_emp_status_exist(employment_status_name)
        if check_epstatus_name == employment_status_name:
            self.sleep(3)
            self.click(self.delete_record)
            self.sleep(3)
            self.click(self.delete_btn)
            self.sleep(3)
            self.click(self.dialog_delete_btn)
            assert "Successfully Deleted" in self.get_element_text(self.success_flag)
            Log.info("Records are deleted Successfully!")
