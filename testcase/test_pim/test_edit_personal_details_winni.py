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
    first_name = "Winnitest"
    last_name = "Zhangtest"
    #edit employee
    firstname = "Winni"
    middlename = "test"
    lastname = "Zhang"
    empid = "9999"
    othid = "222"
    licnum = "333"
    lic_expdate = "2018-06-01"
    gender = "Male"
    marital = "Single"
    nation = "Chinese"
    dob = "1988-11-27"
    attachment1 = "1.png"
    comments1 = "test automation"
    attachment2 = "2.png"
    comments2 = "update comments only"
    attachment3 = "3.png"
    comments3 = "update again"
    file_name = "3.png"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.edit_personal_details = EditPersonalDetails(cls.driver)
        cls.edit_personal_details.open_personal_details_via_adding_employee(cls.first_name, cls.last_name)

    def test_case1_edit_personal_details_name(self):
        self.edit_personal_details.edit_personal_details_name(self.firstname, self.middlename, self.lastname)

    def test_case2_edit_personal_details_id(self):
        self.edit_personal_details.edit_personal_details_id(self.empid, self.othid, self.licnum, self.lic_expdate)

    def test_case3_edit_personal_details_basic_information(self):
        self.edit_personal_details.edit_personal_details_basic_information(self.gender, self.marital, self.nation, self.dob)

    def test_case4_edit_personal_details_add_attachment(self):
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment1, self.comments1)

    def test_case5_edit_personal_details_edit_commentsonly(self):
        self.edit_personal_details.edit_personal_details_edit_commentsonly(self.attachment2, self.comments2)

    def test_case6_edit_personal_details_edit_attachment_comments(self):
        self.edit_personal_details.edit_personal_details_edit_attachment_comments(self.attachment3, self.comments3)

    def test_case7_edit_personal_details_delete_record_for_attachment(self):
        self.edit_personal_details.edit_personal_details_delete_record_for_attachment(self.file_name)

    def test_case8_edit_personal_details_delete_all_records(self):
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment1, self.comments1)
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment2, self.comments2)
        self.edit_personal_details.edit_personal_details_add_attachment_comments(self.attachment3, self.comments3)
        self.edit_personal_details.edit_personal_details_delete_all_records()

    @classmethod
    def tearDownClass(cls):
        cls.edit_personal_details.quit_browser()


if __name__ == '__main__':
        unittest.main
