# -*- coding: utf-8 -*-
"""
@author: Joanna Li
"""

from pageobjects.leave.leave import Leave
from lib.log import Log

class Holidays(Leave):
    """
    Holidays page definition
    """

    # Define declaration for add holiday
    add_button = '//input[@id="btnAdd"]'
    hname = ('ID', 'holiday_description')
    hdate = ('ID', 'holiday_date')
    hannual = ('ID', 'holiday_recurring')
    hday = ('ID', 'holiday_length')
    save_button = ('ID', 'saveBtn')
    #

    # Define declaration for search holiday
    from_date = ('ID', 'calFromDate')
    to_date = ('ID', 'calToDate')
    search_button = ('ID','btnSearch')
    linkName = '//a[text()="{}"]'
    tddate = '//td[text()={}]'
    #

    # Define declaration for edit holiday
    edit_text = ('ID', 'locationHeading')
    #

    # Define declaration for delete holiday
    delete_button = ('ID', 'btnDelete')
    dialogDeleteBtn = ('ID', 'dialogDeleteBtn')
    table_tr = '//a[text()="{}"]/../../td[1]/input'
    #

    def __init__(self, browser):
        super(Holidays, self).__init__(browser)
        self.click_menu('Configure')
        self.click_menu('Holidays')
        Log.info('Start testing Configure->Holidays')

    def click_add_button(self):
        """
        Click on Add button
        """
        add = self.wait_unit_el_present(('xpath', self.add_button))
        self.click(("xpath", self.add_button))
        assert (self.get_element(self.save_button) is not None)

    def click_annual(self, annual):
        """
        Tick checkbox
        """
        if annual:
            self.click(self.hannual)

    def add_holiday(self, name, holidaydate, annual, daytype):
        """
        Input all fields and Add holiday
        """
        Log.info('start adding a holiday')
        self.click_add_button()
        self.sleep(3)
        self.input_text(name, self.hname)
        self.click_annual(annual)
        self.set_combox_value(daytype,self.hday)
        self.clear_text(self.hdate)
        self.input_text(holidaydate, self.hdate)
        self.click(self.save_button)
        self.sleep(3)
        assert (self.get_element(("xpath", self.linkName.format(name))) is not None)

    def edit_holiday(self, originalname, name, holidaydate, daytype):
        """
        Input all fields and update holiday
        """
        Log.info('start editing a holiday')
        self.click(("xpath", self.linkName.format(originalname)))
        assert (self.get_element_text(self.edit_text) == 'Edit Holiday')
        self.clear_text(self.hname)
        self.input_text(name, self.hname)
        self.click(self.hannual)
        self.set_combox_value(daytype, self.hday)
        self.clear_text(self.hdate)
        self.input_text(holidaydate, self.hdate)
        self.click(self.save_button)
        self.sleep(2)
        assert (self.get_element(("xpath", self.linkName.format(name))) is not None)
        assert (self.get_element(("xpath", self.linkName.format(originalname))) is None)
        Log.info("Edit holiday completed")

    def search_holiday(self, appearance, fdate, tdate, names):
        """
        Search holidays according from & to date
        """
        Log.info('start searching holidays')
        self.clear_text(self.from_date)
        self.input_text(fdate, self.from_date)
        self.clear_text(self.to_date)
        self.input_text(tdate, self.to_date)
        self.click(self.search_button)
        self.sleep(3)
        for name in names:
            if appearance:
                assert (self.get_element(("xpath", self.linkName.format(name))) is not None)
            else:
                assert (self.get_element(("xpath", self.linkName.format(name))) is None)

    def delete_holiday(self, names):
        """
        Delete holidays
        """
        Log.info('start deleting holidays')
        try:
            get_name = names[0]
        except Exception:
            Log.info('The params of delete_holiday is not correct')
            raise ValueError("please transfer the correct list params,like () or []")
        for name in names:
            selector = ('xpath', self.table_tr.format(name))
            self.click(selector)
        self.click(self.delete_button)
        self.click(self.dialogDeleteBtn)
        self.sleep(3)
        for name in names:
            assert (self.get_element(("xpath", self.linkName.format(name))) is None)


