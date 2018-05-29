# -*- coding: utf-8 -*-

from pageobjects.mainpage import MainPage
from lib.log import Log


class Hotels(MainPage):
    """
    Flights page
    """
    def __init__(self, browser):
        super(Hotels, self).__init__(browser)