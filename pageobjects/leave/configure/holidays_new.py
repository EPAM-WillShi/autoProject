# -*- coding: utf-8 -*-

import random
import time
from pageobjects.leave.leave import Leave
from lib.log import Log


class HolidayNew(Leave):
    """
    Holiday page search elements
    """
    date_from = ('id', 'calFromDate')
    date_to = ('id', 'calToDate')
    search_btn = ('id', 'btnSearch')
    success_flag = ('xpath', '//h1[text()="Holidays"]')
    """
    Holiday page add and edit elements
    """
    holiday_name = ('id', 'holiday_description')
    holiday_date = ('id', 'holiday_date')
    repeats_annually = ('ID', 'holiday_recurring')
    full_half_day_dropdown = ('id', 'holiday_length')
    save_btn = ('id', 'saveBtn')
    cancel_btn = ('id', 'btnCancel')
    """
    Holiday page list elements
    """
    holiday_list_row = '//*[@id="resultTable"]/tbody/tr[./td[2]/a[text()="{}"]]'
    holiday_list_check_all = ('id', 'ohrmList_chkSelectAll')
    holiday_list_checkbox = '//*[@id="resultTable"]/tbody/tr[./td[2]/a[text()="{}"]]/td[1]/input'
    holiday_text = '//*[@id="resultTable"]/tbody/tr[./td[2]/a[text()="{}"]]/td[2]/a'
    add_btn = ('id', 'btnAdd')
    delete_btn = ('id', 'btnDelete')
    confirm_delete_btn = ('id', 'dialogDeleteBtn')
    cancel_delete_btn = ('xpath', '//*[@id="deleteConfModal"]/div[3]/input[2]')
    delete_text = ('xpath', '// *[ @ id = "deleteConfModal"] / div[2] / p')
    message = ('xpath', "//div[contains(@class,'success')]")

    def __init__(self, browser):
        super(HolidayNew, self).__init__(browser)
        self.click_menu('Configure')
        self.click_menu('Holidays')
        page_ele = self.get_element(self.success_flag)
        if page_ele is not None:
            Log.info("Arrive Holidays page.")
        else:
            Log.info("Cannot arrive Holidays page.")

    @staticmethod
    def create_random_date(start_year, end_year):
        a1 = (start_year, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（XXXX-01-01 00：00：00）
        a2 = (end_year, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（XXXX-12-31 23：59：59）
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        date = time.strftime("%Y-%m-%d", time.localtime(random.randint(start, end)))
        return date

    def set_holiday_element(self):
        date = self.create_random_date(2018, 2018)
        repeats = random.choice([0, 1])
        full_or_half = random.choice(['Full Day', 'Half Day'])
        if repeats == 1:
            self.click(self.repeats_annually)
        self.input_text(date, self.holiday_date)
        self.set_combox_value(full_or_half, self.full_half_day_dropdown)
        # print(date)
        # print(repeats)
        # print(full_or_half)

    def check_holiday_list(self, name):
        list_row = self.holiday_list_row.format(name)
        list_data = self.get_elements_texts(('xpath', list_row))
        holiday_text = self.holiday_text.format(name)
        self.click(('xpath', holiday_text))
        date = self.get_element_attribute(self.holiday_date, 'value')
        full_or_half = self.get_first_select(self.full_half_day_dropdown)
        if self.get_element(self.repeats_annually).is_selected() is True:
            repeats_annually = "Yes"
        else:
            repeats_annually = "No"
        page_date = name + " " + date + " " + full_or_half + " " + repeats_annually
        if list_data[0] == page_date:
            Log.info("The holiday is correct.")
        else:
            Log.info("The holiday is incorrect.")
        self.click(self.cancel_btn)

    def add_holiday_save(self, name):
        self.click(self.add_btn)
        self.clear_text(self.holiday_name)
        self.input_text(name, self.holiday_name)
        self.set_holiday_element()
        self.click(self.save_btn)
        if "Successfully Saved" in self.get_element_text(self.message):
            Log.info("Create a " + name + " holiday and save.")
        else:
            Log.info("Create a " + name + " holiday failed")

    def add_holiday_cancel(self, name):
        self.click(self.add_btn)
        self.clear_text(self.holiday_name)
        self.input_text(name, self.holiday_name)
        self.set_holiday_element()
        self.click(self.cancel_btn)
        Log.info("Create a new holiday and cancel.")

    def delete_all_holiday(self):
        self.click(self.holiday_list_check_all)
        self.click(self.delete_btn)
        if self.get_elements_texts(self.delete_text) == ['Delete records?']:
            Log.info("Open delete confirm pop up.")
        else:
            Log.info("Can't open delete confirm pop up.")
        self.click(self.confirm_delete_btn)
        Log.info("Delete all holidays.")

    def delete_one_holiday(self, name):
        holiday_list_checkbox = self.holiday_list_checkbox.format(name)
        self.click(('xpath', holiday_list_checkbox))
        self.click(self.delete_btn)
        if self.get_elements_texts(self.delete_text) == ['Delete records?']:
            Log.info("Open delete confirm pop up.")
        else:
            Log.info("Can't open delete confirm pop up.")
        self.click(self.confirm_delete_btn)
        Log.info("Delete " + name)

    def edit_holiday(self, name):
        holiday_text = self.holiday_text.format(name)
        self.click(('xpath', holiday_text))
        self.set_holiday_element()
        self.click(self.save_btn)
        Log.info("Edit " + name + " holiday and save.")

    def search_holiday(self):
        date1 = self.create_random_date(2017, 2018)
        date2 = self.create_random_date(2017, 2018)
        if date1 >= date2:
            date_from = date2
            date_to = date1
        else:
            date_from = date1
            date_to = date2
        self.input_text(date_from, self.date_from)
        self.input_text(date_to, self.date_to)
        self.click(self.search_btn)
        Log.info("Search holidays.")







