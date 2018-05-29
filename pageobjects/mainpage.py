# -*- coding: utf-8 -*-
'''
Created on 2018/4/12

@author: Angelia_Yao
'''

from lib.basepage import BasePage
from lib.log import Log


class MainPage(BasePage):
    """
    Main page
    """
    menu_ele = '//a[contains(@href,"/{}")]'

    
    def __init__(self, browser):
        super(MainPage, self).__init__(browser)
        Log.info("Arrive Default page of HRM")

    def switch_main_menu(self, menu):
        """
        Click the menu we want to get
        """
        menu_lower = menu.lower().strip()
        menu_name = self.menu_ele.format(menu_lower)
        targetMenu = self.get_element(("xpath", menu_name))
        if targetMenu is not None:
            self.click(("xpath", menu_name))
        else:
            print "Didn't find the menu %s" % menu
            exit(1)

    def log_out(self): 
        welcomeBut = self.wait_unit_el_present(self.welcome_butt)
        if welcomeBut is not None:
            self.click(self.welcome_butt)
            Log.info("Welcome Button is clicked")
            element = self.get_element(("link_text","Logout")) 
            element.click()
            Log.info("Log out the system successfully!")