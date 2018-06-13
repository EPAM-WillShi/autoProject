# -*- coding: utf-8 -*-
"""
Created on 2018/6/13
@author: Molly Xue
"""

import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.admin.job.job_categories import JobCategories
from lib.log import Log

class TestJobCategories(unittest.TestCase):
    """
    Test Job Categories page functions
    """
    browser = config.BROWSER
    # set testing data
    null_jobcate_name = ''
    limit_jobcate_name = 'JobCategory1234KLMNOPQRSTUVXXYZabcdehhjhjhjhjhjhlklklkfghijklmnopqrstuvwxyz'
    mul_jobcate_name = 'molly job category add'
    mul_time = 5
    valid_jobcate = 'test job category'
    update_jobcate_null = ''
    update_jobcate_duplicate = 'test job category'
    update_jobcate_valid = 'test job category_updated'
    default_job_category = ['Technicians', 'Service Workers', 'Sales Workers', 'Professionals',
                            'Operatives', 'Officials and Managers', 'Office and Clerical Workers',
                            'Laborers and Helpers', 'Craft Workers']

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.jobcate = JobCategories(cls.driver)
        Log.info("SetupClass for Job Categories- passed")
        Log.info("Start to run Job Category page")

    def test_case1_check_null_jobcate_textfiled(self):
        """
        Test Case1: Try to check employee status with NULL
        """
        Log.info("Start to run test_case1_check_null_jobcate_textfiled")
        self.jobcate.check_if_job_category_valid(self.null_jobcate_name)
        Log.info("Run Test Case1: Check Null job category is not allowed - completed!")

    def test_case2_check_limit_jobcate_textfield(self):
        """
        Test Case2: Try to check job category with more than 50 characters
        """
        Log.info("Start to run test_case2_check_limit_jobcate_textfield")
        self.jobcate.check_if_job_category_valid(self.limit_jobcate_name)
        Log.info("Run Test Case2: Check 50+ characters job category is not allowed - completed!")

    def test_case3_add_job_category(self):
        """
        Test Case3: Try to add one new job category
        """
        Log.info("Start to run test_case3_add_job_category")
        check_jobcate_name = self.jobcate.check_if_job_category_exist(self.valid_jobcate)
        if check_jobcate_name is None:
            self.jobcate.add_job_category(self.valid_jobcate)
            Log.info("Run Test Case3: Add one new job category - completed!")
        else:
            Log.info("Don't run Test Case3: Add one new job category - skipped...")

    def test_case4_add_mul_job_category(self):
        """
        Test Case4: Try to add multiple job category
        """
        Log.info("Start to run test_case4_add_mul_job_category")
        check_jobcate_name = self.jobcate.check_if_job_category_exist(self.mul_jobcate_name)
        if check_jobcate_name is None:
            for i in range(1, self.mul_time):
                suffix = str(i)
                mul_jobcate_name = self.mul_jobcate_name + suffix
                self.jobcate.add_job_category(mul_jobcate_name)
                i += 1
            Log.info("Run Test Case4: Add multiple job categories - completed!")
        else:
            Log.info("Don't run Test Case 4: Add multiple job categories - skipped...")

    def test_case5_edit_empty_job_category(self):
        """
        Test Case5: Try to find exist job category and modify into NULL
        """
        Log.info("Start to run test_case5_edit_empty_job_category")
        self.jobcate.edit_job_category(self.valid_jobcate, self.update_jobcate_null)
        Log.info("Run Test Case 5: Edit exist job category to empty not allowed")

    def test_case6_edit_duplicate_job_category(self):
        """
        Test Case6: Try to find exist job category and modify into duplicate one
        """
        Log.info("Start to run test_case6_edit_duplicate_job_category")
        self.jobcate.edit_job_category(self.valid_jobcate, self.update_jobcate_duplicate)
        Log.info("Run Test Case 6: Edit duplicate job category not allowed")

    def test_case7_edit_job_category(self):
        """
        Test Case7: Try to find exist job category and modify into a new valid job category
        """
        Log.info("Start to run test_case7_edit_job_category")
        self.jobcate.edit_job_category(self.valid_jobcate, self.update_jobcate_valid)
        Log.info("Run Test Case 7: Edit exist job category into new valid one - completed")

    def test_case8_delete_job_category(self):
        """
        Test Case8: Try to delete one employee status
        """
        Log.info("Start to run test_case8_delete_job_category")
        self.jobcate.delete_job_category(self.update_jobcate_valid)
        Log.info("Run Test Case 8: Delete exist job category - completed!")

    def test_case91_delete_all_job_category(self):
        """
        Test Case9: Try to delete all job categories
        """
        Log.info("Start to run test_case9_delete_all_job_category")
        self.jobcate.delete_all_job_category()
        Log.info("Run Test Case 9: Delete all job categories - completed!")

    def test_case92_restore_job_category(self):
        """
        Test Case10: Try to restore default job category
        """
        Log.info("Start to run test_case10_restore_job_category")
        default_num = len(self.default_job_category)
        for i in range(0, int(default_num)):
            get_default_jobcate = self.default_job_category[i]
            self.jobcate.add_job_category(get_default_jobcate)
            i += 1
        Log.info("Ran Test Case 10: Restore back default job category")


    @classmethod
    def tearDownClass(cls):
        cls.jobcate.quit_browser()
        Log.info("End of testing Job Category page")

if __name__ == "__main__":
    unittest.main()