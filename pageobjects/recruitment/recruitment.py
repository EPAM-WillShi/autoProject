# -*- coding: utf-8 -*-
from pageobjects.mainpage import MainPage
from lib.log import Log

class Recruitment(MainPage):
    """
    Recruitment page main components
    """
    def __init__(self, browser):
        super(Recruitment, self).__init__(browser)
        self.switch_main_menu("Recruitment")
        Log.info("Arrive Recruitment page") 

    def click_menu(self, menuname):
        """
        Click ADMIN page menu
        """   
        Log.info("Click the % s menu") 
        menu_name =  menuname.title() 
        try:
            element = self.get_element(("link_text", menu_name)) 
            element.click()
        except BaseException, e:
            print e
            Log.error(e)