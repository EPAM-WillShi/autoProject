# -*- coding: utf-8 -*-
"""
Created on 2018/6/4
@author: Yolanda Zhang
"""

from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.pim.config.reporting_methods import Report_method


class Reportto(EmployeeList):
    """
    PIM Add employee page main components
    """
    success_flag = ('xpath', '//h1[text()="Assigned Supervisors"]')
    no_record_flag = ('xpath', "//td[text() = 'No Records Found']")

    add_supervisor_btn = ('id', 'btnAddSupervisorDetail')
    delete_supervisor_btn = ('id',"delSupBtn")
    supervisor_name = ('id',"reportto_supervisorName_empName")
    report_method = ('id','reportto_reportingMethodType')
    save_btn = ('id','btnSaveReportTo')
    cancel_btn = ('id',"btnCancel")
    act_rep_method = "//a[text()='{}']/../../td[3]"
    delete_checkbox = "//a[text()='{}']/../../td[1]"

    check_box = "//a[text()='{}']/../../td[1]"

    message = ('xpath', "//div[contains(@class,'success')]")

    add_subordinate_btn = ('id',"btnAddSubordinateDetail")
    delete_subordinate_btn = ('id', "delSubBtn")
    subordinate_name = ('id',"reportto_subordinateName_empName")
    specify = ('id',"reportto_reportingMethod")

    add_attachment_btn = ('id', 'btnAddAttachment')
    delete_attachment_btn = ('id', 'btnDeleteAttachment')
    file_path = ('id', 'ufile')
    upload_btn = ('id', 'btnSaveAttachment')
    file_name = "//a[normalize-space(text())='{}']"
    delete_attachment_checkbox = "//a[normalize-space(text())='{}']/../preceding-sibling::td"


    def __init__(self, browser):
        super(Reportto, self).__init__(browser)
        self.click_menu("Employee List")
        Log.info("Arrive Employee list page")

    def open_report_page_via_creating_emp(self, fname, lname):
        self.add_employee(fname, lname)
        self.switch_employee_detail_page("Report-to")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive report-to page!")

    def search_emp_report(self, fname, lname):
        self.query_employee_by_name(fname + ' ' + lname)
        self.click_employee_to_edit(fname, lname)
        self.switch_employee_detail_page("Report-to")
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive report-to page!")

    def add_assigned_supervisors(self, name, method):
        self.click(self.add_supervisor_btn)
        self.input_text(name, self.supervisor_name)
        self.set_combox_value(method, self.report_method)
        self.click(self.save_btn)
        Log.info("Add assigned supervisors successfully!")

    # def verify_added_supervisor(self,fname, lname):
    #     self.query_employee_by_name(fname + ' ' + lname)
    #     #########

    def cancel_add_supervisors(self, name):
        self.click(self.add_supervisor_btn)
        self.input_text(name , self.supervisor_name)
        self.wait(2)
        self.click(self.cancel_btn)
        Log.info("Cancel add assigned supervisors!")

    def edit_added_supervisors(self, name, method):
        self.click(('link_text', name))
        self.wait(2)
        self.set_combox_value(method,self.report_method)
        self.click(self.save_btn)
        Log.info("Edit added record!")

    def verify_edit_actual_result(self, name, method,*args ):
        act_value = self.act_rep_method.format(name)
        ielement = ('XPATH', act_value)
        act_result = self.get_element_text(ielement)
        if method == "Other":
            assert act_result ==args[0]
        else:
            assert act_result == method
        Log.info("Edited report method, actual result is equal to expected result.")

    def delete_supervisor(self, name):
        act_value = self.delete_checkbox.format(name)
        ielement = ('XPATH', act_value)
        self.click(ielement)
        self.click(self.delete_supervisor_btn)
        Log.info("Delete added supervisor!")

    def add_subordinates(self, name, method):
        self.click(self.add_subordinate_btn)
        self.input_text(name, self.subordinate_name)
        self.set_combox_value(method, self.report_method)
        self.click(self.save_btn)
        Log.info("Add subordinates successfully!")

    def cancel_add_subordinates(self,name):
        self.click(self.add_subordinate_btn)
        self.input_text(name, self.subordinate_name)
        self.click(self.cancel_btn)
        Log.info("Cancel add subordinate!")

    def edit_added_subordinates(self, name, method, *args):
        self.click(('link_text', name))
        self.wait(2)
        self.set_combox_value(method,self.report_method)
        if method == "Other":
            self.input_text(args, self.specify)
        self.click(self.save_btn)
        Log.info("Edit added subordinate!")

    def delete_subordinates(self,name):
        act_value = self.delete_checkbox.format(name)
        ielement = ('XPATH', act_value)
        self.click(ielement)
        self.click(self.delete_subordinate_btn)
        Log.info("Delete added subordinate!")

    def add_attachment(self, document):
        self.click(self.add_attachment_btn)
        self.upload_file(document, self.file_path)
        self.click(self.upload_btn)
        Log.info("Add attachment for report-to successfully!")

    def verify_attachment(self, document):
        attachment = self.file_name.format(document)
        name = self.get_element(('xpath',attachment))
        if name is not None:
            Log.info("upload file success!")
        else:
            Log.info("uploaded file is not existed!")

    def delete_attachment(self, document):
        attachment = self.delete_attachment_checkbox.format(document)
        self.click(('xpath', attachment))
        self.click(self.delete_attachment_btn)
        Log.info("The attachment is deleted.")

    def add_employee(self, first_name, last_name):
        self.employeelist = EmployeeList(self.driver)
        self.employeelist.add_employee(first_name, last_name)

    def delete_employee(self, employee):
        self.employeelist = EmployeeList(self.driver)
        self.employeelist.delete_employee(employee)

    def delete_report_method(self, name):
        self.repmethod = Report_method(self.driver)
        self.repmethod.delete_report_method(name)

