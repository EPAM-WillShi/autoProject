# -*- coding: utf-8 -*-
"""
Created on 2018/6/13
@author: Molly Xue
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.admin.org.general_info import GeneralInformation
from lib.log import Log


class TestGeneralInformation(unittest.TestCase):
    """
    Test General Information page functions
    """
    browser = config.BROWSER
    # set testing data
    organization_name_null = ""
    organization_name_max = "ABCDEFGHigklmnopqrstuvwxyz!@#$%^ui3456789OPUuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
    organization_name = "Molly defined organization name"

    tax_id_null = ""
    tax_id_max = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^()"
    tax_id = "molly_taxid051266667777"

    registration_number_null = ""
    registration_number_max = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^()"
    registration_number = "molly add registration number1"

    phone_null = ''
    phone_invalid = 'qwehhh'
    phone_max = '0123456789012345678901234567890123456789'
    phone = '(+86)15062628751'

    fax_null = ''
    fax_invalid = 'QWRHHJHJ'
    fax_max = '0123456789012345678901234567890123456789'
    fax = '(+86)-051266778899'

    email_null = ''
    email_invalid = 'udhufhjlkk@jjjj'
    email_max = 'jsjfdsjfjdsk@dfkjgjfdkgfdkjsg.comfjhdsfhdjfhdjfhdufeirteritiurhterurughruuhgrgiejrower'
    email = 'molly_xue@epam.com'

    address_null = ''
    address_max = 'molly tested address street 1 and address street 2, which has more than 100' \
                  ' characters, dfdkdfdfdfdsfdsfdsfdsfdsfdsfdsfdsfdsfdfdsfds'
    address1 = 'address1-molly added'
    address2 = 'address2-molly added'

    city_null = ''
    city_max = 'City1234567890123456789012345678901234567890'
    city = 'SuZhou_molly_hometown'

    state_province_null = ''
    state_province_max = 'State province is molly added to test the limit length is less than 30 01233345'
    state_province = 'Jiangsu-molly added'

    zip_postal_code_null = ''
    zip_postal_code_max = 'Zip / Postal Code is molly added to test the limit length...'
    zip_postal_code = '215004-molly added'

    country_null = '-- Select --'
    country_a = 'American Samoa'
    country_b = 'Bhutan'

    note_less_250 = 10
    note_more_250 = 260


    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.generalinfo = GeneralInformation(cls.driver)
        Log.info("SetupClass for General Information - passed")
        Log.info("Start to run General Information page")

    def test_case1_edit_organization_name(self):
        """
        Test Case1: Try to check organization name field
        """
        Log.info("Start to run test_case1_edit_organization_name")
        Log.info("Edit to null")
        self.generalinfo.edit_organization_name(self.organization_name_null)
        Log.info("Edit to limit length")
        self.generalinfo.edit_organization_name(self.organization_name_max)
        Log.info("Edit to valid length")
        self.generalinfo.edit_organization_name(self.organization_name)
        Log.info("Run Test case1: Edit organization name - completed")

    def test_case2_edit_tax_id(self):
        """
        Test Case2: Try to check Tax ID
        """
        Log.info("Start to run test_case2_edit_tax_id")
        Log.info("Edit to null")
        self.generalinfo.edit_tax_id(self.tax_id_null)
        Log.info("Edit to limit length")
        self.generalinfo.edit_tax_id(self.tax_id_max)
        Log.info("Edit to valid length")
        self.generalinfo.edit_tax_id(self.tax_id)
        Log.info("Run Test case1: Edit organization name - completed")

    def test_case3_show_number_of_employees(self):
        """
        Test Case3: Try to check number of employees
        """
        Log.info("Start to run test_case3_show_number_of_employees")
        self.generalinfo.display_number_of_employees()
        Log.info("Ran Test Case3: Show number of employees - completed")

    def test_case4_edit_registration_number(self):
        """
        Test Case4: Try to check Registration Name
        """
        Log.info("Start to run test_case4_edit_registration_number")
        self.generalinfo.edit_registration_number(self.registration_number_null)
        self.generalinfo.edit_registration_number(self.registration_number_max)
        self.generalinfo.edit_registration_number(self.registration_number)
        Log.info("Run Test Case4: Edit registration number works well")

    def test_case5_edit_phone(self):
        """
        Test Case5: Try to check Phone
        """
        Log.info("Start to run test_case5_edit_phone")
        self.generalinfo.edit_phone(self.phone_invalid)
        self.generalinfo.edit_phone(self.phone_null)
        self.generalinfo.edit_phone(self.phone_max)
        self.generalinfo.edit_phone(self.phone)
        Log.info("Run Test Case5: Edit phone works well")

    def test_case6_edit_fax(self):
        """
        Test Case6: Try to check Fax
        """
        Log.info("Start to run test_case6_edit_fax")
        self.generalinfo.edit_fax(self.fax_invalid)
        self.generalinfo.edit_fax(self.fax_null)
        self.generalinfo.edit_fax(self.fax_max)
        self.generalinfo.edit_fax(self.fax)
        Log.info("Run Test Case6: Edit Fax works well")

    def test_case7_edit_email(self):
        """
        Test Case7: Try to check Email
        """
        Log.info("Start to run test_case7_edit_email")
        self.generalinfo.edit_email(self.email_invalid)
        self.generalinfo.edit_email(self.email_null)
        self.generalinfo.edit_email(self.email_max)
        self.generalinfo.edit_email(self.email)
        Log.info("Run Test Case7: Edit email works well")

    def test_case81_edit_address_street_1(self):
        """
        Test Case8: Try to check Address Street 1
        """
        Log.info("Start to run test_case8_edit_address_street_1")
        self.generalinfo.edit_address_street_1(self.address_null)
        self.generalinfo.edit_address_street_1(self.address_max)
        self.generalinfo.edit_address_street_1(self.address1)
        Log.info("Run Test Case8: Edit Address Street 1 works well")

    def test_case82_edit_address_street_2(self):
        """
        Test Case8: Try to check Address Street 2
        """
        Log.info("Start to run test_case8_edit_address_street_2")
        self.generalinfo.edit_address_street_2(self.address_null)
        self.generalinfo.edit_address_street_2(self.address_max)
        self.generalinfo.edit_address_street_2(self.address2)
        Log.info("Run Test Case8: Edit Address Street 2 works well")

    def test_case91_edit_city(self):
        """
        Test Case9: Try to check City
        """
        Log.info("Start to run test_case9_edit_city")
        self.generalinfo.edit_city(self.city_null)
        self.generalinfo.edit_city(self.city_max)
        self.generalinfo.edit_city(self.city)
        Log.info("Run Test Case9: Edit City works well")

    def test_case92_edit_state_province(self):
        """
        Test Case10: Try to check state/province
        """
        Log.info("Start to run test_case10_edit_state_province")
        self.generalinfo.edit_state_province(self.state_province_null)
        self.generalinfo.edit_state_province(self.state_province_max)
        self.generalinfo.edit_state_province(self.state_province)
        Log.info("Run Test Case10: Edit state province works well")

    def test_case93_edit_zip_postal_code(self):
        """
        Test Case11: Try to check Zip/Postal Code
        """
        Log.info("Start to run test case11_edit_zip_postal_code")
        self.generalinfo.edit_zip_postal_code(self.zip_postal_code_null)
        self.generalinfo.edit_zip_postal_code(self.zip_postal_code_max)
        self.generalinfo.edit_zip_postal_code(self.zip_postal_code)
        Log.info("Run Test Case11: Edit Zip/Postal Code works well")

    def test_case94_select_country(self):
        """
        Test Case12: Try to check Country
        """
        Log.info("Start to run test case12_select_country")
        self.generalinfo.select_country(self.country_null)
        self.generalinfo.select_country(self.country_a)
        self.generalinfo.select_country(self.country_b)
        Log.info("Run test case12: Select Country works well")

    def test_case95_edit_note(self):
        """
        Test Case13: Try to edit note
        """
        Log.info("Start to run test case13_edit_note")
        self.generalinfo.edit_note(self.note_less_250)
        self.generalinfo.edit_note(self.note_more_250)
        Log.info("Run test case13: Edit note works well")


    @classmethod
    def tearDownClass(cls):
        cls.generalinfo.quit_browser()
        Log.info("End of testing General Information page")

if __name__ == "__main__":
    unittest.main()