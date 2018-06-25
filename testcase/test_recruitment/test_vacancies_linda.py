# coding:utf-8
import unittest
from config import config
from com import utils
from pageobjects.login import Login
from pageobjects.recruitment.vacancies import Vacancies


class TestVacancies(unittest.TestCase):
    """
    Test Recruitment Vacancies page functions
    """
    # Login
    login_url = config.LOGIN_URL
    username = config.USER_NAME
    passwd = config.PASSWORD
    browser = config.BROWSER

    # Create a vacancy
    job_title = "CEO"
    vacancy = "Job_01"
    vacancy_02 = "Job_02"
    vacancy_03 = "Job_03"
    hiring_manager = "Steven Edwards"
    hiring_manager_02 = "John Smith"

    # Add an attachment
    attachment = "test.docx"
    comment = "comment"

    # Edit an attachment
    new_attachment = "testedit.docx"
    new_comment = "edit comment"

    # Delete vacancies
    vacancy_key = "Job_0"

    # Apply
    first_name = "linda"
    last_name = "zang"
    resume = "test.docx"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.vacancies = Vacancies(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.vacancies.quit_browser()

    def test_case07_vacancies_edit_attachment_save_comment_only(self):  # Edit the attachment - save comment only
        self.vacancies.open_vacancy(self.job_title, self.vacancy, self.hiring_manager)  # Open a vacancy
        self.vacancies.delete_attachment()
        self.vacancies.add_attachment(self.attachment, self.comment)  # Add an attachment
        self.vacancies.edit_attachment(self.attachment, self.new_attachment, self.new_comment)  # Edit the attachment
        self.vacancies.click_back_btn()

    def test_case12_vacancies_search_vacancies_by_hiringmanager(self):  # Vacancies search by hiring manager
        self.vacancies.delete_vacancies(self.vacancy)  # Delete all vacancies
        self.vacancies.delete_vacancies(self.vacancy_02)
        self.vacancies.delete_vacancies(self.vacancy_03)
        self.vacancies.create_vacancy(self.job_title, self.vacancy, self.hiring_manager)  # Create a vacancy
        self.vacancies.click_back_btn()
        self.vacancies.create_vacancy(self.job_title, self.vacancy_02, self.hiring_manager)  # Create a vacancy
        self.vacancies.click_back_btn()
        self.vacancies.create_vacancy(self.job_title, self.vacancy_03, self.hiring_manager_02)  # Create a vacancy
        self.vacancies.click_back_btn()
        self.expected_row = self.vacancies.expected_search_result(self.hiring_manager)  # Obtain expected row
        self.vacancies.search_vacancies_by_hiring_manager(self.hiring_manager)  # Search vacancies by hiring_manager
        self.vacancies.check_search_result(self.expected_row)  # Verify row number is equal to expected row

    def test_case3_vacancies_Apply_for_a_job(self):  # Apply for a job via Web Page URL
        self.vacancies.open_vacancy(self.job_title, self.vacancy, self.hiring_manager)  # Open a vacancy
        self.vacancies.click_web_page_url()  # Open application page
        self.vacancies.click_apply_btn(self.vacancy)  # Apply for a job
        self.vacancies.input_person_details(self.first_name, self.last_name, self.resume)  # Input applicant details
        self.vacancies.check_person_details(self.first_name, self.last_name)  # Check applicant details


if __name__ == "__main__":
    unittest.main()
