# -*- coding: utf-8 -*-
"""
Created on 2018/5/30
@author: Yolanda Zhang
"""

from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList


class Salary(EmployeeList):
    # search_emp = ("ID", "empsearch_employee_name_empName")
    # include = ("id","empsearch_termination")
    # search_btn = ('id', 'searchBtn')

    add_btn = ('id', 'addSalary')
    success_flag = ('xpath', '//h1[text()="Assigned Salary Components"]')
    no_record_flag = ('xpath', "//*[@id='tblSalary']//td[text() = 'No Records Found']")

    pay_grade = ('id', 'salary_sal_grd_code')
    salary_component = ('id', 'salary_salary_component')
    pay_frequency = ('id', 'salary_payperiod_code')
    currency = ('id', 'salary_currency_id')
    amount = ('id', 'salary_basic_salary')
    save_btn = ('id', 'btnSalarySave')
    cancel_btn = ('id', 'btnSalaryCancel')

    add_attachment_btn = ('id', 'btnAddAttachment')
    file_path = ('id', 'ufile')
    upload_btn = ('id', 'btnSaveAttachment')
    file_name = ('xpath', '//a[normalize-space(text())="salary.txt"]')

    delete_btn = ('id', 'delSalary')
    message = ('xpath', "//div[contains(@class,'success')]")

    salary_list = ('xpath', "//*[@id='tblSalary']")

    add_deposit_detail = ('id', 'salary_set_direct_debit')
    account_num = ('id', 'directdeposit_account')
    account_type = ('id', 'directdeposit_account_type')
    routing_num = ('id', 'directdeposit_routing_num')
    ramount = ('id', 'directdeposit_amount')
    other_name = ('id', "directdeposit_account_type_other")

    deposit_flag = ('xpath', "//*[@id='tblSalary']//h3[text()= 'Direct Deposit Details']")
    v_anum = ('xpath', "//table[@id='tblSalary']//table")

    list = []

    def __init__(self, browser):
        super(Salary, self).__init__(browser)
        self.click_menu("Employee List")
        Log.info("Arrive Employee list page")

    # def get_emp_record(self, name):
    #     self.clear_text(self.search_emp)
    #     self.input_text(name, self.search_emp)
    #     self.click(self.search_btn)
    #     self.wait(2)
    #     fname = name.split()[0]
    #     lname = name.split()[1]
    #     search_name = ('link_text', str(fname))
    #     self.click(search_name)

    def open_salary_page_via_creating_emp(self, fname, lname):
        self.add_employee(fname, lname)
        self.switch_employee_detail_page("Salary")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive salary page!")

    def search_emp_salary(self, fname, lname):
        self.query_employee_by_name(fname + ' ' + lname)
        self.click_employee_to_edit(fname, lname)
        self.switch_employee_detail_page("Salary")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive salary page!")

    def assign_salary(self, grade, component, frequency, currency, amount):
        # self.get_emp_record(name)
        # self.check_salary_page()
        self.click(self.add_btn)
        self.set_combox_value(grade, self.pay_grade)
        self.input_text(component, self.salary_component)
        self.set_combox_value(frequency, self.pay_frequency)
        self.wait_unit_el_present(self.currency)
        self.set_combox_value(currency, self.currency)
        self.input_text(amount, self.amount)
        self.click(self.save_btn)
        self.get_element_text(self.message)
        Log.info("Add record successfully!")

    def cancel_assgin_salary(self):
        self.click(self.add_btn)
        self.click(self.cancel_btn)

    def get_result_list(self):
        Log.info("Verify search result!")
        table = self.get_element(self.salary_list)
        table_rows = table.find_elements_by_tag_name("tr")
        Log.info("Total Rows: %d" % len(table_rows))
        return table_rows

    def verify_cancel(self):
        result1 = self.get_result_list()
        self.cancel_assgin_salary()
        result2 = self.get_result_list()
        if result1 == result2:
            Log.info("cancel successfully")
        else:
            Log.info("cancel fail!")

    def edit_salary(self, component, amount, num, dtype, rout, ramount,*args):
        search_name = ('link_text', str(component))
        self.click(search_name)
        self.clear_text(self.amount)
        self.input_text(amount, self.amount)
        self.click(self.add_deposit_detail)
        self.input_text(num, self.account_num)
        self.set_combox_value(dtype, self.account_type)
        if dtype == "Other":
            self.input_text(args, self.other_name)
        self.input_text(rout, self.routing_num)
        self.input_text(ramount, self.ramount)
        self.wait(2)
        self.click(self.save_btn)
        self.wait_unit_el_present(self.message)

    def show_direct_deposit(self, name):
        show_flag = (
            "xpath", "//*[@id='tblSalary']//tbody/tr[./td[2]//a[text() ='" + str(name) + "']]/td[7]/input[1]")
        self.click(show_flag)
        self.wait_unit_el_present(self.deposit_flag)
        detail_title = self.get_element(self.deposit_flag)
        if detail_title is not None:
            Log.info("Show detail direct deposit")

    def verify_deposit_detail(self):
        tabel = self.get_element(self.v_anum)
        rows = tabel.find_elements_by_tag_name("tr")
        r1 = rows[1].find_elements_by_tag_name("td")
        for i in r1:
            self.list.append(i.text.encode("utf-8"))
        self.list[-1] = float(self.list[-1])

    def delete_salary(self, name):
        delete_checkbox = (
            "xpath", "//*[@id='tblSalary']/tbody/tr[./td[2]//a[text() ='" + str(name) + "']]/td[1]")
        self.click(delete_checkbox)
        self.click(self.delete_btn)

    def add_attachment(self):
        self.click(self.add_attachment_btn)
        self.upload_file("salary.txt", self.file_path)
        self.click(self.upload_btn)

    def verify_attachment(self):
        name = self.get_element(self.file_name)
        if name is not None:
            Log.info("upload file success!")

    def delete_employee(self, employee):
        self.employeelist = EmployeeList(self.driver)
        self.employeelist.delete_employee(employee)


