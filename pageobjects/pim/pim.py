# -*- coding: utf-8 -*-
from pageobjects.mainpage import MainPage
from lib.log import Log


class PIM(MainPage):
    """
    PIM page main components
    """
    menuBar = ".//*[@id='{}']"

    
    def __init__(self, browser):
        super(PIM, self).__init__(browser)
        self.switch_main_menu("PIM")
        Log.info("Arrive PIM page")   
       
    def click_menu(self, menuname):
        """
        Click PIM page menu
        """     
        Log.info("Click the %s menuname") 
        menu_name =  menuname.title() 
        try:
            element = self.get_element(("link_text", menu_name)) 
            element.click()
        except:  
            if menu_name == "Optional Fields":
                newmenu = "menu_pim_{}".format("configurePim")
            else:
                newmenu = "menu_pim_{}".format(menuname)
            menu = self.menuBar.format(newmenu) 
            try:
                element = self.get_element(("xpath", menu))
                element.click()
            except BaseException, e:
                print e
                Log.error(e)
                raise "Element %s not found" %menuname 

        


        
    

    