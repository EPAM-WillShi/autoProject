# -*- coding: utf-8 -*-
from lib.log import Log
from pageobjects.time.time import Time


class Project(Time):
    """
    Time Project page main components
    """
    # Create a project
    add_project_btn_ele = ('ID', 'btnAdd')
    project_name_ele = ('ID', 'addProject_projectName')
    project_admin_ele = ('ID', 'addProject_projectAdmin_1')
    project_description_ele = ('ID', 'addProject_description')
    save_project_btn_ele = ('ID', 'btnSave')
    save_project_success_flag = ("XPATH", "//h1[text()='Project']")
    cancel_btn_ele = ('ID', 'btnCancel')

    # Create a customer
    add_customer_btn_ele = ('ID', 'addCustomerLink')
    customer_name_ele = ('ID', 'addCustomer_customerName')
    customer_description_ele = ('ID', 'addCustomer_description')
    save_customer_btn_ele = ('ID', 'dialogSave')

    # Add another project admin
    add_project_admin_btn_ele = ('ID', 'addButton')
    another_project_admin_ele = ('ID', 'addProject_projectAdmin_2')

    # Open a project
    project_ele_value = "//td[3]/a[text()='{}']"

    # Create an activity
    add_activity_btn_ele = ('ID', 'btnAdd')
    activity_name_ele = ('ID', 'addProjectActivity_activityName')
    save_activity_btn_ele = ('ID', 'btnActSave')
    activity_ele_value = "//td[last()]/a[text()='{}']"

    # Search projects
    search_project_admin_ele = ('ID', 'searchProject_projectAdmin')
    search_btn_ele = ('ID', 'btnSearch')
    expected_row_ele_value = "//td[last()][contains(text(),'{}')]"
    actual_row_ele = ('XPATH', '//tbody/tr')

    def __init__(self, browser):
        super(Project, self).__init__(browser)
        self.click_menu("Project Info")
        self.click_menu("Projects")
        Log.info("Arrive Time Project page")

    def click_add_btn(self):
        """
        Click Add button
        """
        self.click(self.add_project_btn_ele)

    def add_customer(self, customer_name, customer_description):
        """
        Add a customer
        """
        self.click(self.add_customer_btn_ele)
        self.clear_text(self.customer_name_ele)
        self.input_text(customer_name, self.customer_name_ele)
        self.clear_text(self.customer_description_ele)
        self.input_text(customer_description, self.customer_description_ele)
        self.click(self.save_customer_btn_ele)
        self.sleep(1)

    def add_project_admin(self, another_project_admin):
        """
        Add another project admin
        """
        self.click(self.add_project_admin_btn_ele)
        self.clear_text(self.another_project_admin_ele)
        self.input_text(another_project_admin, self.another_project_admin_ele)

    def input_project_details(self, project_name, project_admin, project_description):
        """
        Input project details
        """
        self.clear_text(self.project_name_ele)
        self.input_text(project_name, self.project_name_ele)
        self.clear_text(self.project_admin_ele)
        self.input_text(project_admin, self.project_admin_ele)
        self.clear_text(self.project_description_ele)
        self.input_text(project_description, self.project_description_ele)

    def click_save_btn(self):
        """
        Click Add button and check if Project label is show
        """
        self.click(self.save_project_btn_ele)
        project_page_name = self.wait_unit_el_present(self.save_project_success_flag)
        if project_page_name is not None:
            Log.info("New project is created successfully!")

    def click_cancel_btn(self):
        """
        Click cancel button and go back to Project page
        """
        self.click(self.cancel_btn_ele)

    def open_project(self, project_name):
        """
        Click a project to open
        """
        open_project_ele_value = self.project_ele_value.format(project_name)
        self.click(("XPATH", open_project_ele_value))

    def add_activity(self, activity_name):
        """
        Add an activity
        """
        self.click(self.add_activity_btn_ele)
        self.clear_text(self.activity_name_ele)
        self.input_text(activity_name, self.activity_name_ele)
        self.click(self.save_activity_btn_ele)

    def check_activity(self, activity_name):
        """
        Verify new activity is listed
        """
        check_activity_ele_value = self.activity_ele_value.format(activity_name)
        check_activity = self.wait_unit_el_present(("XPATH", check_activity_ele_value))
        if check_activity is not None:
            Log.info("New activity is listed.")

    def expected_search_result(self, project_admin):
        """
        Obtain expected row of search result
        """
        expected_row_ele_value = self.expected_row_ele_value.format(project_admin)
        expected_row = self.get_elements(("XPATH", expected_row_ele_value))
        return len(expected_row)

    def search_projects_by_project_admin(self, project_admin):
        """
        Search projects by project admin
        """
        self.clear_text(self.search_project_admin_ele)
        self.input_text(project_admin, self.search_project_admin_ele)
        self.click(self.search_btn_ele)

    def check_search_result(self, expected_row):
        """
        Check if actual row of search result is equal to expected row
        """
        actual_row = self.get_elements(self.actual_row_ele)
        assert len(actual_row) == expected_row
        Log.info('Search result is correct.')

    def go_back_to_project(self):
        """
        Go back to Projects page
        """
        self.click_menu("Project Info")
        self.click_menu("Projects")














