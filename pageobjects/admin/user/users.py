# coding=utf-8
"""
Created on 2018/6/11
@author: Julie Wu
"""
from pageobjects.admin.admin import Admin
from lib.log import Log
from pageobjects.pim.add_employee import AddEmployee


class Users(Admin):
    user_management_menu = ("id", "menu_admin_UserManagement")

    # Define element keys on User page: elements on user table panel
    user_add_btn = ("id", "btnAdd")
    user_del_btn = ("id", "btnDelete")
    username_list = ("xpath", "//table[@id='resultTable']/tbody/tr/td[2]/a")
    user_checkbox_xpath = "//a[contains(text(), '{}')]/../../td[1]"
    no_record_element = ("xpath", "//table[@id='resultTable']/tbody/tr/td")
    user_table = ("id", "resultTable")

    # Define element keys on Add User panel
    emp_name_input = ("id", "systemUser_employeeName_empName")
    user_name_input = ("id", "systemUser_userName")
    user_role_select = ("id", "systemUser_userType")
    user_status_select = ("id", "systemUser_status")
    user_password_input = ("id", "systemUser_password")
    user_confirm_password = ("id", "systemUser_confirmPassword")
    user_save_btn = ("id", "btnSave")
    user_cancel_btn = ("id", "btnCancel")
    add_user_form = ("id", "frmSystemUser")

    # Define elements on User Delete dialog
    dialog_del_btn = ("id", "dialogDeleteBtn")

    def __init__(self, browser):
        super(Users, self).__init__(browser)

    def add_employee(self, first_name, last_name):
        """
        Go to PIM page to add an employee with first and lats name
        """
        self.switch_main_menu("PIM")
        self.click_menu("Add Employee")
        self.pim = AddEmployee(self.driver)
        self.pim.add_user_employee(first_name, last_name)

    def open_user_page(self):
        """
        Open Admin->User Management->Users page
        """
        self.switch_main_menu("Admin")
        self.wait_unit_el_present(self.user_management_menu)
        self.click_menu("User Management")
        self.click_menu("Users")

    def check_if_user_exists(self, username):
        """
        check if the username listed in the user table， if existing then return True else return False
        """
        if username in self.get_elements_texts(self.username_list):
            return True
        else:
            return False

    def add_user(self, role, emp_name, username, status, password):
        """
        On Users page, by Add button, add a new user with role, employee name, user name, status and password
        """
        Log.info("Start to add user.")
        self.click(self.user_add_btn)
        self.wait_unit_el_present(self.add_user_form)
        self.set_combox_value(role, self.user_role_select)
        self.input_text(emp_name, self.emp_name_input)
        self.input_text(username, self.user_name_input)
        self.set_combox_value(status, self.user_status_select)
        self.input_text(password, self.user_password_input)
        self.input_text(password, self.user_confirm_password)
        self.click(self.user_save_btn)
        self.wait_unit_el_present(self.user_table)
        Log.info("New user is added.")

    def delete_user(self, username):
        """
        On Users page, by delete button, delete the selected user (this is only for single user)
        """
        Log.info("Start to delete user.")
        if self.check_if_user_exists(username):
            self.click(("xpath", self.user_checkbox_xpath.format(username)))
            self.click(self.user_del_btn)
            self.click(self.dialog_del_btn)
            self.wait_unit_el_present(self.user_table)
            Log.info("Use is deleted.")
        else:
            Log.info("User is not in the user list, not delete.")

