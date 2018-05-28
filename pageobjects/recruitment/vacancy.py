# -*- coding: utf-8 -*-
"""
Created by Julia
"""
from pageobjects.mainpage import MainPage
from lib.log import Log
from pageobjects.recruitment.recruitment import Recruitment


class Vacancy(MainPage):
    """
    Candidates page elements
    """
    # Vacancies elements
    tvacan_xpath = './/a[text()="{}"]/../preceding-sibling::td[1]'
    delete_btn = ('id', 'btnDelete')
    vdelete_btn = ('id', 'dialogDeleteBtn')

    # Add job vacancy elements
    add_btn = ('id', 'btnAdd')
    job_title = ('id', 'addJobVacancy_jobTitle')
    vacan_name = ('id', 'addJobVacancy_name')
    hiring_manager = ('id', 'addJobVacancy_hiringManager')
    save_btn = ('id', 'btnSave')
    vacancy_ele = ("ID", "menu_recruitment_viewJobVacancy")
    position_number_ele = ("xpath", "//input[@id='addJobVacancy_noOfPositions']")
    desc_ele = ("xpath", "//textarea[@id='addJobVacancy_description']")


    def __init__(self, browser):
        super(Vacancy, self).__init__(browser)
        self.switch_main_menu('Recruitment')
        Log.info("Arrive Recruitment page")
        self.recruitment = Recruitment(browser)

    def click_vacancies_menu(self):
        self.get_element(self.vacancy_ele).click()

    def delete_vacancies(self, vacan_name):
        """
        delete candidates
        """
        self.recruitment.click_menu('Vacancies')
        Log.info("Arrive Cacancies page")
        tvacan_xpath = self.tvacan_xpath.format(vacan_name)
        tvacan = ('xpath', tvacan_xpath)
        vacan = self.get_element(tvacan)
        if vacan is not None:
            self.click(tvacan)
            self.click(self.delete_btn)
            self.click(self.vdelete_btn)
            Log.info('Vacancies record cleaned up')

    def add_vacancies_required(self, jobtitle, vacancyname, hiringmanager, positionNo, desc):
        """
        Add vacancies
        1. input job title
        2. input vacancy name
        3. input hiring manager
        4. click save button
        """
        self.recruitment.click_menu('Vacancies')
        self.click(self.add_btn)
        self.set_combox_value(jobtitle, self.job_title)
        self.clear_text(self.vacan_name)
        self.input_text(vacancyname, self.vacan_name)
        self.clear_text(self.hiring_manager)
        self.input_text(hiringmanager, self.hiring_manager)
        self.input_text(positionNo, self.position_number_ele)
        self.input_text(desc, self.desc_ele)
        self.click(self.save_btn)
        Log.info("Vacancies record added")


