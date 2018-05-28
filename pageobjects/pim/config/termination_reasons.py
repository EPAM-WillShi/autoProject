'''
Created on 2018��4��27��

@author: Angelia_Yao
'''
# -*- coding: utf-8 -*-
from pageobjects.pim.pim import PIM
from lib.log import Log


class TerminationReasons(PIM):
    """
    PIM TerminationReasons page main components
    """
    # Quick Launch part
    add_bth = ('ID', 'btnAdd')
    reason_input = ('ID', 'terminationReason_name')
    save_bth = ('ID', 'btnSave')
    success_flag = ("xpath", ".//*[@linkText='test']")
    #success_flag2 = ("xpath", "//div[@class='message success fadable']")
    
    def __init__(self, browser):
        # type: (object) -> object
        super(TerminationReasons, self).__init__(browser)
        self.sleep(10)
        self.click_menu("Configuration")
        self.click_menu("Termination Reasons")
        Log.info("Enter the Termination Reasons page")

    def create_termination_reason(self, reason):
        '''
        Create termination reason
        '''
        self.click(self.add_bth)
        self.input_text(reason, self.reason_input)
        self.click(self.save_bth)
        assert self.is_element_visible(self.success_flag)
        Log.info("Create Termination Reason Successfully!")



