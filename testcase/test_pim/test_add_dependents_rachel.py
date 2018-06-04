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

    # Create a Dependents
    name = "Dependents"
    name1 = "Dependents1"
    name2 = "Dependents2"
    relationshipType_child = "Child"
    relationshipType_other = "Other"
    relationship = "note"
    dateOfBirth = "1990-05-09"
    first_name = 'rachel'
    last_name = 'test2'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.dep = Dependents(cls.driver)

    def test_add_dependents_after_creating_emp_type_child(self):
        self.dep.open_dependents_page_via_creating_emp(self.first_name, self.last_name)
        self.dep.add_dependents_without_specify(self.name, self.relationshipType_child, self.dateOfBirth)

    def test_add_dependents_after_creating_emp_type_other(self):
        self.dep.add_dependents_with_specify(self.name, self.relationshipType_other, self.relationship, self.dateOfBirth)

    def test_edit_the_first_dependents_save(self):
        self.dep.edit_the_first_dependents_save(self.name1)

    def test_edit_the_first_dependents_cancel(self):
        self.dep.edit_the_first_dependents_cancle(self.name2)

    def test_delete_the_first_dependents(self):
        self.dep.delete_the_first_dependents()

    @classmethod
    def tearDownClass(cls):
        cls.dep.quit_browser()

    if __name__ == "__main__":
        unittest.main()
