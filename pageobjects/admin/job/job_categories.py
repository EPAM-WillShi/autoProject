# -*- coding: utf-8 -*-
from pageobjects.admin.admin import Admin
from lib.log import Log

class JobCategories(Admin):
    """
    Employment Status page
    """
    def __init__(self,browser):
        super(JobCategories, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Job Categories")
        Log.info("Arrive Admin Job Categories page")