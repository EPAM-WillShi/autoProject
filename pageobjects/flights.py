# -*- coding: utf-8 -*-

from pageobjects.mainpage import MainPage
from lib.log import Log


class Flights(MainPage):
    """
    Flights page
    """
    def __init__(self, browser):
        super(Flights, self).__init__(browser)

