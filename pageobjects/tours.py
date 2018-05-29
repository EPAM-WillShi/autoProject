# -*- coding: utf-8 -*-

from pageobjects.mainpage import MainPage
from lib.log import Log


class Tours(MainPage):
    """
    Flights page
    """
    def __init__(self, browser):
        super(Tours, self).__init__(browser)