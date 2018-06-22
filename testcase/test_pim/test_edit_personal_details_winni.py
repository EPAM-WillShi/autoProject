# -*-coding:utf-8-*-

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.edit_personal_details import EditPersonalDetails

class TestPersonalDetails(unittest.TestCase):
    """
    Test edit personal details for employee functions
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER
    # Add employee
    first_name = utils.input_random_text(5)
    last_name = utils.input_random_text(5)
    #edit employee
    middle_name = utils.input_random_text(5)
    empid = utils.input_random_number(4)
    othid = utils.input_random_number(3)
    licnum = utils.input_random_number(3)
    lic_expdate = "2018-06-01"
    gender = "Male"
    marital = "Single"
    nation = "Chinese"
    dob = "1988-11-27"
    attachment1 = "1.png"
    comments1 = utils.input_random_text(10)
    attachment2 = "2.png"
    comments2 = utils.input_random_text(10)
    attachment3 = "3.png"
    comments3 = utils.input_random_text(10)
    file_name = "3.png"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.edit_personal_details = EditPersonalDetails(cls.driver)
        cls.edit_personal_details.open_personal_details_via_adding_employee(cls.first_name, cls.last_name)

    def test_case01_edit_personal_details_name(self):
        self.edit_personal_details.edit_personal_details_name(self.first_name, self.middle_name, self.last_name)

    def test_case02_edit_personal_details_id(self):
        self.edit_personal_details.edit_personal_details_id(self.empid, self.othid, self.licnum, self.lic_expdate)

    def test_case03_edit_personal_details_basic_information(self):
        self.edit_personal_details.edit_personal_details_basic_information(self.gender, self.marital, self.nation, self.dob)

    def test_case04_edit_personal_details_cancel_add_attahment_comments(self):
        self.edit_personal_details.edit_personal_details_cancel_add_attahment_comments(self.attachment1, self.comments1)

    def test_case05_edit_personal_details_add_attachment_comments(self):
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment1, self.comments1)

    def test_case06_edit_personal_details_edit_commentsonly(self):
        self.edit_personal_details.edit_personal_details_edit_commentsonly(self.attachment2, self.comments2)

    def test_case07_edit_personal_details_cancel_edit_attachment_comments(self):
        self.edit_personal_details.edit_personal_details_cancel_edit_attachment_comments(self.attachment2, self.comments2)

    def test_case08_edit_personal_details_edit_attachment_comments(self):
        self.edit_personal_details.edit_personal_details_edit_attachment_comments(self.attachment3, self.comments3)

    def test_case09_edit_personal_details_delete_record_for_attachment(self):
        self.edit_personal_details.edit_personal_details_delete_record_for_attachment(self.file_name)

    def test_case10_edit_personal_details_delete_all_records(self):
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment1, self.comments1)
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment2, self.comments2)
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment3, self.comments3)
        self.edit_personal_details.edit_personal_details_delete_all_records()

    @classmethod
    def tearDownClass(cls):
        cls.edit_personal_details.quit_browser()


if __name__ == '__main__':
    unittest.main()
