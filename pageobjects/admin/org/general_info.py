# -*- coding: utf-8 -*-
"""
Created on 2018/6/13
@author: Molly Xue
"""

import re
from pageobjects.admin.admin import Admin
from lib.log import Log
from string import letters, digits
from random import choice

class GeneralInformation(Admin):
    """
    General Information page
    """
    # Define declaration for General Information page
    edit_btn = ('ID', 'btnSaveGenInfo')
    save_btn = ('ID', 'btnSaveGenInfo')
    organization_name = ('ID', 'organization_name')
    check_org_name = ('xpath', "//span[@for='organization_name']")

    number_of_employees = ('ID', 'numOfEmployees')
    tax_id = ('ID', 'organization_taxId')
    registration_number = ('ID', 'organization_registraionNumber')
    phone = ('ID', 'organization_phone')
    check_phone = ('xpath', "//span[@for='organization_phone']")

    fax = ('ID', 'organization_fax')
    check_fax = ('xpath', "//span[@for='organization_fax']")

    email = ('ID', 'organization_email')
    check_email = ('xpath', "//span[@for='organization_email']")

    address_street_1 = ('ID', 'organization_street1')
    address_street_2 = ('ID', 'organization_street2')
    city = ('ID', 'organization_city')
    state_province = ('ID', 'organization_province')
    zip_postal_code = ('ID', 'organization_zipCode')
    country = ('ID', 'organization_country')
    note = ('ID', 'organization_note')
    check_note = ('xpath', "//span[@for='organization_note']")

    success_flag = ("xpath", "//*[@class='message success fadable']")


    def __init__(self,browser):
        super(GeneralInformation, self).__init__(browser)
        self.click_menu("Organization")
        self.click_menu("General Information")
        Log.info("Arrive Admin -> Organization: General Information page")


    def edit_general_inf(self):
        """
        Click Edit button to enable the Generation information
        """
        self.click(self.edit_btn)


    def save_general_inf(self):
        """
        Click save button to save the edit generation information
        """
        self.click(self.save_btn)


    def check_if_edit_success(self):
        """
        Test to check edit successfully flag
        """
        assert "Successfully Saved" in self.get_element_text(self.success_flag)


    def check_organization_name_length(self, org_name):
        """
        Test to check organization name allow length and null not allowed
        """
        if len(org_name) == 0:
            self.input_text(org_name, self.organization_name)
            self.press_enter_key(self.organization_name)
            invalid_flag = self.get_element_text(self.check_org_name)
            assert "Required" in invalid_flag
            Log.info("Input null as organization name is not allowed")
        elif len(org_name) > 100:
            self.input_text(org_name, self.organization_name)
            self.press_enter_key(self.organization_name)
            dis_org_name = self.get_element_attribute(self.organization_name, 'value')
            assert len(dis_org_name) == 100
            assert dis_org_name in org_name
            Log.info("Only keep the first 100 characters input as organization name")
        else:
            self.input_text(org_name, self.organization_name)
            self.press_enter_key(self.organization_name)
            dis_org_name = self.get_element_attribute(self.organization_name, 'value')
            assert dis_org_name == org_name
            Log.info("Less than or equal to 100 characters allowed input as organization name")


    def check_tax_id_length(self, tax_id):
        """
        Test to check tax id allowed length
        """
        if len(tax_id) > 30:
            self.input_text(tax_id, self.tax_id)
            self.press_enter_key(self.tax_id)
            dis_tax_id = self.get_element_attribute(self.tax_id, 'value')
            assert len(dis_tax_id) == 30
            assert dis_tax_id in tax_id
            Log.info("Only keep the first 30 characters input as tax id")
        else:
            self.input_text(tax_id, self.tax_id)
            self.press_enter_key(self.tax_id)
            dis_tax_id = self.get_element_attribute(self.tax_id, 'value')
            assert dis_tax_id == tax_id
            Log.info("Less than or equal to 30 characters allowed input as tax id")


    def check_registration_number_length(self, reg_num):
        """
        Test to check for registration number text field allow length
        """
        if len(reg_num) > 30:
            self.input_text(reg_num, self.registration_number)
            self.press_enter_key(self.registration_number)
            dis_reg_num = self.get_element_attribute(self.registration_number, 'value')
            assert len(dis_reg_num) == 30
            assert dis_reg_num in reg_num
            Log.info("Only keep the first 30 characters input as registration number")
        else:
            self.input_text(reg_num, self.registration_number)
            self.press_enter_key(self.registration_number)
            dis_reg_num = self.get_element_attribute(self.registration_number, 'value')
            assert dis_reg_num == reg_num
            Log.info("Less than or equal to 30 characters allowed input as registration number")


    def is_symbols(self, s):
        """
        Test to check the input string only contains symbols as 0123456789-+()
        """
        symbols = '0123456789-+()'
        for i in s:
            if i not in symbols:
                return False
            return True


    def check_phone_valid(self, phone):
        """
        Test to check the phone text field
        """
        if len(phone) == 0:
            self.input_text(phone, self.phone)
            self.press_enter_key(self.phone)
            Log.info("You can input null for phone")
        elif 0 < len(phone) <= 30:
            check_phone_valid = self.is_symbols(phone)
            if check_phone_valid == False:
                self.input_text(phone, self.phone)
                self.press_enter_key(self.phone)
                invalid_flag = self.get_element_text(self.check_phone)
                assert "Allows numbers and only + - / ( )" in invalid_flag
                Log.info("Only allow numbers and + - / () input as phone")
                self.clear_text(self.phone)
            else:
                self.input_text(phone, self.phone)
                self.press_enter_key(self.phone)
                dis_phone = self.get_element_attribute(self.phone, 'value')
                assert dis_phone == phone
                Log.info("Less than or equal to 30 numbers allowed input as phone")
        else:
            first_phone = phone[0:30]
            check_phone_valid = self.is_symbols(first_phone)
            if check_phone_valid == False:
                self.input_text(phone, self.phone)
                self.press_enter_key(self.phone)
                invalid_flag = self.get_element_text(self.check_phone)
                assert "Allows numbers and only + - / ( )" in invalid_flag
                Log.info("Only allow numbers and + - / () input as phone")
                self.clear_text(self.phone)
            else:
                self.input_text(phone, self.phone)
                self.press_enter_key(self.phone)
                dis_phone = self.get_element_attribute(self.phone, 'value')
                assert dis_phone in phone
                Log.info("Only allow first 30 numbers allowed input as phone")


    def check_fax_valid(self, fax):
        """
        Test to check the fax field
        """
        if len(fax) == 0:
            self.input_text(fax, self.fax)
            self.press_enter_key(self.fax)
            Log.info("You can input null for fax")
        elif 0 < len(fax) <= 30:
            check_fax_valid = self.is_symbols(fax)
            if check_fax_valid == False:
                self.input_text(fax, self.fax)
                self.press_enter_key(self.fax)
                invalid_flag = self.get_element_text(self.check_fax)
                assert "Allows numbers and only + - / ( )" in invalid_flag
                Log.info("Only allow numbers and + - / () input as fax")
                self.clear_text(self.fax)
            else:
                self.input_text(fax, self.fax)
                self.press_enter_key(self.fax)
                dis_fax = self.get_element_attribute(self.fax, 'value')
                assert dis_fax == fax
                Log.info("Less than or equal to 30 numbers allowed input as fax")
        else:
            first_fax = fax[0:30]
            check_fax_valid = self.is_symbols(first_fax)
            if check_fax_valid == False:
                self.input_text(fax, self.fax)
                self.press_enter_key(self.fax)
                invalid_flag = self.get_element_text(self.check_fax)
                assert "Allows numbers and only + - / ( )" in invalid_flag
                Log.info("Only allow numbers and + - / () input as fax")
                self.clear_text(self.fax)
            else:
                self.input_text(fax, self.fax)
                self.press_enter_key(self.fax)
                dis_fax = self.get_element_attribute(self.fax, 'value')
                assert dis_fax in fax
                Log.info("Only allow first 30 numbers allowed input as fax")


    def is_email_format(self, email):
        """
        Test to check input string as email format: xxx@xxx.com
        """
        if len(email) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                return True
        return False


    def check_email_valid(self, email):
        """
        Test to check Email text field
        """
        if len(email) == 0:
            self.input_text(email, self.email)
            self.press_enter_key(self.email)
            Log.info("You can input null for email")
        elif 0 < len(email) < 7:
            self.input_text(email, self.email)
            self.press_enter_key(self.email)
            self.clear_text(self.email)
            Log.info("email length less than is not a valid email format")
        elif 7 <= len(email) <= 30:
            check_email_valid = self.is_email_format(email)
            if check_email_valid == False:
                self.input_text(email, self.email)
                self.click(self.save_btn)
                invalid_flag = self.get_element_text(self.check_email)
                assert "Expected format: admin@example.com" in invalid_flag
                Log.info("Only expected format: admin@example.com input as email")
                self.press_enter_key(self.email)
                self.clear_text(self.email)
            else:
                self.input_text(email, self.email)
                self.press_enter_key(self.email)
                dis_email = self.get_element_attribute(self.email, 'value')
                assert dis_email == email
                Log.info("Email format and less than or equal to 30 characters allowed input as email")
        else:
            first_email = email[0:30]
            check_email_valid = self.is_email_format(first_email)
            if check_email_valid == False:
                self.input_text(email, self.email)
                self.click(self.save_btn)
                invalid_flag = self.get_element_text(self.check_email)
                assert "Expected format: admin@example.com" in invalid_flag
                Log.info("Only expected format: admin@example.com input as email")
                self.press_enter_key(self.email)
                self.clear_text(self.email)
            else:
                self.input_text(email, self.email)
                self.press_enter_key(self.email)
                dis_email = self.get_element_attribute(self.email, 'value')
                assert dis_email == email
                Log.info("Email format and less than or equal to 30 characters allowed input as email")

    def check_address_Street1_length(self, street_address):
        """
        Test to check address street allowed length
        """
        if len(street_address) > 100:
            self.input_text(street_address, self.address_street_1)
            self.press_enter_key(self.address_street_1)
            dis_street_address = self.get_element_attribute(self.address_street_1, 'value')
            assert len(dis_street_address) == 100
            assert dis_street_address in street_address
            Log.info("Only keep the first 100 characters input as Address Street 1")
        else:
            self.input_text(street_address, self.address_street_1)
            self.press_enter_key(self.address_street_1)
            dis_street_address = self.get_element_attribute(self.address_street_1, 'value')
            assert street_address == dis_street_address
            Log.info("Less than or equal to 100 characters allowed input as Address Street 1")

    def check_address_Street2_length(self, street_address):
        """
        Test to check address street allowed length
        """
        if len(street_address) > 100:
            self.input_text(street_address, self.address_street_2)
            self.press_enter_key(self.address_street_2)
            dis_street_address = self.get_element_attribute(self.address_street_2, 'value')
            assert len(dis_street_address) == 100
            assert dis_street_address in street_address
            Log.info("Only keep the first 100 characters input as Address Street 2")
        else:
            self.input_text(street_address, self.address_street_2)
            self.press_enter_key(self.address_street_2)
            dis_street_address = self.get_element_attribute(self.address_street_2, 'value')
            assert street_address == dis_street_address
            Log.info("Less than or equal to 100 characters allowed input as Address Street 2")

    def check_city_length(self, city):
        """
        Check City text field
        """
        if len(city) > 30:
            self.input_text(city, self.city)
            self.press_enter_key(self.city)
            dis_city = self.get_element_attribute(self.city, 'value')
            assert len(dis_city) == 30
            assert dis_city in city
            Log.info("Only keep the first 30 characters input as city")
        else:
            self.input_text(city, self.city)
            self.press_enter_key(self.city)
            dis_city = self.get_element_attribute(self.city, 'value')
            assert dis_city == city
            Log.info("Less than or equal to 30 characters allowed input as city")

    def check_state_province(self, state_province):
        if len(state_province) > 30:
            self.input_text(state_province, self.state_province)
            self.press_enter_key(self.state_province)
            dis_state_province = self.get_element_attribute(self.state_province, 'value')
            assert len(dis_state_province) == 30
            assert dis_state_province in state_province
            Log.info("Only keep the first 30 characters input as state/province")
        else:
            self.input_text(state_province, self.state_province)
            self.press_enter_key(self.state_province)
            dis_state_province = self.get_element_attribute(self.state_province, 'value')
            assert dis_state_province == state_province
            Log.info("Less than or equal to 30 characters allowed input as state/province")

    def check_zip_postal_code(self, zip_postal_code):
        if len(zip_postal_code) > 30:
            self.input_text(zip_postal_code, self.zip_postal_code)
            self.press_enter_key(self.zip_postal_code)
            dis_zip_postal_code = self.get_element_attribute(self.zip_postal_code, 'value')
            assert len(dis_zip_postal_code) == 30
            assert dis_zip_postal_code in zip_postal_code
            Log.info("Only keep the first 30 characters input as zip/postal code")
        else:
            self.input_text(zip_postal_code, self.zip_postal_code)
            self.press_enter_key(self.zip_postal_code)
            dis_zip_postal_code = self.get_element_attribute(self.zip_postal_code, 'value')
            assert dis_zip_postal_code == zip_postal_code
            Log.info("Less than or equal to 30 characters allowed input as zip/postal code")

    def generate_str(self, x):
        ss1 = ''
        ss = letters + digits
        for i in range(x):
            add_ss = choice(ss)
            ss1 += add_ss
            i += 1
        return ss1

    def check_note_length(self, note):
        if len(note) >= 250:
            self.input_text(note, self.note)
            self.press_enter_key(self.note)
            invalid_flag = self.get_element_text(self.check_note)
            assert "Should be less than 250 characters" in invalid_flag
            allow_note = note[0: 250]
            self.input_text(allow_note, self.note)
            self.press_enter_key(self.note)
            dis_note = self.get_element_attribute(self.note, 'value')
            assert cmp(dis_note, allow_note) == 1
            assert cmp(dis_note, note) == -1
            Log.info("Only 250 characters input as note supported")
        else:
            self.input_text(note, self.note)
            self.press_enter_key(self.note)
            dis_note = self. get_element_attribute(self.note, 'value')
            assert cmp(dis_note, note) == 1
            Log.info("Less than 250 and equal to 250 characters supported for note")


    def edit_organization_name(self, org_name):
        """
        Test for organization name edit function
        """
        self.edit_general_inf()
        self.clear_text(self.organization_name)
        self.check_organization_name_length(org_name)
        if len(org_name)!= 0:
            self.save_general_inf()
            self.check_if_edit_success()
            Log.info("Edit organization name action works well")
        else:
            Log.info("Required for organization name to save")

    def edit_tax_id(self, tax_id):
        """
        Test for tax id edit function
        """
        self.edit_general_inf()
        self.clear_text(self.tax_id)
        self.check_tax_id_length(tax_id)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit tax id action works well")

    def display_number_of_employees(self):
        """
        Test for number of employees read function
        """
        dis_num_employess= self.get_element_text(self.number_of_employees)
        print dis_num_employess
        Log.info("The number of employees are displayed")

    def edit_registration_number(self, reg_num):
        """
        Test for registration number edit function
        """
        self.edit_general_inf()
        self.clear_text(self.registration_number)
        self.check_registration_number_length(reg_num)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit registration number action works well")

    def edit_phone(self, phone):
        """
        Test for phone edit function
        """
        self.edit_general_inf()
        self.clear_text(self.phone)
        self.check_phone_valid(phone)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit phone action works well")

    def edit_fax(self, fax):
        """
        Test for fax edit function
        """
        self.edit_general_inf()
        self.clear_text(self.fax)
        self.check_fax_valid(fax)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit fax action works well")

    def edit_email(self, email):
        """
        Test for email edit function
        """
        self.edit_general_inf()
        self.clear_text(self.email)
        self.check_email_valid(email)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit email action works well")

    def edit_address_street_1(self, address):
        """
        Test for address street 1 edit function
        """
        self.edit_general_inf()
        self.clear_text(self.address_street_1)
        self.check_address_Street1_length(address)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit Address Street 1 action works well")

    def edit_address_street_2(self, address):
        """
        Test for address street 1 edit function
        """
        self.edit_general_inf()
        self.clear_text(self.address_street_2)
        self.check_address_Street2_length(address)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit Address Street 2 action works well")

    def edit_city(self, city):
        """
        Test for city edit function
        """
        self.edit_general_inf()
        self.clear_text(self.city)
        self.check_city_length(city)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit City action works well")

    def edit_state_province(self, state_province):
        """
        Test for state/province edit function
        """
        self.edit_general_inf()
        self.clear_text(self.state_province)
        self.check_state_province(state_province)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit State Province action works well")

    def edit_zip_postal_code(self, zip_postal_code):
        """
        Test for zip/postal code
        """
        self.edit_general_inf()
        self.clear_text(self.zip_postal_code)
        self.check_zip_postal_code(zip_postal_code)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit State Zip/Postal Code action works well")

    def select_country(self, country):
        """
        Test for Country
        """
        self.edit_general_inf()
        self.set_combox_value(value=country, keys=self.country)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit Country action works well")

    def edit_note(self, x):

        self.edit_general_inf()
        self.clear_text(self.note)
        note_ge = self.generate_str(x)
        self.check_note_length(note_ge)
        self.save_general_inf()
        self.check_if_edit_success()
        Log.info("Edit note action works well")