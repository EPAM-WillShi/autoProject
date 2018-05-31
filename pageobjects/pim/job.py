# -*- coding: utf-8 -*-

from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList

class Job(EmployeeList):
    """
    Employee list - Job
    """
    job_flag = ('XPATH', "//h1[text()='Job']")
    edit_btn = ('ID', 'btnSave')
    Terminate_emp_btn = ('ID', 'btnTerminateEmployement')
    job_title = ('ID', 'job_job_title')
    emp_status = ('ID', 'job_emp_status')
    job_cat = ('ID', 'job_eeo_category')
    join_date = ('ID', 'job_joined_date')
    sub_unit = ('ID', 'job_sub_unit')
    loc = ('ID', 'job_location')
    contract_start_date = ('ID', 'job_contract_start_date')
    contract_end_date = ('ID', 'job_contract_end_date')
    contract_details = ('ID', 'job_contract_file')


    def __int__(self, browser):
        super(Job, self).__int__(browser)

    def open_job_page_via_creating_emp(self, first_name, last_name):
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Job")
        page_ele = self.get_element(self.job_flag)
        if page_ele is not None:
            Log.info("Arrive Job_page")

    def open_job_page_via_editing_emp(self, first_name, last_name):
        self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Job")
        page_ele = self.get_element(self.job_flag)
        if page_ele is not None:
            Log.info("Arrive Job_page")

    def edit_emp_job(self, jobtitle, empStatus):
        self.click(self.edit_btn)
        self.input_text(jobtitle, self.job_title)
        self.input_text(empStatus, self.emp_status)
        self.click(self.edit_btn)


