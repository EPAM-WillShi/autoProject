# -*- coding: utf-8 -*-
from pageobjects.mainpage import MainPage
from lib.log import Log


class Leave(MainPage):
    """
    Leave page main components
    """
    menuBar = ".//*[@id='{}']"
    
    def __init__(self, browser):
        super(Leave, self).__init__(browser)
        self.switch_main_menu("Leave")
        Log.info("Arrive Leave page")
    
    def click_menu(self, menuname):
        """
        Click Leave page menu
        """   
        Log.info("Click the % s menu") 
        menu_name =  menuname.title() 
        try:
            element = self.get_element(("link_text", menu_name)) 
            element.click()
        except:
            if menuname == "Leave Entitlements and Usage Report":
                newmenu = "menu_leave_{}".format("viewLeaveBalanceReport")
            else:
                newmenu = "menu_leave_{}".format(menuname)
            menu = self.menuBar.format(newmenu)
            try:
                element = self.get_element(("xpath", menu))
                element.click()
            except BaseException, e:
                print e
                Log.error(e)