# -*- coding: utf-8 -*-

from pageobjects.mainpage import MainPage
from lib.log import Log


class Cars(MainPage):
    """
    Flights page
    """
    def __init__(self, browser):
        super(Cars, self).__init__(browser)