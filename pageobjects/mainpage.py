# -*- coding: utf-8 -*-
'''
Created on 2018/4/12

@author: Angelia_Yao
'''

from lib.basepage import BasePage
from lib.log import Log


class MainPage(BasePage):
    """
    Main page of HRM
    """
    menu = '//b[text()="{}"]'
    dash_menu = menu.format("Dashboard")
    admin_menu = menu.format("Admin")
    pim_menu = menu.format("PIM")
    dir_menu = menu.format("Directory")
    per_menu = menu.format("Performance")
    recr_menu = menu.format("Recruitment")
    time_menu = menu.format("Time")
    leave_menu = menu.format("Leave")
    welcome_butt = ("xpath",".//*[@id='welcome']")
    
    def __init__(self, browser):
        super(MainPage, self).__init__(browser)
        Log.info("Arrive Default page of HRM")   
        
    def switch_main_menu(self, menuname):
        """
        Click the menu we want to get
        """
        menuname = menuname.lower().strip()
        if menuname == "admin":
            menu = self.admin_menu
        elif menuname == "pim":
            menu = self.pim_menu
        elif menuname == "leave":
            menu = self.leave_menu
        elif menuname == "time":
            menu = self.time_menu
        elif menuname == "recruitment":
            menu = self.recr_menu  
        elif menuname == "performance":
            menu = self.per_menu
        elif menuname == "dashboard":
            menu = self.dash_menu   
        elif menuname == "directory":
            menu = self.dir_menu
        else:
            print "Didn't find the menu %s" % menuname
            exit(1)        
        targetMenu = self.wait_unit_el_present(("xpath",menu))
        if targetMenu is not None:
            self.click(("xpath", menu))  
                         
    def log_out(self): 
        welcomeBut = self.wait_unit_el_present(self.welcome_butt)
        if welcomeBut is not None:
            self.click(self.welcome_butt)
            Log.info("Welcome Button is clicked")
            element = self.get_element(("link_text","Logout")) 
            element.click()
            Log.info("Log out the system successfully!")