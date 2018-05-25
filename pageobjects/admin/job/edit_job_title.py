# -*- coding: utf-8 -*-

from pageobjects.admin.admin import Admin
from lib.log import Log


class EditJobTitle(Admin):
    """
    Admin page Job edit job title main components

    """
    input_job_title = ('id', 'jobTitle_jobTitle')
    input_job_description = ('id', 'jobTitle_jobDescription')
    input_job_spec = ('id', 'jobTitle_jobSpec')

    save_button = ('id', 'btnSave')


    def __init__(self, browser):
        super(EditJobTitle, self).__init__(browser)
        self.click_menu("JOB")
        self.click_menu("Job Titles")

    def input_text_job_title(self,keys):
        # add job title
        self.input_text(keys, self.input_job_title)
        Log.info("write job title spec successfully")

    def input_text_job_description(self,keys):
        # add job title description
        self.input_text(keys, self.input_job_description)
        Log.info("write job title spec successfully")

    def input_text_job_spec(self,keys):
        # add job title spec
        self.input_text(keys, self.input_job_spec)
        Log.info("write job title spec successfully")

    def clear_job_title_info(self):
        # clear job title
        self.clear_text(self.input_job_spec)
        self.clear_text(self.input_job_title)
        self.clear_text(self.input_job_description)
        Log.info( "clear job title info successfully")

    def click_save_button(self):
        self.click(self.save_button)

    def click_edit_button(self):
        self.click(self.save_button)