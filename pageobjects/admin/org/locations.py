# -*- coding: utf-8 -*-
"""
Created on 2018/6/14
@author: Joanna Li
"""
import random
from lib.log import Log
from pageobjects.admin.admin import Admin
class Location(Admin):
    """
    Structure page
    """
    # Organization location main page objects
    add_btn = ("ID", "btnAdd")
    delete_btn = ("ID", "btnDelete")
    result_table = "//table[@id='resultTable']/tbody"
    #Search objects
    search_btn = ("ID", "btnSearch")
    reset_btn = ("ID", "btnReset")
    location_name = ("ID", "searchLocation_name")
    location_city = ("ID", "searchLocation_city")
    location_country = ("ID", "searchLocation_country")
    name_link = "//a[text()='{}']"
    city_path = "//a[text()='{}']/../following-sibling::td[1]"
    country_path = "//a[text()='{}']/../following-sibling::td[2]"
    phone_path = "//a[text()='{}']/../following-sibling::td[3]"
    del_path = "//a[text()='{}']/../../td[1]/input"
    #Add objects
    add_location_name = ("ID", "location_name")
    add_location_country = ("ID", "location_country")
    add_location_province = ("ID", "location_province")
    add_location_city = ("ID", "location_city")
    add_location_address = ("ID", "location_address")
    add_location_zipCode = ("ID", "location_zipCode")
    add_location_phone = ("ID", "location_phone")
    add_location_fax = ("ID", "location_fax")
    add_location_notes = ("ID", "location_notes")
    save_btn = ("ID", "btnSave")
    name_exist_text = ("xpath", "//span[@class='validation-error']")
    exist_message = "Already exists"
    cancle_btn = ("ID", "btnCancel")
    # Delete objects
    ok_btn = ("ID", "dialogDeleteBtn")

    def __init__(self, browser):
        super(Location, self).__init__(browser)
        self.click_menu("Organization")
        self.click_menu("Locations")
        self.wait_unit_el_present(("xpath", self.result_table))
        Log.info("Arrive at location page")

    def add_location(self, name, province, city, address, zip, phone, fax, notes):
        Log.info("Start to add a location")
        self.sleep(3)
        is_exist = self.check_name_exists(name)
        self.click(self.add_btn)
        self.input_location(name, province, city, address, zip, phone, fax, notes)
        country = self.get_first_select(self.add_location_country)
        self.click(self.save_btn)
        if is_exist:
            assert self.get_element(self.name_exist_text).text == self.exist_message
            self.click(self.cancle_btn)
            Log.info("The location name has already exist, adding cancelled")
        else:
            self.sleep(3)
            self.verify_fields_in_table(name, city, country, phone)
            Log.info("The location is added successfully")

    def input_location(self, name, province, city, address, zip, phone, fax, notes):
        self.input_text(name, self.add_location_name)
        self.select_option_country()
        self.input_text(province, self.add_location_province)
        self.input_text(city, self.add_location_city)
        self.input_text(address, self.add_location_address)
        self.input_text(zip, self.add_location_zipCode)
        self.input_text(phone, self.add_location_phone)
        self.input_text(fax, self.add_location_fax)
        self.input_text(notes, self.add_location_notes)

    def check_name_exists(self, loc_name):
        Log.info("Start to verify if the location name already exist")
        is_exist = False
        if self.get_element(("xpath", self.name_link.format(loc_name))) is not None:
            is_exist = True
        return is_exist

    def verify_fields_in_table(self, name, city, country, phone):
        Log.info("Start to verify if all input fileds show in table correctly")
        assert self.get_element(("xpath", self.name_link.format(name))) is not None
        city_text = self.get_element(("xpath", self.city_path.format(name))).text
        country_text = self.get_element(("xpath", self.country_path.format(name))).text
        phone_text = self.get_element(("xpath", self.phone_path.format(name))).text
        assert city_text == city
        assert country_text == country
        assert phone_text == phone

    def select_option_country(self):
        Log.info("Start to select an option in country dropdown")
        toloptions = self.get_element(self.add_location_country).find_elements_by_tag_name("option")
        tolcount = len(toloptions)
        i = random.randint(0, tolcount - 1)
        self.select_option(self.add_location_country, i)

    def delete_location(self):
        Log.info("Start to delete a location randomly")
        self.sleep(3)
        roweles = self.get_element(("xpath",self.result_table)).find_elements_by_tag_name("a")
        rowcount = len(roweles)
        i = random.randint(0, rowcount - 1)
        name_text = roweles[i].text
        self.click(("xpath", self.del_path.format(name_text)))
        self.sleep(2)
        self.click(self.delete_btn)
        self.click(self.ok_btn)
        assert self.get_element(("xpath", self.name_link.format(name_text))) is None

    def edit_location(self, name, province, city, address, zip, phone, fax, notes):
        Log.info("Start to edit a location randomly")
        self.sleep(3)
        is_exist = self.check_name_exists(name)
        roweles = self.get_element(("xpath", self.result_table)).find_elements_by_tag_name("a")
        rowcount = len(roweles)
        i = random.randint(0, rowcount - 1)
        name_text = roweles[i].text
        self.click(("xpath", self.name_link.format(name_text)))
        self.click(self.save_btn)
        self.input_location(name, province, city, address, zip, phone, fax, notes)
        country = self.get_first_select(self.add_location_country)
        self.click(self.save_btn)
        if is_exist:
            assert self.get_element(self.name_exist_text).text == self.exist_message
            self.click(self.cancle_btn)
            Log.info("The location name has already exist, editing cancelled")
        else:
            self.sleep(3)
            self.verify_fields_in_table(name, city, country, phone)
            Log.info("The location is edited successfully")










