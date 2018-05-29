# -*- coding: utf-8 -*-
from pageobjects.mainpage import MainPage
from lib.log import Log

class Performance(MainPage):
    """
    Performance page main components
    """
    menuBar = ".//*[@id='{}']"
    
    def __init__(self, browser):
        super(Performance, self).__init__(browser)
        self.switch_main_menu("Performance")
        Log.info("Arrive Performance page")   

    def click_menu(self, menuname):
        """
        Click ADMIN page menu
        """   
        Log.info("Click the % s menu") 
        if menuname == "Configure":
            newmenu = "menu_performance_{}".format("Configure")
        elif menuname =="KPIs":
            newmenu = "menu_performance_searchKpi"
        elif menuname =="Trackers":
            newmenu = "menu_performance_addPerformanceTracker"
        elif menuname == "Manage Reviews":
            newmenu = "menu_performance_ManageReviews"
        elif menuname =="Employee Trackers":
            newmenu = "menu_performance_viewEmployeePerformanceTrackerList"
        else:
            newmenu = "menu_performance_{}".format(menuname)
        menu = self.menuBar.format(newmenu)    
        try:
            element = self.wait_unit_el_present(("xpath", menu))
            element.click()
        except BaseException, e:
            print e
            Log.error(e)
            raise "Element %s not found" %menuname  