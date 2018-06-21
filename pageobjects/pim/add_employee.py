# -*- coding: utf-8 -*-
import os
from lib.log import Log
from pageobjects.pim.pim import PIM


class AddEmployee(PIM):
    """
    PIM Add employee page main components
    """
    # Create an employee
    employee_menu = ("ID", "menu_pim_addEmployee")
    emp_firstname_field = ("ID", "firstName")
    emp_lastname_field = ("ID", "lastName")
    employee_save_btn = ("ID", "btnSave")
    first_name_ele = ('ID', 'firstName')
    middle_name_ele = ('ID', 'middleName')
    last_name_ele = ('ID', 'lastName')
    upload_file_ele = ('ID', 'photofile')
    save_btn_ele = ('ID', 'btnSave')
    save_employee_success_flag = ("XPATH", "//h1[text()='Personal Details']")
    check_login_btn_ele = ('ID', 'chkLogin')
    login_name_ele = ('ID', 'user_name')
    login_password_ele = ('ID', 'user_password')
    confirm_password_ele = ('ID', 're_password')
    user_status_ele = ('ID', 'status')
    employee_id_ele = ('ID', 'employeeId')

    # Check new employee
    check_employee_id_ele = ('ID', 'personal_txtEmployeeId')
    check_first_name_ele = ('ID', 'personal_txtEmpFirstName')
    check_middle_name_ele = ('ID', 'personal_txtEmpMiddleName')
    check_last_name_ele = ('ID', 'personal_txtEmpLastName')

    # Delete employees
    get_total_row_ele = ("XPATH", "//tr")
    name_ele_value = "//tr[{}]/td[4]"
    check_name_ele_value = "//tr[{}]/td[1]"
    delete_btn_ele = ('ID', 'btnDelete')
    ok_btn_ele = ('ID', 'dialogDeleteBtn')

    def __init__(self, browser):
        super(AddEmployee, self).__init__(browser)
        self.click_menu("Add Employee")
        Log.info("Arrive PIM Add Employee page")

    def add_user_employee(self, firstname, lastname):
        """
        Add employee:
        1. input first name and last name
        2. get employee id
        3. click save button
        """
        Log.info("Add employee record")
        self.input_text(firstname, self.emp_firstname_field)
        self.input_text(lastname, self.emp_lastname_field)
        self.click(self.employee_save_btn)
        Log.info("New Employee Added")

    def input_employee_details(self, first_name, middle_name, last_name, upload_file):
        """
        Input all fields: First Name/Middle Name/Last Name/Attached the Photograph
        """
        self.input_text(first_name, self.first_name_ele)
        self.input_text(middle_name, self.middle_name_ele)
        self.input_text(last_name, self.last_name_ele)
        self.upload_file(upload_file, self.upload_file_ele)

    def input_login_details(self, login_name, login_password, confirm_password, user_status):
        """
        Check 'create login details' box and input login details: User name/Password/Confirm Password/Status(Enable)
        """
        self.click(self.check_login_btn_ele)
        self.input_text(login_name, self.login_name_ele)
        self.input_text(login_password, self.login_password_ele)
        self.input_text(confirm_password, self.confirm_password_ele)
        self.set_combox_value(user_status, self.user_status_ele)

    def get_employee_id_add_page(self):
        """
        Obtain employee id in Add Employee page
        """
        employee_id = self.get_element_attribute(self.employee_id_ele, "value")
        return employee_id

    def save_employee(self):
        """
        Click Save button if Personal Details label is show
        """
        self.click(self.save_btn_ele)
        page_name = self.wait_unit_el_present(self.save_employee_success_flag)
        if page_name is not None:
            Log.info("New employee is created successfully!")

    def check_employee_details(self, first_name, middle_name, last_name, employee_id):
        """
        On 'Personal Details' page, check if all the values (Names, employeeID) are equal to what you just add
        """
        assert self.get_element_attribute(self.check_employee_id_ele, "value") == employee_id
        Log.info('Employee id is correct.')
        assert self.get_element_attribute(self.check_first_name_ele, "value") == first_name
        Log.info('First name is correct.')
        assert self.get_element_attribute(self.check_middle_name_ele, "value") == middle_name
        Log.info('Middle name is correct.')
        assert self.get_element_attribute(self.check_last_name_ele, "value") == last_name
        Log.info('Last name is correct')

    def log_out_btn(self):
        """
        Logout
        """
        self.log_out()

    def go_back_to_add_employee(self):
        """
        Go back to Add Employee page.
        """
        self.click_menu("Add Employee")

    def check_employee_checkbox(self, last_name):
        """
        Select employee
        """
        rows = self.get_elements(self.get_total_row_ele)  # Obtain all rows
        for row in range(1, len(rows)):
            get_name_ele_value = self.name_ele_value.format(row)
            name = self.get_element_text(("XPATH", get_name_ele_value))  # Obtain employee name of this row.
            if name == last_name:  # If obtained employee name is equal to last_name, check the user's checkbox.
                check_employee_ele_value = self.check_name_ele_value.format(row)
                self.click(("XPATH", check_employee_ele_value))
            else:  # If obtained employee name is not equal to last_name, check the next name.
                row += 1

    def delete_employee(self, last_name):
        """
        Delete all employees with last name which you will create
        """
        self.click_menu("Employee List")
        try:
            self.check_employee_checkbox(last_name)
            self.click(self.delete_btn_ele)
            self.click(self.ok_btn_ele)
            Log.info("All employees with last name: %s are listed!" % last_name)
        except Exception:
            Log.info("No employee with last name: %s is listed!" % last_name)
        self.click_menu("Add Employee")


