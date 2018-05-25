# -*- coding: utf-8 -*-
from pageobjects.admin.admin import Admin
from lib.log import Log

class JobTitles(Admin):
    """
    Admin page job titles main components
    """
    add_Button = ('ID', 'btnAdd')
    delete_button = ('id', 'btnDelete')
    message = ('XPATH', "//*[@class='message success fadable']")

    OK_button_confirm = ('ID', 'dialogDeleteBtn')
    Cancel_button_confirm = ('xpath',"//*[@id = 'dialogDeleteBtn']/../input[2]")
    
    def __init__(self,browser):
        super(JobTitles, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Job Titles")
        Log.info("Arrive Admin Job Titles page")

    def click_add_button(self):
        self.wait_unit_el_present(self.add_Button)
        self.click(self.add_Button)

    def click_job_title(self, keys):
        edit_element = ('LINK_TEXT', keys)
        self.click(edit_element)

    def click_delete_button(self):
        self.click(self.delete_button)

    def click_confirm_dialog_ok(self):
        self.sleep(5)
        self.click(self.OK_button_confirm)

    def click_confirm_dialog_cancel(self):
        self.sleep(5)
        self.click(self.Cancel_button_confirm)

    def check_delete_element_(self, keys):
        element = self.wait_unit_el_present(keys)
        if element is not None:
            Log.info("delete job title failed! ")

        else:
            return None

    def click_checkbox(self,keys):
        a = '//a[text()="{}"]/../../td[1]/input'
        b = a.format(keys)
        job_title_checkbox = ("xpath", b)
        self.click(job_title_checkbox)
        Log.info("check on checkbox successfully")

    def assert_message(self, return_message):
        """
        Assert the result of current operation
        """
        a = self.get_element_text(self.message)
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)

