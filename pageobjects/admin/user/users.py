# coding=utf-8

from pageobjects.admin.admin import Admin
from lib.log import Log
from pageobjects.pim.add_employee import AddEmployee


class Users(Admin):

    """
    User page main components
    """
    user_add_btn = ("ID", "btnAdd")
    user_role_field = ("ID", "systemUser_userType")
    user_employee_name_field = ("ID", "systemUser_employeeName_empName")
    user_name_field = ("ID", "systemUser_userName")
    user_status_field = ("ID", "systemUser_status")
    user_pwd_field = ("ID", "systemUser_password")
    user_confirm_pwd_field = ("ID", "systemUser_confirmPassword")
    user_save_btn = ("ID", "btnSave")
    user_search_field = ("ID", "searchSystemUser_userName")
    user_search_btn = ("ID", "searchBtn")
    user_reset_btn = ("ID", "resetBtn")
    user_delete_btn = ("ID", "btnDelete")
    dialog_delete_btn = ('ID', 'dialogDeleteBtn')
    delete_record = ("xpath", "//a[contains(text(),'dorothy_012345')]/../../td[1]/input")
    user_names = ("xpath", "//tbody/tr/td[2]/a")
    search_flag = ('link_text', 'dorothy_012345')
    success_flag = ("xpath", "//*[@class='message success fadable']")
    search_name = None
    edit_record = ('link_text', 'test1')
    user_edit_btn = ("ID", "btnSave")
    search_link_text = "{}"
    delete_tr = "//*[text()='{}']/../../td[1]"

    def __init__(self, browser):
        super(Users, self).__init__(browser)

    def create_employee(self, first_name, last_name):
        """
        Go to PIM, check employee and create a new employee
        """
        self.pim = AddEmployee(self.driver)
        self.sleep(3)
        self.pim.add_user_employee(first_name, last_name)
        Log.info("Arrive Add Employee page")

    def switch_menu(self):
        """
        Back to Users page
        """
        self.click_menu("Admin")
        self.click_menu("User Management")
        self.click_menu("Users")
        Log.info("Arrive System Users page")

    def check_if_user_exist(self, uname):
        """
        Check if user exist
        """
        names = self.get_elements_texts(self.user_names)
        for name in names:
            if uname == name:
                return uname
                break
        return None

    def add_user(self, user_role, employee_name, user_name, user_status, user_password):
        """
        Add user
        """
        Log.info("Start to add user")
        check_user_name = self.check_if_user_exist(user_name)
        if check_user_name is None:
            self.click(self.user_add_btn)
            self.set_combox_value(user_role, self.user_role_field)
            self.clear_text(self.user_employee_name_field)
            self.input_text(employee_name, self.user_employee_name_field)
            self.clear_text(self.user_name_field)
            self.input_text(user_name, self.user_name_field)
            self.set_combox_value(user_status, self.user_status_field)
            self.clear_text(self.user_pwd_field)
            self.input_text(user_password, self.user_pwd_field)
            self.clear_text(self.user_confirm_pwd_field)
            self.input_text(user_password, self.user_confirm_pwd_field)
            self.sleep(2)
            self.click(self.user_save_btn)
            assert "Successfully Saved" in self.get_element_text(self.success_flag)

    def search_user(self, user_name):
        """
        search user record
        """
        Log.info("Start to search user")
        self.clear_text(self.user_search_field)
        self.sleep(3)
        self.input_text(user_name, self.user_search_field)
        self.sleep(3)
        self.click(self.user_search_btn)
        self.sleep(3)
        self.search_name = self.get_element_text(self.search_flag)
        return self.search_name

    def delete_user(self, deleted_user_name):
        """
        delete user
        """
        Log.info("Start to delete user")
        check_user_name = self.check_if_user_exist(deleted_user_name)
        if check_user_name == deleted_user_name:
            self.click(self.delete_record)
            self.sleep(3)
            self.click(self.user_delete_btn)
            self.sleep(3)
            self.click(self.dialog_delete_btn)
            assert "Successfully Deleted" in self.get_element_text(self.success_flag)
            Log.info("Records are deleted Successfully!")

    def edit_users(self, edit_name):
        """
        edit user
        """
        Log.info("Start to edit user")
        self.click(self.edit_record)
        self.sleep(3)
        self.click(self.user_edit_btn)
        self.clear_text(self.user_name_field)
        self.input_text(edit_name, self.user_name_field)
        self.sleep(3)
        self.click(self.user_edit_btn)
        assert "Successfully Updated" in self.get_element_text(self.success_flag)
        Log.info("Edit Successfully")

    def update_user(self, user_name_value, updated_user_name):
        """
        update searched record
        """
        self.click(["LINK_TEXT", self.search_link_text.format(user_name_value)])
        self.click(self.user_edit_btn)
        self.clear_text(self.user_name_field)
        self.input_text(updated_user_name, self.user_name_field)
        self.click(self.user_edit_btn)
        assert self.get_element_text(["LINK_TEXT", self.search_link_text.format(updated_user_name)]) is not None

    def search(self, user_name):
        """
        search user record
        """
        Log.info("search user")
        self.clear_text(self.user_search_field)
        self.input_text(user_name, self.user_search_field)
        self.click(self.user_search_btn)
        assert self.get_element_text(["LINK_TEXT", self.search_link_text.format(user_name)]) is not None

    def delete(self, update_user_name):
        """
        Delete user
        """

        Log.info("Start To Delete")
        tr = ("XPATH", self.delete_tr.format(update_user_name))
        self.click(tr)
        self.click(self.user_delete_btn)
        self.click(self.dialog_delete_btn)
        assert self.get_element_text(["LINK_TEXT", self.search_link_text.format(update_user_name)]) is None
        Log.info("Delete Successfully")
