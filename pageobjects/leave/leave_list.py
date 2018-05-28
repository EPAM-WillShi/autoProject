# -*- coding: utf-8 -*-
"""
Created on 2018/4/25
@author: Yolanda Zhang
"""

from lib.log import Log
from pageobjects.leave.leave import Leave
import datetime


class LeaveList(Leave):
    """
     Leave list page main components
     """
    fdate = ('id', 'calFromDate')
    tdate = ('id', 'calToDate')
    emp_name = ('id', 'leaveList_txtEmployee_empName')
    sub_unit = ('id', 'leaveList_cmbSubunit')
    checkbox = ('xpath', "//input[@type= 'checkbox']")
    checkbox_label = ('xpath', "//input[@type= 'checkbox']/preceding-sibling::label")

    default_checkbox = ('id', 'leaveList_chkSearchFilter_1')
    all = ('id', 'leaveList_chkSearchFilter_checkboxgroup_allcheck')
    include_past_emp = ('id', 'leaveList_cmbWithTerminated')
    search_btn = ('id', 'btnSearch')
    reset_btn = ('id', 'btnReset')

    rtable = ('id', "resultTable")

    def __init__(self, browser):
        super(LeaveList, self).__init__(browser)
        self.click_menu("Leave List")
        Log.info("Arrive leave list page!")

    def search_leave(self, name, fdate, tdate):
        """
        search function: fill in criteria to search
        """
        Log.info("Start search function!")
        self.clear_text(self.fdate)
        self.input_text(fdate, self.fdate)
        self.clear_text(self.tdate)
        self.input_text(tdate, self.tdate)
        # self.wait(2)
        self.click(self.all)
        self.clear_text(self.emp_name)
        self.input_text(name, self.emp_name)
        # self.wait(2)
        self.click(self.search_btn)

    def verify_search_result(self, value, fdate, tdate):
        """
        verify search function: verify search result is correct
        """
        Log.info("Verify search result!")
        table = self.get_element(self.rtable)
        table_rows = table.find_elements_by_tag_name("tr")
        Log.info("Total Rows: %d" % len(table_rows))
        if len(table_rows) >= 1:
            for table_num in range(1, len(table_rows)):
                table_text = table_rows[table_num].find_elements_by_tag_name("td")[1].text
                table_date = table_rows[table_num].find_elements_by_tag_name("td")[0].text
                date = datetime.datetime.strptime(table_date.split(' ')[0], '%Y-%m-%d')
                assert value in table_text
                assert fdate <= date <= tdate
        else:
            Log.info("No result is displayed!")

    def reset_search(self):
        """
        reset search function
        """
        Log.info("Click reset button!")
        self.click(self.reset_btn)

    def verify_reset_function(self):
        """
        verify reset search function: check all the default values
        """
        assert "2018-01-01" == self.get_element_attribute(self.fdate, "value")
        assert "2019-12-31" == self.get_element_attribute(self.tdate, "value")
        assert "All" == self.get_first_select(self.sub_unit)
        checkbox_list = self.get_elements(self.checkbox)
        checkbox_label = self.get_elements(self.checkbox_label)
        result1 = []
        result2 = []
        for i in iter(checkbox_list):
            result1.append(i.is_selected())
        for j in iter(checkbox_label):
            result2.append(j.text)
        mydict = dict(zip(result2, result1))
        Log.info("Status for all check box: %s" % mydict)
        assert mydict["Pending Approval"] == True
