# -*- coding: utf-8 -*-

from lib.log import Log
from pageobjects.pim.pim import PIM
from pageobjects.pim.add_employee import AddEmployee

class EmployeeList(PIM):
    """
    Employee list page elements
    """
    srch_empname = ("id", "empsearch_employee_name_empName")
    srch_empid = ("id", "empsearch_id")
    srch_btn = ("id", "searchBtn")
    srch_result = ('xpath', './/*[@id="resultTable"]//td')

    def __init__(self, browser):
        super(EmployeeList, self).__init__(browser)
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