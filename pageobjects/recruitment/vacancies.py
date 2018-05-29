# -*- coding: utf-8 -*-
"""
Created by Linda
"""
import os
from lib.log import Log
from pageobjects.recruitment.recruitment import Recruitment


class Vacancies(Recruitment):
    """
    Recruitment Vacancies page main components
    """
    # Create a vacancy
    add_btn_ele = ('ID', 'btnAdd')
    job_title_ele = ('ID', 'addJobVacancy_jobTitle')
    vacancy_name_ele = ('ID', 'addJobVacancy_name')
    hiring_manager_ele = ('ID', 'addJobVacancy_hiringManager')
    save_btn_ele = ('ID', 'btnSave')
    back_btn_ele = ('ID', 'btnBack')

    # Find a vacancy
    vacancy_ele_value = "//td[2]//a[text()='{}']"

    # Add an attachment
    add_attachment_btn_ele = ('ID', 'btnAddAttachment')
    upload_attachment_ele = ('ID', 'recruitmentAttachment_ufile')
    add_comment_ele = ('ID', 'recruitmentAttachment_comment')
    upload_attachment_btn_ele = ('ID', 'btnSaveAttachment')

    # Edit an attachment
    attachment_ele = ('XPATH', '//tr[1]/td[2]')
    comment_ele = ('XPATH', '//tr[1]/td[5]')
    edit_attachment_btn_ele = ('XPATH', '//tr[1]/td[6]/a')
    save_comment_only_btn_ele = ('ID', 'btnCommentOnly')

    # Delete an attachment
    check_attachment_ele = ('ID', 'attachmentsCheckAll')
    delete_attachment_btn_ele = ('ID', 'btnDeleteAttachment')

    # Search vacancies
    search_hiring_manager_ele = ('ID', 'vacancySearch_hiringManager')
    search_btn_ele = ('ID', 'btnSrch')
    expected_row_ele_value = "//td[4][text()='{}']"
    actual_row_ele = ('XPATH', '//tbody/tr')

    # Delete vacancies
    delete_btn_ele = ('ID', 'btnDelete')
    ok_btn_ele = ('ID', 'dialogDeleteBtn')

    # Open RSS Feed URL
    rss_feed_url_btn = ("XPATH", "//li[9]/a")

    # Open Web Page URL
    web_page_url_btn = ("XPATH", "//li[10]/a")
    active_job_vacancies_ele = ("XPATH", "//h1[text()='Active Job Vacancies']")

    # Apply
    apply_btn_ele_value = "//h3[text()='{}']/ancestor-or-self::div/p/input[@value='Apply']"
    apply_page_ele_value = "//h1[contains(text(),'{}')]"
    first_name_ele = ('ID', 'addCandidate_firstName')
    last_name_ele = ('ID', 'addCandidate_lastName')
    email_ele = ('ID', 'addCandidate_email')
    resume_ele = ('ID', 'addCandidate_resume')
    submit_btn_ele = ('ID', 'btnSave')
    check_resume_ele = ('ID', "//span[text()='Uploaded']")

    # Vacancies elements
    tvacan_xpath = './/a[text()="{}"]/../preceding-sibling::td[1]'

    def __init__(self, browser):
        super(Vacancies, self).__init__(browser)
        self.click_menu("Vacancies")
        Log.info("Arrive Recruitment Vacancies page")
        
    def create_vacancy(self, jobtitle, vacancyname, hiringmanager):
        """
        Add vacancies
        1. input job title
        2. input vacancy name
        3. input hiring manager
        4. click save button
        """
        self.click(self.add_btn_ele)
        self.set_combox_value(jobtitle, self.job_title_ele)
        self.clear_text(self.vacancy_name_ele)
        self.input_text(vacancyname, self.vacancy_name_ele)
        self.clear_text(self.hiring_manager_ele)
        self.input_text(hiringmanager, self.hiring_manager_ele)
        self.click(self.save_btn_ele)
        Log.info("Vacancies record added")
        
    def open_vacancy(self, job_title, vacancy_name, hiring_manager):
        """
        If the vacancy exists, click vacancy name to open
        If the vacancy doesn't exist, create a vacancy
        """
        vacancy_ele = self.vacancy_ele_value.format(vacancy_name)
        try:
            self.wait_unit_el_present(("XPATH", vacancy_ele))
            self.click(("XPATH", vacancy_ele))
        except:
            self.create_vacancy(job_title, vacancy_name, hiring_manager)

    def delete_attachment(self):
        """
        Delete all attachments
        """
        try:
            self.click(self.check_attachment_ele)
            self.click(self.delete_attachment_btn_ele)
        except:
            Log.info("No attachment is found!")

    def add_attachment(self, attachment, comment):
        """
        Add an attachment
        """
        self.click(self.add_attachment_btn_ele)
        path = os.getcwd().split("testcase")[0]
        upload_file = path + attachment
        self.sleep(1)
        self.input_text(upload_file, self.upload_attachment_ele)
        self.clear_text(self.add_comment_ele)
        self.input_text(comment, self.add_comment_ele)
        self.click(self.upload_attachment_btn_ele)

    def edit_attachment(self, attachment, new_attachment, new_comment):
        """
        Edit the attachment - save comment only
        """
        self.click(self.edit_attachment_btn_ele)
        path = os.getcwd().split("testcase")[0]
        upload_file = path + new_attachment
        self.input_text(upload_file, self.upload_attachment_ele)
        self.clear_text(self.add_comment_ele)
        self.input_text(new_comment, self.add_comment_ele)
        self.click(self.save_comment_only_btn_ele)
        attachment = attachment.split("testfiles\\")[1]
        check_attachment = self.get_element_text(self.attachment_ele)
        check_comment = self.get_element_text(self.comment_ele)
        assert check_attachment == attachment
        assert check_comment == new_comment
        Log.info("Save comment only successfully.")

    def click_back_btn(self):
        """
        Click back button to go back to Vacancies page
        """
        self.click(self.back_btn_ele)

    def expected_search_result(self, hiring_manager):
        """
        Obtain expected row of search result
        """
        expected_row_ele = self.expected_row_ele_value.format(hiring_manager)
        expected_row = self.get_elements(("XPATH", expected_row_ele))
        return len(expected_row)

    def search_vacancies_by_hiring_manager(self, hiring_manager):
        """
        Search vacancies by hiring manager
        """
        self.set_combox_value(hiring_manager, self.search_hiring_manager_ele)
        self.wait(2)
        self.click(self.search_btn_ele)

    def check_search_result(self, expected_row):
        """
        Check if actual row of search result is equal to expected row
        """
        actual_row = self.get_elements(self.actual_row_ele)
        assert len(actual_row) == expected_row
        Log.info('Search result is correct.')

    def delete_vacancies(self, vacan_name):
        """
        Delete all vacancies
        """
        tvacan_xpath = self.tvacan_xpath.format(vacan_name)
        tvacan = ('xpath', tvacan_xpath)
        vacan = self.get_element(tvacan)
        if vacan is not None:
            try:
                self.click(tvacan)
                self.click(self.delete_btn_ele)
                self.click(self.ok_btn_ele)
                Log.info('Vacancies record cleaned up')
            except:
                Log.info("No vacancy should be deleted!")

    def click_rss_feed_url(self):
        """
        Open application page rss feed url
        """
        self.click(self.rss_feed_url_btn)

    def click_web_page_url(self):
        """
        Open application page via web page url
        """
        self.click(self.web_page_url_btn)
        now_handle = self.get_current_window()
        all_handles = self.get_all_window()
        for handle in all_handles:
            if handle != now_handle:
                self.switch_to_window(handle)
        check_active_job_vacancies = self.get_element(self.active_job_vacancies_ele)
        if check_active_job_vacancies is not None:
            Log.info("Open Active Job Vacancies page")

    def click_apply_btn(self, vacancy):
        """
        Apply for a job
        """
        apply_btn_ele = self.apply_btn_ele_value.format(vacancy)
        self.click(("XPATH", apply_btn_ele))
        apply_page_ele = self.apply_page_ele_value.format(vacancy)
        check_apply_page = self.get_element(("XPATH", apply_page_ele))
        if check_apply_page is not None:
            Log.info("Open Apply page")

    def input_person_details(self, first_name, last_name, resume):
        """
        Input applicant details
        """
        self.clear_text(self.first_name_ele)
        self.input_text(first_name, self.first_name_ele)
        self.clear_text(self.last_name_ele)
        self.input_text(last_name, self.last_name_ele)
        self.clear_text(self.email_ele)
        self.input_text(first_name+'_'+last_name+'@epam.com', self.email_ele)
        path = os.getcwd().split("testcase")[0]
        upload_file = path + resume
        self.input_text(upload_file, self.resume_ele)
        self.click(self.submit_btn_ele)

    def check_person_details(self, first_name, last_name):
        """
        Check applicant details
        """
        assert self.get_element_attribute(self.first_name_ele, "value") == first_name
        Log.info("First name is correct.")
        assert self.get_element_attribute(self.last_name_ele, "value") == last_name
        Log.info("Last name is correct.")
        assert self.get_element_attribute(self.email_ele, "value") == first_name+'_'+last_name+'@epam.com'
        Log.info("Email is correct.")
        check_resume_value = self.get_element(self.check_resume_ele)
        if check_resume_value is not None:
            Log.info("Resume is upload successfully")
           

