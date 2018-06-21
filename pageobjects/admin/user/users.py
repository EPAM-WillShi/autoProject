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

    # Define element keys on User page: Search panel
    search_username = ("id", "searchSystemUser_userName")
    search_role = ("id", "searchSystemUser_userType")
    search_employee = ("id", "searchSystemUser_employeeName_empName")
    search_status = ("id", "searchSystemUser_status")
    search_btn = ("id", "searchBtn")
    reset_btn = ("id", "resetBtn")

    # Define element keys on User page: elements on user table panel
    user_add_btn = ("id", "btnAdd")
    user_del_btn = ("id", "btnDelete")
    username_list = ("xpath", "//table[@id='resultTable']/tbody/tr/td[2]/a")
    user_role_list = ("xpath", "//table[@id='resultTable']/tbody/tr/td[3]")
    employee_name_list = ("xpath", "//table[@id='resultTable']/tbody/tr/td[4]")
    user_status_list = ("xpath", "//table[@id='resultTable']/tbody/tr/td[5]")
    user_checkbox_xpath = "//a[contains(text(), '{}')]/../../td[1]"
    username_link_xpath = "//a[contains(text(), '{}')]/../../td[2]/a"
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

    # Define elements on Edit User panel
    user_edit_save_btn = ("id", "btnSave")
    change_password = ("id", "systemUser_chkChangePassword")

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

    def get_all_users(self):
        """
        :return a dictionary which include the username, employee name, role, status details
        """
        username_list = self.get_elements_texts(self.username_list)
        employee_name_list = self.get_elements_texts(self.employee_name_list)
        user_role_list = self.get_elements_texts(self.user_role_list)
        user_role_status = self.get_elements_texts(self.user_status_list)
        all_user_info = {"UserName": username_list, "EmployeeName": employee_name_list,
                         "UserRole": user_role_list, "UserStatus": user_role_status}
        return all_user_info

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
            Log.info("User " + username + " is not in the user list, not delete.")

    def open_user(self, username):
        """
        On Users page, click username to open a user (to go to Edit User page)
        """
        if self.check_if_user_exists(username):
            self.click(("xpath", self.username_link_xpath.format(username)))
            self.wait_unit_el_present(self.user_edit_save_btn)
        else:
            Log.info("User " + username + " is not in the user list.")

    def get_user_info(self):
        """
        On Edit User page, get the username, employee name, role and status
        """
        name = self.get_element_attribute(self.user_name_input, "value")
        role = self.get_first_select(self.user_role_select)
        employee = self.get_element_attribute(self.emp_name_input, "value")
        status = self.get_first_select(self.user_status_select)
        info = [name, employee, role, status]
        return info

    def edit_user(self, username, employee, role, status, change_pwd=False, *password):
        """
        On Edit Users page, edit an user
        """
        self.click(self.user_edit_save_btn)
        # self.wait(1)
        self.set_combox_value(role, self.user_role_select)
        self.input_text(employee, self.emp_name_input)
        self.input_text(username, self.user_name_input)
        self.set_combox_value(status, self.user_status_select)
        if change_pwd:
            self.click(self.change_password)
            self.input_text(password, self.user_password_input)
            self.input_text(password, self.user_confirm_password)
        self.click(self.user_edit_save_btn)
        self.wait_unit_el_present(self.user_table)
        Log.info("User is edited and saved.")

    def click_search(self):
        self.click(self.search_btn)

    def click_reset(self):
        self.click(self.reset_btn)

    def search_system_user(self, username="", employee="", role="All", status="All"):
        """
        On Users page, input keywords for username, employee name, role, status, then click search button to search

        """
        self.clear_text(self.search_username)
        self.input_text(username, self.search_username)
        self.clear_text(self.search_employee)
        self.input_text(employee, self.search_employee)
        self.set_combox_value(role, self.search_role)
        self.set_combox_value(status, self.search_status)
        self.click_search()
        self.wait(1)
        Log.info("Search user is done.")

    def get_search_info(self):
        """
        On User page, get the text of search input controls: username, employee name, role and status
        """
        name = self.get_element_attribute(self.search_username, "value")
        employee = self.get_element_attribute(self.search_employee, "value")
        role = self.get_first_select(self.search_role)
        status = self.get_first_select(self.search_status)
        info = [name, employee, role, status]
        return info

