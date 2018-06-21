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
    Choose an employee, and then click it to go to Immigration page.
    """

    # Attachment CRUD
    attachment = "test.docx"
    comment = utils.input_random_text()
    new_attachment = "testedit.docx"
    new_comment = utils.input_random_text()

    # Immigration CRUD
    # document = "Visa"
    number = utils.input_random_number()
    issued_date = utils.input_random_date()
    expiry_date = utils.input_random_date(issued_date)
    eligible_status = utils.input_random_text()
    # issued_by = "China"
    eligible_review_date = utils.input_random_date(issued_date)
    comments = utils.input_random_text()

    # new_document = "Passport"
    new_number = utils.input_random_number()
    new_issued_date = utils.input_random_date()
    new_expiry_date = utils.input_random_date(new_issued_date)
    new_eligible_status = utils.input_random_text()
    # new_issued_by = "United States"
    new_eligible_review_date = utils.input_random_date(new_issued_date)
    new_comments = utils.input_random_text()

    

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(config.BROWSER)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.immigration = Immigration(cls.driver)
        cls.immigration.open_immigration_page_via_editing_emp()

    @classmethod
    def tearDownClass(cls):
        cls.immigration.quit_browser()

    def test_case01_add_immigration_with_required_fields(self):  # Add an immigration record with required fields only
        self.immigration.click_add_btn()
        self.document = self.immigration.get_document_data()
        self.immigration.input_immigration_details(self.document, self.number)
        self.immigration.save_immigration()
        self.assertTrue(self.immigration.check_immigration_exist(self.document))
        self.immigration.check_immigration_details(self.document, self.number)
        self.immigration.delete_all_immigration()

    def test_case02_cancel_add_immigration(self):  # Cancel the immigration record creation
        self.immigration.click_add_btn()
        self.document = self.immigration.get_document_data()
        self.issued_by = self.immigration.get_issued_by_data()
        self.immigration.input_immigration_details(self.document, self.number,
                                                   issued_date=self.issued_date,
                                                   expiry_date=self.expiry_date,
                                                   eligible_status=self.eligible_status,
                                                   issued_by=self.issued_by,
                                                   eligible_review_date=self.eligible_review_date,
                                                   comments=self.comments)
        self.immigration.cancel_immigration()
        self.assertFalse(self.immigration.check_immigration_exist(self.document))

    def test_case03_add_immigration(self):  # Add an immigration record
        self.immigration.click_add_btn()
        self.document = self.immigration.get_document_data()
        self.issued_by = self.immigration.get_issued_by_data()
        self.immigration.input_immigration_details(self.document, self.number,
                                                   issued_date=self.issued_date,
                                                   expiry_date=self.expiry_date,
                                                   eligible_status=self.eligible_status,
                                                   issued_by=self.issued_by,
                                                   eligible_review_date=self.eligible_review_date,
                                                   comments=self.comments)
        self.immigration.save_immigration()
        self.assertTrue(self.immigration.check_immigration_exist(self.document))
        self.immigration.check_immigration_details(self.document, self.number,
                                                   issued_date=self.issued_date,
                                                   expiry_date=self.expiry_date,
                                                   issued_by=self.issued_by)

    def test_case04_cancel_edit_immigration(self):  # Cancel the immigration record editing
        self.document, self.issued_by = self.immigration.click_existing_record()
        self.new_document = self.immigration.get_document_data()
        self.new_issued_by = self.immigration.get_issued_by_data()
        self.immigration.input_immigration_details(self.new_document, self.new_number,
                                                   issued_date=self.new_issued_date,
                                                   expiry_date=self.new_expiry_date,
                                                   eligible_status=self.new_eligible_status,
                                                   issued_by=self.new_issued_by,
                                                   eligible_review_date=self.new_eligible_review_date,
                                                   comments=self.new_comments)
        self.immigration.cancel_immigration()
        self.immigration.check_immigration_details(self.document, self.number,
                                                   issued_date=self.issued_date,
                                                   expiry_date=self.expiry_date,
                                                   issued_by=self.issued_by)

    def test_case05_edit_immigration(self):  # Edit an immigration record
        self.immigration.click_existing_record()
        self.new_document = self.immigration.get_document_data()
        self.new_issued_by = self.immigration.get_issued_by_data()
        self.immigration.input_immigration_details(self.new_document, self.new_number,
                                                   issued_date=self.new_issued_date,
                                                   expiry_date=self.new_expiry_date,
                                                   eligible_status=self.new_eligible_status,
                                                   issued_by=self.new_issued_by,
                                                   eligible_review_date=self.new_eligible_review_date,
                                                   comments=self.new_comments)
        self.immigration.save_immigration()
        self.assertTrue(self.immigration.check_immigration_exist(self.new_document))
        self.immigration.check_immigration_details(self.new_document, self.new_number,
                                                   issued_date=self.new_issued_date,
                                                   expiry_date=self.new_expiry_date,
                                                   issued_by=self.new_issued_by)

    def test_case06_delete_immigration(self):  # Delete an immigration record
        self.document = self.immigration.delete_immigration()
        self.assertFalse(self.immigration.check_immigration_exist(self.document))

    def test_case07_add_attachment(self):  # Add an attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.assertTrue(self.immigration.check_attachment_exists(self.attachment))
        self.immigration.check_attachment(self.attachment, self.comment)
        self.immigration.delete_all_attachments()

    def test_case08_edit_attachment(self):  # Edit an attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.edit_attachment(self.new_attachment, self.new_comment)
        self.immigration.check_attachment(self.new_attachment, self.new_comment)
        self.immigration.delete_all_attachments()

    def test_case09_edit_attachment_comment_only(self):  # Only edit the comment of the attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.edit_attachment_comment_only(self.new_attachment, self.new_comment)
        self.immigration.check_attachment(self.attachment, self.new_comment)
        self.immigration.delete_all_attachments()

    def test_case10_delete_attachment(self):  # Delete an attachment
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.delete_attachment(self.attachment)
        self.assertFalse(self.immigration.check_attachment_exists(self.attachment))

    def test_case11_cancel_add_attachment(self):  # Cancel the attachment creation
        self.immigration.cancel_add_attachment(self.attachment, self.comment)
        self.assertFalse(self.immigration.check_attachment_exists(self.attachment))

    def test_case12_cancel_edit_attachment(self):  # Cancel the attachment editing
        self.immigration.add_attachment(self.attachment, self.comment)
        self.immigration.cancel_edit_attachment(self.new_attachment, self.new_comment)
        self.immigration.check_attachment(self.attachment, self.comment)
        self.immigration.delete_all_attachments()


if __name__ == "__main__":
    unittest.main()
