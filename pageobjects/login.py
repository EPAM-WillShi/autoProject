# -*- coding: utf-8 -*-

from lib.basepage import BasePage
from lib.log import Log

class Login(BasePage):
    """
    login page
    """
    user_name = ('ID', 'txtUsername')
    password = ('ID', 'txtPassword')
    login_btn = ('ID', 'btnLogin')
    success_flag =("xpath", ".//*[@id='welcome']")
    
    def __init__(self, browser):
        super(Login, self).__init__(browser)
        Log.info("Arrive Login page")   
            
    def login(self, username, passwd):
        """
        log in 
        """
        # Input user name
        self.input_text(username, self.user_name)
        # Input password
        self.input_text(passwd, self.password)
        # Click login button
        self.click(self.login_btn)

    def check_login_status(self):
        """
        Check if Welcome label is show
        """
        assert self.is_element_visible(self.success_flag) 
