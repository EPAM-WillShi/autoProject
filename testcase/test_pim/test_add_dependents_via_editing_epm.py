# -*- coding: utf-8 -*-

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.pim.dependents import Dependents


class TestAddDependents(unittest.TestCase):
    """
        Test add Dependents for employee
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Choose an employee
    first_name = "John"
    last_name = "Smith"

    # Create a Dependent
    name = "A Dependents"
    name1 = "A Dependents1"
    name2 = "A Dependents2"
    relationshipType_child = "Child"
    relationshipType_other = "Other"
    relationship = "note"
    dateOfBirth = "1990-05-09"


    # Create an attachment
    attachment = "test.docx"
    comment = "Added attachment"
    new_attachment = "testedit.docx"
    new_comment = "Edited attachment"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.dep = Dependents(cls.driver)
        cls.dep.open_dependents_page_via_editing_emp(cls.first_name, cls.last_name)

    def test_add_dependents_after_creating_emp_type_child(self):
        self.dep.add_dependents_without_specify(self.name, self.relationshipType_child, self.dateOfBirth)
        self.dep.check_dependents_list(self.name, self.relationshipType_child, self.dateOfBirth)
        self.dep.delete_the_first_dependents()

    def test_add_dependents_after_creating_emp_type_other(self):
        self.dep.add_dependents_with_specify(self.name, self.relationshipType_other, self.relationship, self.dateOfBirth)
        self.dep.check_dependents_list(self.name, self.relationship, self.dateOfBirth)
        self.dep.delete_the_first_dependents()

    def test_edit_the_first_dependents_save(self):
        self.dep.add_dependents_without_specify(self.name, self.relationshipType_child, self.dateOfBirth)
        self.dep.edit_the_first_dependents_save(self.name1)
        self.dep.check_dependents_list(self.name1, self.relationshipType_child, self.dateOfBirth)
        self.dep.delete_the_first_dependents()

    def test_edit_the_first_dependents_cancel(self):
        self.dep.add_dependents_without_specify(self.name, self.relationshipType_child, self.dateOfBirth)
        self.dep.edit_the_first_dependents_cancel(self.name2)
        self.dep.delete_the_first_dependents()

    def test_delete_the_first_dependents(self):
        self.dep.add_dependents_without_specify(self.name, self.relationshipType_child, self.dateOfBirth)
        self.dep.delete_the_first_dependents()

    def test_add_attachments_save(self):
        self.dep.add_attachments_upload(self.attachment, self.comment)
        self.dep.edit_the_first_attachments(self.new_attachment, self.new_comment)

    def test_add_attachments_cancel(self):
        self.dep.add_attachments_cancel(self.attachment, self.comment)

    def test_edit_the_first_attachment(self):
        self.dep.add_attachments_upload(self.attachment, self.comment)
        self.dep.edit_the_first_attachments(self.new_attachment, self.new_comment)
        self.dep.delete_the_first_attachments()

    def test_delete_the_first_attachments(self):
        self.dep.add_attachments_upload(self.attachment, self.comment)
        self.dep.delete_the_first_attachments()

    @classmethod
    def tearDownClass(cls):
        cls.dep.quit_browser()


if __name__ == "__main__":
    unittest.main()
