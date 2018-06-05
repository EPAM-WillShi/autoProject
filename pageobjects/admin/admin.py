# -*- coding: utf-8 -*-
from pageobjects.mainpage import MainPage
from lib.log import Log


class Admin(MainPage):
    """
    Admin page main components
    """
    menuBar = ".//*[@id='{}']"
    
    def __init__(self, browser):
        super(Admin, self).__init__(browser)
        self.switch_main_menu("Admin")    
        Log.info("Arrive Admin page") 
            
    def click_menu(self, menuname):
        """
        Click ADMIN page menu
        """   
        Log.info("Click the % s menu") 
        menu_name =  menuname.title() 
        try:
            element = self.get_element(("link_text", menu_name)) 
            element.click()
            self.sleep(1)
        except:
            if menuname == "Employment Status":
                newmenu = "menu_admin_{}".format("employmentStatus")
            else:
                newmenu = "menu_admin_{}".format(menuname)
            menu = self.menuBar.format(newmenu)    
            try:
                element = self.get_element(("xpath", menu))
                element.click()
            except BaseException, e:
                print e
                Log.error(e)
                raise "Element %s not found" %menuname  