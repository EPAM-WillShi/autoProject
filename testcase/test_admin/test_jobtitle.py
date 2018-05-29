# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login

from pageobjects.admin.job.job_titles import JobTitles
from pageobjects.admin.job.edit_job_title import EditJobTitle


class TestJobtitle(unittest.TestCase):
    """
    Test Admin page functions
    """
    browser = config.BROWSER

    input_job_title_text = 'jilladd'
    input_job_description_text = 'testPostion'

    input_job_edit_text = 'jilledit'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.jobtitle = JobTitles(cls.driver)
        cls.addjobtitle = EditJobTitle(cls.driver)

    def test_case1_add_job_title(self):
        # # check job title exsit then delete
        # old_title = self.jobtitle.wait_unit_el_present(self.new_job_title_xpath)
        # if old_title is not None:
        #     self.jobtitle.click_checkbox(self.new_job_title_xpath)
        #     self.jobtitle.click_delete_button()
        #     self.jobtitle.click_confirm_dialog_ok()
        # else:
        #     return None
        # add new job title
        self.jobtitle.click_add_button()
        self.addjobtitle.input_text_job_title(self.input_job_title_text)
        self.addjobtitle.input_text_job_description(self.input_job_description_text)
        self.jobtitle.sleep(1)
        self.addjobtitle.click_save_button()
        # check job title added successfully
        self.jobtitle.assert_message("Successfully Saved")

    def test_case2_edit_job_title(self):
        # choose the job title need to edit
        self.jobtitle.click_job_title(self.input_job_title_text)
        self.addjobtitle.click_edit_button()
        # clear the old information
        self.addjobtitle.clear_job_title_info()
        # write for new job title
        self.addjobtitle.input_text_job_title(self.input_job_edit_text)
        self.addjobtitle.click_edit_button()
        # check edit job title
        self.jobtitle.assert_message("Successfully Updated")

    def test_case3_delete_job_titles(self):
        # check on deleted job title
        self.jobtitle.click_checkbox(self.input_job_edit_text )
        # delete button
        self.jobtitle.click_delete_button()
        # cancel to delete
        self.jobtitle.click_confirm_dialog_ok()
        # check job title deleted successful
        self.jobtitle.assert_message("Successfully Deleted")

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_browser()


if __name__ == "__main__":
    unittest.main()