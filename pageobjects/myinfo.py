# -*- coding: utf-8 -*-

from mainpage import MainPage
from lib.log import Log

class MyInfo(MainPage):
    """
    MyInfo page
    """
    
    def __init__(self, browser):
        super(MyInfo, self).__init__(browser)
        Log.info("Arrive MyInfo page")   
            