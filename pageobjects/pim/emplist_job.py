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
    attach_btn = ('ID', 'btnAddAttachment')
    message = ('XPATH', "//*[@class='message success fadable']")

    terminate = ('ID', 'btnTerminateEmployement')
    ter_title = ('ID', 'terminateEmployement')
    ter_reason = ('ID', 'terminate_reason')
    ter_date = ('ID', 'terminate_date')
    ter_note = ('ID', 'terminate_note')
    ter_conf_btn = ('ID', 'dialogConfirm')
    ter_msg = ('XPATH', '//a[contains(text(),"Terminated on")]')

    del_contract = ('ID', 'job_contract_update_2')
    rep_contract = ('ID', 'job_contract_update_3')
    not_defined_contract = ('ID', 'notDefinedLabel')
    contract_file = ('XPATH', '//li[@class="contractReadMode"]/a')

    def __int__(self, browser):
        super(Job, self).__int__(browser)

    def open_job_page_via_creating_emp(self, first_name, last_name):
        """
        Open Job page under Employee List by creating a new employee
        """
        self.add_employee(first_name, last_name)
        self.switch_employee_detail_page("Job")
        page_ele = self.get_element(self.job_flag)
        if page_ele is not None:
            Log.info("Arrive Job_page")

    def open_job_page_via_editing_emp(self, first_name, last_name):
        """
        Open Job page under Employee List by clicking an employee name
        """
        self.click_employee_to_edit(first_name, last_name)
        self.switch_employee_detail_page("Job")
        page_ele = self.get_element(self.job_flag)
        if page_ele is not None:
            Log.info("Arrive Job_page")

    def add_emp_job(self,jobtitle, empStatus, jobcategory, joindate, subunit,location, startdate, enddate, contract):
        """
        Add Job information for employee
        """
        Log.info("Start to edit job information...")
        self.click(self.edit_btn)
        self.sleep(2)
        self.set_combox_value(jobtitle, self.job_title)
        self.set_combox_value(empStatus, self.emp_status)
        self.set_combox_value(jobcategory, self.job_cat)
        self.input_text(joindate, self.join_date)
        self.select_option(self.sub_unit, 1)
        self.select_option(self.loc, 1)
        # self.set_combox_value(subunit, self.sub_unit)
        # self.set_combox_value(location, self.loc)
        self.input_text(startdate, self.contract_start_date)
        self.input_text(enddate, self.contract_end_date)
        self.upload_file(contract, self.contract_details)
        self.click(self.edit_btn)

    def verify_edit_job_success(self, return_message):
        """
        Assert the result of current operation

        """
        if self.get_element_text(self.message) is not None:
            assert return_message in self.get_element_text(self.message)
            Log.info(return_message)
        else:
            raise Exception("%s is not found" % return_message)


    def replace_current_contract(self, repcontract):
        """
        Replace current contract with a new contract
        """
        Log.info("Start to replace contract...")
        self.click(self.edit_btn)
        self.click(self.rep_contract)
        self.upload_file(repcontract, self.contract_details)
        self.click(self.edit_btn)
        self.sleep(2)
        assert self.get_element_text(self.contract_file).encode("utf-8") == repcontract

    def delete_current_contract(self):
        """
        Delete current contract
        """
        Log.info("Start to delete contract...")
        self.click(self.edit_btn)
        self.click(self.del_contract)
        self.click(self.edit_btn)
        assert self.get_element_text(self.not_defined_contract) == "Not Defined"

    def terminate_employment(self, terdate):
        """
        Terminate the employment for current employee
        """
        Log.info("Start to terminate employment...")
        self.click(self.terminate)
        self.wait_unit_el_present(self.ter_title)
        assert self.get_element(self.ter_title).is_displayed()
        self.select_option(self.ter_reason, 7)
        self.input_text("test-terminate", self.ter_note)
        self.input_text(terdate, self.ter_date)
        self.click(self.ter_conf_btn)
        assert terdate in self.get_element_text(self.ter_msg).encode("utf-8")

    def activate_employment(self, terdate):
        """
        Activate the employment for current employee
        """
        self.click(self.terminate)
        assert self.get_element_attribute(self.terminate, "value").encode("utf-8") == "Terminate Employment"












