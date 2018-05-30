# -*- coding: utf-8 -*-

from lib.log import Log
from pageobjects.pim.pim import PIM
from pageobjects.pim.add_employee import AddEmployee

class EmployeeList(PIM):
    """
    Employee list page elements
    """
    save_btn = ('id', 'btnSave')
    search_empid = ('id', 'empsearch_id')
    search_emp = ('id', 'empsearch_employee_name_empName')
    search_btn = ('id', 'searchBtn')
    select_row = ('name', 'chkSelectRow[]')
    delete_btn = ('id', 'btnDelete')
    delete_box = ('xpath', './/*[@id="deleteConfModal"]//p')
    cancel_btn = ('xpath', './/*[@class="btn cancel"]')
    ok_btn = ('xpath', './/*[@id="dialogDeleteBtn"]')
    delete_result = ('xpath', './/*[@id="resultTable"]//td')
    check_all = ('id', 'ohrmList_chkSelectAll')
    check_all_ret = ('xpath', './/input[contains(@id,"ohrmList_chkSelectRecord")]')
    uncheck_all_ret = ('xpath', './/table[@id="resultTable"]/tbody/tr/td[1][not(@check)]')
    table_all = ('xpath', './/*[@id="resultTable"]/tbody/tr')
    # Anne added 2018-4-27
    search_empname = ('xpath', './/input[@name="empsearch[employee_name][empName]"]')
    search_empsupname = ('xpath', './/input[@name="empsearch[supervisor_name]"]')
    search_empsts = ('xpath', './/select[@name="empsearch[employee_status]"]')
    search_empjobtl = ('xpath', './/select[@name="empsearch[job_title]"]')
    search_subunit = ('xpath', './/select[@name="empsearch[sub_unit]"]')
    search_includ = ('xpath', './/select[@name="empsearch[termination]"]')
    reset_btn = ('xpath', './/input[@name="_reset"]')
    row1_column2 = ('xpath', './/tr[1]/td[3]')
    row2_column2 = ('xpath', './/tr[2]/td[3]')
    edit_employee_ele = '//tr[./td[3]/a[text()="{}"]][./td[4]/a[text()="{}"]]//td[2]'
    add_btn_ele = ('id', 'btnAdd')
    save_btn_ele = ('ID', 'btnSave')
    tab_ele = '//div[@id="employee-details"]//a[text()="{}"]'
    first_name_ele = ('ID', 'firstName')
    last_name_ele = ('ID', 'lastName')

    def __init__(self, browser):
        super(EmployeeList, self).__init__(browser)
        self.click_menu("Employee List")
        Log.info("Arrive PIM Employee List page")
    
    def query_employee_by_id(self, employee_id):
        """
        Query the employee by employee id
        """
        emp_id = self.wait_unit_el_present(self.search_empid)
        if emp_id is not None:
            self.clear_text(self.search_empid)
            self.input_text(employee_id, self.search_empid)
            self.click(self.search_btn)
            query_res = self.get_element_text(self.delete_result)
            if query_res == 'No Records Found':
                ele_exist = False
            else:
                ele_exist = True
            return ele_exist

    def query_employee_by_name(self, employee):
        """
        Query the employee by employee name
        """
        emp = self.wait_unit_el_present(self.search_emp)
        if emp is not None:
            self.clear_text(self.search_emp)
            self.input_text(employee, self.search_emp)
            self.click(self.search_btn)
            query_res = self.get_element_text(self.delete_result)
            if query_res == 'No Records Found':
                ele_exist = False
            else:
                ele_exist = True
            return ele_exist
    
    def cancel_del_employee(self, employee):
        """
        Cancel delete employee function
        """
        # Check if the employee exist
        check_flag = self.query_employee_by_name(employee)
        if check_flag is False:
            firstname = employee.split()[0]
            lastname = employee.split()[1]
            addemployee = AddEmployee(self.driver)
            addemployee.add_user_employee(firstname, lastname)
            self.click_menu("Employee List") 
            Log.info("Back to Employee list page after create new employee")
            self.query_employee_by_name(employee)
        # Delete the employee   
        self.click(self.select_row)
        self.click(self.delete_btn)
        assert 'Delete records?' == self.get_element_text(self.delete_box)
        self.click(self.cancel_btn)
        Log.info("Cancel of employee deletion succeed")    
    
    def delete_employee(self, employee):
        """
        Delete employee:
        1. Search for employee
        2. choose the employee and click the delete option(cancel/ok)
        """
        # Check if the employee exist
        check_flag = self.query_employee_by_name(employee)
        if check_flag is False:
            firstname = employee.split()[0]
            lastname = employee.split()[1]
            addemployee = AddEmployee(self.driver)
            addemployee.add_user_employee(firstname, lastname)
            self.click_menu("Employee List") 
            Log.info("Back to Employee list page after create new employee")
            self.query_employee_by_name(employee)
        # Delete the employee   
        self.click(self.select_row)
        self.click(self.delete_btn)
        assert 'Delete records?' == self.get_element_text(self.delete_box)
        self.click(self.ok_btn)
        assert 'No Records Found' == self.get_element_text(self.delete_result)
        Log.info('Employee deleted successfully')
 
    def emplist_chkall(self):
        """
        Test Employee List check-all Function
        """
        self.click(self.check_all)
        eles = self.get_elements(self.check_all_ret)
        for i in range(len(eles)):
            assert 'true' == eles[i].get_attribute("checked")
        Log.info("All records checked")

    def emplist_unchkall(self):
        """
        Test Employee List Uncheck-all Function
        """
        self.click(self.check_all)
        teles = self.get_elements(self.table_all)
        ueles = self.get_elements(self.uncheck_all_ret)
        if len(ueles) == len(teles):
            Log.info("All records unchecked")
        else:
            raise Exception, "Not all unchecked"

    # Anne added 2018-4-27

    def input_search_text(self, value, keys):
        """
        clear input_box, then input search condition
        """
        self.clear_text(keys)
        self.input_text(value, keys)

    def select_downlist_option(self, value, keys):
        """
        select dropdown list value
        """
        self.set_combox_value(value, keys)

    def get_search_result(self, keys):
        """
        select dropdown list value
        """
        self.get_element_text(keys)

    def get_reset_result(self, keys):
        self.click(self.reset_btn)
        self.wait_unit_el_present(keys)

    # def get_listvalue(self, keys):
    #     text = self.get_element_text(keys)
    #     text1 = self.unicode_to_encode(text)
    #     self.split_linewrap_text(text1)
    #     return self.split_linewrap_text(text1)

    def add_employee(self, first_name, last_name):
        """
        Input all fields: First Name/Middle Name/Last Name/Attached the Photograph
        """
        self.click(self.add_btn_ele)
        self.clear_text(self.first_name_ele)
        self.input_text(first_name, self.first_name_ele)
        self.clear_text(self.last_name_ele)
        self.input_text(last_name, self.last_name_ele)
        self.click(self.save_btn_ele)

    def click_employee_to_edit(self, first_name, last_name):
        employee = self.edit_employee_ele.format(first_name, last_name)
        self.click(('xpath', employee))

    def switch_employee_detail_page(self, tab_name):
        try:
            tab = self.tab_ele.format(tab_name)
            self.click(('xpath', tab))
        except BaseException, e:
            print e
            Log.error(e)
            raise "Element %s not found" % tab_name


