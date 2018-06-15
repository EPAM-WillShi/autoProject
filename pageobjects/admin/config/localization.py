# -*- coding: utf-8 -*-
"""
Created on 2018��4��26��

@author: Angelia_Yao
"""

import random
from pageobjects.admin.admin import Admin
from lib.log import Log


class Localization(Admin):
    """
    Localization components
    """
    title = ('xpath', '//h1[text()="Localization"]')
    language = ('id', 'localization_dafault_language')
    language_box = ('id', 'localization_use_browser_language')
    supp_language = ('xpath', '//a[@class="btn1"]')
    date_format = ('id', 'localization_default_date_format')
    link = ('xpath', '//a[@href="http://www.orangehrm.com/localization-help.shtml"]')
    edit_btn = ('xpath', '//input[@value="Edit"]')
    save_btn = ('xpath', '//input[@value="Save"]')
    Ok_btn = ('xpath', '//input[@value="Ok"]')
    link_lang = ('id', 'languageList')
    link_group = ('id', 'add_label_language_group_id')
    window_name = 'Orange - Localizit'
    download_btn = ('id', 'downloadDictionary')

    def __init__(self, browser):
        super(Localization, self).__init__(browser)

    def select_randm_list(self, keys):
        value = self.get_element_text(keys).encode('utf-8')
        value_list = value.rsplit('\n')
        print value_list
        length = len(value_list)
        print length
        if value_list[0] == '--Select--':
            num = random.randint(1, length-1)
        elif value_list[0] == '-- Month --':
            num = random.randint(1, length - 1)
        else:
            num = random.randint(0, length-1)
        print(num)
        self.select_option(keys, num)

    def switch_to_tab(self):
        handles = self.get_all_window()  # 获取所有窗口
        for handle in handles:  # 切换窗口
            if handle != self.get_current_window():
                print 'switch to second window', handle
                self.switch_to_window(handle)  # 切换到第二个窗口

    def edit_local(self, ptitle):
        assert ptitle == self.get_element_text(self.title)
        handle = self.get_current_window()
        self.click(self.edit_btn)
        self.select_randm_list(self.language)
        self.click(self.language_box)
        self.click(self.supp_language)
        self.sleep(3)
        self.click(self.Ok_btn)
        self.select_randm_list(self.date_format)
        self.click(self.link)
        self.switch_to_tab()
        self.sleep(2)
        self.close_browser()
        self.sleep(3)
        self.switch_to_window(handle)
        self.click(self.save_btn)
        Log.info("edit localization successfully")




