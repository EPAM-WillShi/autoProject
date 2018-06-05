# -*- coding: utf-8 -*-

from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList

class EmployeeListSearch(EmployeeList):
    """
    Employee list page elements
    """
    srch_empname = ("id", "empsearch_employee_name_empName")
    srch_empid = ("id", "empsearch_id")
    srch_btn = ("id", "searchBtn")
    srch_result = ('xpath', './/*[@id="resultTable"]//td')
    search_supervisor_name = ('id', 'empsearch_supervisor_name')
    search_job_title = ('id', 'empsearch_job_title')
    search_sub_unit = ('id', 'empsearch_sub_unit')
    search_btn = ('id', 'searchBtn')
    reset_btn = ('id', 'resetBtn')
    search_status = ('id', 'empsearch_employee_status')

    def __init__(self, browser):
        super(EmployeeListSearch, self).__init__(browser)
        self.click_menu("Employee List")
        Log.info("Arrive Employee List page")

    def search_employee_by_name(self, empname):
        '''
        Search employee by name
        '''
        self.wait_unit_el_present(self.srch_empname)
        self.input_text(empname, self.srch_empname)
        self.click(self.srch_btn)
        Log.info("Search employee by name")
        srch_res = self.get_element_text(self.srch_result)
        if srch_res == 'No Records Found':
            print("No such records found!")
        else:
            print("Record is found!")
        self.click(self.reset_btn)

    def search_employee_by_id(self, empid):
        '''
        Search employee by id
        '''
        self.wait_unit_el_present(self.srch_empid)
        self.input_text(empid, self.srch_empid)
        self.click(self.srch_btn)
        Log.info("Search employee by id")
        srch_res = self.get_element_text(self.srch_result)
        if srch_res == 'No Records Found':
            print("No such records found!")
        else:
            print("Record is found!")
        self.click(self.reset_btn)

    def search_emp_by_supervisor_name(self, supervisor_name):
        self.wait_unit_el_present(self.search_supervisor_name)
        self.input_text(supervisor_name, self.search_supervisor_name)
        self.click(self.search_btn)
        Log.info("Search employee by Supervisor Name!")
        search_res = self.get_element_text(self.srch_result)
        if search_res == "No Records Found":
            print("No records found!")
        else:
            print("Record is found!")
        self.click(self.reset_btn)

    def search_emp_by_job_title(self, job_title):
        self.wait_unit_el_present(self.search_job_title)
        self.set_combox_value(job_title, self.search_job_title)
        self.click(self.search_btn)
        Log.info("Search employee by Job Title!")
        search_res = self.get_element_text(self.srch_result)
        if search_res == "No Records Found":
            print("No records found!")
        else:
            print("Record is found!")
        self.click(self.reset_btn)

    def search_emp_by_sub_unit(self, sub_unit):
        self.wait_unit_el_present(self.search_sub_unit)
        self.set_combox_value(sub_unit, self.search_sub_unit)
        self.click(self.search_btn)
        Log.info("Search employee by Sub Unit!")
        search_res = self.get_element_text(self.srch_result)
        if search_res == "No Records Found":
            print("No records found!")
        else:
            print("Record is found!")
        self.click(self.reset_btn)

    def search_emp_by_status(self, status):
        """
        Search employee by status
        """
        self.wait_unit_el_present(self.search_status)
        self.set_combox_value(status, self.search_status)
        self.click(self.srch_btn)
        Log.info("Search employee by Status!")
        search_res = self.get_element_text(self.srch_result)
        if search_res == "No Records Found":
            print("No records found!")
        else:
            print("Record is found!")
        self.click(self.reset_btn)