# -*- coding: utf-8 -*-
from pageobjects.pim.pim import PIM
from lib.log import Log


class TerminationReasons(PIM):
    """
    PIM page main components
    """
    # Quick Launch part
    add_bth = ('ID', 'btnAdd')
    reason_input = ('ID', 'terminationReason_name')
    save_bth = ('ID', 'btnSave')
    success_flag = ("xpath", "//div[@class='message success fadable']")

    def __init__(self, browser):
        # type: (object) -> object
        super(TerminationReasons, self).__init__(browser)
        self.click_menu("Configuration")
        self.click_menu("Termination Reasons")
        Log.info("Arrive PIM page!")

    def create_termination_reason(self, reason):
        '''
        Create termination reason
        '''
        self.click(self.add_bth)
        self.input_text(reason, self.reason_input)
        self.click(self.save_bth)
        # if self.wait_unit_el_present(self.success_flag):
        #     message1 = self.get_element_text(self.success_flag)
        # assert "Successfully Saved" in message1
        Log.info("Create Termination Reason Successfully!")






