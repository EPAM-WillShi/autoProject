# -*- coding: utf-8 -*-
from pageobjects.recruitment.recruitment import Recruitment
from lib.log import Log


class Candidates(Recruitment):

    """
    Recruitment Candidates page elements
    """
    #Candidates elements
    tcandi_xpath = './/td[text()="{}"]/preceding-sibling::td[1]'
    delete_btn = ('id', 'btnDelete')
    cdelete_btn = ('id', 'dialogDeleteBtn')
    rcandi_xpath = './/td[text()="{}"]/following-sibling::td[1]/a'
    status_xpath = './/td[text()="{}"]/following-sibling::td[4]'
    status_class = ("xpath", "//span[@class='status']")

    #Add Candidate elements and edit candidate
    add_btn = ('id', 'btnAdd')
    first_name = ('id', 'addCandidate_firstName')
    last_name = ('id', 'addCandidate_lastName')
    e_mail = ('id', 'addCandidate_email')
    job_vacancy = ('id', 'addCandidate_vacancy')
    save_btn = ('id', 'btnSave')
    action = ('xpath', './/select[contains(@id,"viewCandidateAction")]')
    status_reason = ('id', 'candidateVacancyStatus_notes')
    status_btn = ('id', 'actionBtn')
    back_btn = ('id', 'cancelBtn')
    candidate_ele = ("ID", "menu_recruitment_viewCandidates")
    contactNo_ele = ("xpath", "//input[@id='addCandidate_contactNo']")
    backbtn = ("xpath", "//input[@id='btnBack']")
    candidate_link = ("xpath", "//*[@id='resultTable']//tr[./td/a[contains(text(),'julia1_first')]]//a[contains(text(), 'julia1_first')]")
    interview_title = ("id", "jobInterview_name")
    interview_name = ("id", "jobInterview_interviewer_1")
    interview_date = ("id", "jobInterview_date")
    interview_save = ("id", "saveBtn")
    view_link = ("xpath", "//*[@id='resultTable']/tbody/tr[1]/td[3]/a")
    interview_head = ("xpath", "//div[@id='jobInterview']/div[1]/h1")
    interview_backbtn = ("id", "cancelButton")


    def __init__(self, browser):
        super(Candidates, self).__init__(browser)
        self.click_menu("Candidates")
        Log.info("Arrive Recruitment Candidates page")

    def click_candidate_menu(self):
        """
        click the candidates menu
        """
        self.get_element(self.candidate_ele).click()

    def delete_candidates(self, vacan_name):
        """
        delete candidates   ---added by julia
        """
        self.click(self.backbtn)
        tcandi_xpath = self.tcandi_xpath.format(vacan_name)
        tcandi = ('xpath', tcandi_xpath)
        candi = self.get_element(tcandi)
        if candi is not None:
            self.click(tcandi)
            self.click(self.delete_btn)
            self.click(self.cdelete_btn)
            Log.info('Candidates record cleaned up')

    def add_candidates_required(self, firstname, lastname, email, contactNo, vacan_name):
        """
        Add candidates
        1. input first name and last name
        2. input email
        3. input contact number    ---edit by julia
        3. choose job vacancy
        4. click save button
        """
        self.click(self.add_btn)
        self.clear_text(self.first_name)
        self.input_text(firstname, self.first_name)
        self.clear_text(self.last_name)
        self.input_text(lastname, self.last_name)
        self.clear_text(self.e_mail)
        self.input_text(email, self.e_mail)
        self.input_text(contactNo, self.contactNo_ele)
        self.set_combox_value(vacan_name, self.job_vacancy)
        self.wait(2)
        self.click(self.save_btn)
        Log.info("Candidates record added")

    def edit_candidate_contact(self, contactNo):
        """
        edit a candidate's contact number   ---added by julia
        """
        self.get_element(self.save_btn).click()
        self.get_element(self.contactNo_ele).clear()
        self.input_text(contactNo, self.contactNo_ele)
        self.get_element(self.save_btn).click()


    def candidates_edit_status(self, vacan_name, status, status_reason):
        """
        Test Change the candidate's vacancy status to reject Function
        1. click edit button
        2. change status to reject
        3. input reject reason
        4. validate the status
        """
        rcandi_xpath = self.rcandi_xpath.format(vacan_name)
        rcandi = ('xpath', rcandi_xpath)
        candi_rec = self.get_element(rcandi)
        if candi_rec is not None:
            self.click(rcandi)
            self.click(self.save_btn)
            self.set_combox_value(status, self.action)
            self.clear_text(self.status_reason)
            self.input_text(status_reason, self.status_reason)
            self.click(self.status_btn)
            self.click(self.back_btn)
            self.click_menu('Candidates')
            status_xpath = self.status_xpath.format(vacan_name, )
            status = ('xpath', status_xpath)
            assert 'Rejected' == self.get_element_text(status)
        else:
            Log.error("Unable to locate the candidate record")

    def candidates_change_status(self, status, status_reason):
        """
        Change the candidate status to shortlist and check the changed action is correct   ---added by julia
        """
        self.click_candidate_menu()
        self.wait(2)
        candi_name = self.get_element(self.candidate_link)
        if candi_name is not None:
            self.get_element(self.candidate_link).click()
            self.click(self.save_btn)
            self.set_combox_value(status, self.action)
            self.clear_text(self.status_reason)
            self.input_text(status_reason, self.status_reason)
            self.click(self.status_btn)
            self.click(self.back_btn)
            assert 'Status: Shortlisted' == self.get_element_text(self.status_class)
        else:
            raise Exception, "Unable to locate the candidate record"

    def candidates_change_status1(self, status1, interview_title, interview_name, interview_date):
        """
        Change the candidate status to schedule interview and check the changed action is correct   ---added by julia
        """
        self.click_candidate_menu()
        candi_name = self.get_element(self.candidate_link)
        if candi_name is not None:
            self.get_element(self.candidate_link).click()
            self.click(self.save_btn)
            self.wait(2)
            self.set_combox_value(status1, self.action)
            self.clear_text(self.interview_title)
            self.input_text(interview_title, self.interview_title)
            self.clear_text(self.interview_name)
            self.input_text(interview_name, self.interview_name)
            self.clear_text(self.interview_date)
            self.input_text(interview_date, self.interview_date)
            self.click(self.interview_save)
            self.wait(2)
            self.click(self.interview_backbtn)
            self.wait(2)
            self.click(self.view_link)
            assert 'Schedule Interview' == self.get_element_text(self.interview_head)
        else:
            raise Exception, "Unable to locate the candidate record"


