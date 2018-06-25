# -*- coding: utf-8 -*-
from pageobjects.mainpage import MainPage
from lib.log import Log

class Time(MainPage):
    """
    Time page main components
    """
    menuBar = ".//*[@id='{}']"
    
    def __init__(self, browser):
        super(Time, self).__init__(browser)
        self.switch_main_menu("Time")
        Log.info("Arrive Time page") 
         
    def click_menu(self, menuname):
        """
        Click Time page menu
        """   
        Log.info("Click the % s menu") 
        menu_name =  menuname.title() 
        try:
            element = self.get_element(("link_text", menu_name)) 
            element.click()
        except:
            if menuname == "Configuration":
                newmenu = "menu_attendance_configure"
            elif menuname == "Reports":
                newmenu = "menu_time_Reports"
            else:
                newmenu = "menu_time_{}".format(menuname)
            menu = self.menuBar.format(newmenu)    
            try:
                element = self.get_element(("xpath", menu))
                element.click()
            except BaseException, e:
                print e
                Log.error(e)
                raise Exception("Element %s not found" % menuname)
