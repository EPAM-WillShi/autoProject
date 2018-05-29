# -*- coding: utf-8 -*-
"""
Created on 2018/4/25
@author: Molly Xue
"""

from pageobjects.mainpage import MainPage
from pageobjects.pim.add_employee import AddEmployee
from lib.log import Log

class Directory(MainPage):
    """
    Directory page main components
    """
    name = ('id', 'searchDirectory_emp_name_empName')
    jobtitle = ('id', 'searchDirectory_job_title')
    location = ('id', 'searchDirectory_location')
    searchbutton = ('id', 'searchBtn')
    resetbutton = ('id', 'resetBtn')
    resulttable = ('id', 'resultBox')
    No_records_Found = ('XPATH', ".//*[@id='content']/div[2]/div[2]")

    def __init__(self, browser):
        """
        Arrive Directory page-Search Directory
        """
        super(Directory, self).__init__(browser)
        self.switch_main_menu("Directory")
        Log.info("Arrive Directory page")

    def create_employee(self, first_name, last_name):
        """
        Go to PIM, check employee and create a new employee
        """
        self.pim = AddEmployee(self.driver)
        self.pim.delete_employee(last_name)
        self.pim.add_user_employee(first_name, last_name)

    def delete_employee(self, last_name):
        """
        Go to PIM, delete an employee
        """
        self.pim = AddEmployee(self.driver)
        self.pim.delete_employee(last_name)

    def resetDirectory(self,Name,JobTitle,Location):
        """
        Test reset name, job title and location on Search Directory
        """
        #Reset name, job title and location at one time
        self.clear_text(self.name)
        self.input_text(value=Name, keys=self.name)
        self.press_enter_key(self.name)
        self.sleep(2)
        self.set_combox_value(value=JobTitle, keys=self.jobtitle)
        self.sleep(2)
        self.set_combox_value(value=Location, keys=self.location)
        self.sleep(2)
        self.click(self.resetbutton)
        self.sleep(2)
        assert self.get_element_text(self.name) == ""
        DefaultOptionValue_jobtitle = self.get_element_attribute(self.jobtitle, "value")
        assert DefaultOptionValue_jobtitle == "0"
        DefaultOptionValue_location = self.get_element_attribute(self.location, "value")
        assert DefaultOptionValue_location == "-1"
        Log.info("Directory Page, reset name, job title and location for search directory - all passed")


    def searchDirectory_One(self,Name,JobTitle,Location):
        """
        Test search name, job title and location on Search Directory
        """
        #Search name only
        self.input_text(value=Name, keys=self.name)
        self.press_enter_key(self.name)
        self.click(self.searchbutton)
        enter_name = self.get_element_attribute(self.name, "Value")
        queryout_name = self.get_element_text(self.resulttable)
        assert enter_name in queryout_name
        Log.info("Directory Page, search name for search directory - passed")

        #Search job title only
        self.click(self.resetbutton)
        self.set_combox_value(value=JobTitle, keys=self.jobtitle)
        self.click(self.searchbutton)
        queryout_jobtitle = self.get_element_text(self.resulttable)
        assert JobTitle in queryout_jobtitle
        Log.info("Directory Page, search job title for search directory - passed")

        # Search location only
        self.click(self.resetbutton)
        self.set_combox_value(value=Location, keys=self.location)
        self.click(self.searchbutton)
        queryout_location = self.get_element_text(self.resulttable)
        location_without_gap = Location.strip()
        assert location_without_gap in queryout_location
        Log.info("Directory Page, search location for search directory - passed")

    def search_SearchDirectory_All(self, Name, JobTitle, Location):
        """
        Test search name, job title and location on Search Directory
        """
        # Search name,job title and location at one time
        self.click(self.resetbutton)
        self.input_text(value=Name, keys=self.name)
        self.press_enter_key(self.name)
        self.sleep(2)
        self.set_combox_value(value=JobTitle, keys=self.jobtitle)
        self.sleep(2)
        self.set_combox_value(value=Location, keys=self.location)
        self.sleep(2)
        self.click(self.searchbutton)
        self.driver.implicitly_wait(5)
        enter_name = self.get_element_attribute(self.name, "Value")
        queryout_name = self.get_element_text(self.resulttable)
        assert enter_name in queryout_name
        queryout_jobtitle = self.get_element_text(self.resulttable)
        assert JobTitle in queryout_jobtitle
        queryout_location = self.get_element_text(self.resulttable)
        location_without_gap = Location.strip()
        assert location_without_gap in queryout_location
        Log.info("Directory Page, search name, title, location for search directory - passed")

    def search_SearchDirectory_No(self, Name, JobTitle, Location):
        """
        Test search name, job title and location on Search Directory
        """
        self.click(self.resetbutton)
        self.input_text(value=Name, keys=self.name)
        self.press_enter_key(self.name)
        self.sleep(2)
        self.set_combox_value(value=JobTitle, keys=self.jobtitle)
        self.sleep(2)
        self.set_combox_value(value=Location, keys=self.location)
        self.sleep(2)
        self.click(self.searchbutton)
        self.driver.implicitly_wait(5)
        self.is_element_visible(xpath=self.No_records_Found)
        queryout_info = self.get_element_text(self.No_records_Found)
        assert queryout_info == "No Records Found"
        Log.info("Directory Page, search name, job title and location, no records found - passed")