# coding:utf-8
"""
Created by Linda
"""
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.immigration import Immigration


class TestImmigration(unittest.TestCase):
    """
    Test PIM Immigration page functions
    Create an employee, and then click it to go to Immigration page.
    """
    # Create an employee
    first_name = "linda"
    last_name = "test"

    # Attachment CRUD
    attachment = "test.docx"
    comment = "Added attachment"
    new_attachment = "testedit.docx"
    new_comment = "Edited attachment"

    # Immigration CRUD
    document = "Visa"
    number = "123AB"
    issued_date = "2018-05-30"
    expiry_date = "2018-05-31"
    eligible_status = "Active"
    issued_by = "China"
    eligible_review_date = "2018-05-31"
    comments = "Added"

    new_document = "Passport"
    new_number = "456CD"
    new_issued_date = "2018-06-01"
    new_expiry_date = "2018-06-02"
    new_eligible_status = "Cancel"
    new_issued_by = "United States"
    new_eligible_review_date = "2018-06-03"
    new_comments = "Edited"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.immigration = Immigration(cls.driver)
        cls.immigration.open_immigration_page_via_creating_emp(cls.first_name, cls.last_name)

    @classmethod
    def tearDownClass(cls):
        cls.immigration.click_menu("Employee List")
        cls.immigration.delete_employee(cls.first_name + " " + cls.last_name)
        cls.immigration.quit_browser()

    def test_add_immigration(self):  # Add an immigration record
        self.immigration.add_immigration(self.document, self.number, self.issued_date,
                                         self.expiry_date, self.eligible_status, self.issued_by,
                                         self.eligible_review_date, self.comments)
        self.assertTrue(self.immigration.check_immigration_exist(self.document))
        self.immigration.check_immigration_details(self.document, self.number, self.issued_date,
                                                   self.expiry_date, self.issued_by)
        self.immigration.delete_all_immigration()

    def test_edit_immigration(self):  # Edit an immigration record
        self.immigration.add_immigration(self.document, self.number, self.issued_date,
                                         self.expiry_date, self.eligible_status, self.issued_by,
                                         self.eligible_review_date, self.comments)
        self.immigration.edit_immigration(self.document, self.new_document, self.new_number, self.new_issued_date,
                                          self.new_expiry_date, self.new_eligible_status, self.new_issued_by,
                                          self.new_eligible_review_date, self.new_comments)
        self.assertTrue(self.immigration.check_immigration_exist(self.new_document))
        self.immigration.check_immigration_details(self.new_document, self.new_number, self.new_issued_date,
                                                   self.new_expiry_date, self.new_issued_by)
        self.immigration.delete_all_immigration()

    def test_delete_immigration(self):  # Delete an immigration record
        self.immigration.add_immigration(self.document, self.number, self.issued_date,
                                         self.expiry_date, self.eligible_status, self.issued_by,
                                         self.eligible_review_date, self.comments)
        self.immigration.delete_immigration(self.document)
        self.assertFalse(self.immigration.check_immigration_exist(self.document))

    def test_add_attachment(self):  # Add an attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.assertTrue(self.immigration.check_attachment_exists(self.attachment))
        self.immigration.check_attachment(self.attachment, self.comment)
        self.immigration.delete_all_attachments()

    def test_edit_attachment(self):  # Edit an attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.edit_attachment(self.new_attachment, self.new_comment)
        self.immigration.check_attachment(self.new_attachment, self.new_comment)
        self.immigration.delete_all_attachments()

    def test_edit_attachment_comment_only(self):  # Only edit the comment of the attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.edit_attachment_comment_only(self.new_attachment, self.new_comment)
        self.immigration.check_attachment(self.attachment, self.new_comment)
        self.immigration.delete_all_attachments()

    def test_delete_attachment(self):  # Delete an attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.delete_attachment(self.attachment)
        self.assertFalse(self.immigration.check_attachment_exists(self.attachment))

    def test_cancel_add_immigration(self):  # Cancel the immigration record creation
        self.immigration.cancel_add_immigration(self.document, self.number, self.issued_date,
                                                self.expiry_date, self.eligible_status, self.issued_by,
                                                self.eligible_review_date, self.comments)
        self.assertFalse(self.immigration.check_immigration_exist(self.document))

    def test_cancel_edit_immigration(self):  # Cancel the immigration record editing
        self.immigration.add_immigration(self.document, self.number, self.issued_date,
                                         self.expiry_date, self.eligible_status, self.issued_by,
                                         self.eligible_review_date, self.comments)
        self.immigration.cancel_edit_immigration(self.document, self.new_document, self.new_number,
                                                 self.new_issued_date, self.new_expiry_date, self.new_eligible_status,
                                                 self.new_issued_by, self.new_eligible_review_date, self.new_comments)
        self.immigration.check_immigration_details(self.document, self.number, self.issued_date,
                                                   self.expiry_date, self.issued_by)
        self.immigration.delete_all_immigration()

    def test_cancel_add_attachment(self):  # Cancel the attachment creation
        self.immigration.cancel_add_attachment(self.attachment, self.comment)
        self.assertFalse(self.immigration.check_attachment_exists(self.attachment))

    def test_cancel_edit_attachment(self):  # Cancel the attachment editing
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.cancel_edit_attachment(self.new_attachment, self.new_comment)
        self.immigration.check_attachment(self.attachment, self.comment)
        self.immigration.delete_all_attachments()


if __name__ == "__main__":
    unittest.main()
