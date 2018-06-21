# -*- coding: utf-8 -*-
"""
Created on 2018/4/25
@author: Yolanda Zhang
"""

from lib.log import Log
from pageobjects.leave.leave import Leave
import datetime
from pageobjects.pim.emplist_job import Job


class LeaveList(Leave):
    """
     Leave list page main components
     """
    fdate = ('id', 'calFromDate')
    tdate = ('id', 'calToDate')
    validate = ('xpath', "//span[text() = 'To date should be after from date']")
    emp_name = ('id', 'leaveList_txtEmployee_empName')
    sub_unit = ('id', 'leaveList_cmbSubunit')
    checkbox = ('xpath', "//input[@type= 'checkbox']")
    checkbox_label = ('xpath', "//input[@type= 'checkbox']/preceding-sibling::label")

    default_checkbox = ('id', 'leaveList_chkSearchFilter_1')
    all = ('id', 'leaveList_chkSearchFilter_checkboxgroup_allcheck')
    include_past_emp = ('id', 'leaveList_cmbWithTerminated')
    search_btn = ('id', 'btnSearch')
    reset_btn = ('id', 'btnReset')

    status_box = "leaveList_chkSearchFilter_{}"
    status_label = "//label[@for = 'leaveList_chkSearchFilter_{}']"

    rtable = ('id', "resultTable")
    no_record_flag = ('xpath', "//td[text() = 'No Records Found']")

    label_name = ''

    def __init__(self, browser):
        super(LeaveList, self).__init__(browser)
        self.click_menu("Leave List")
        Log.info("Arrive leave list page!")

    def search_leave(self, name, fdate, tdate):
        """
        search function: fill in criteria to search
        """
        Log.info("Start search function!")
        self.input_text(fdate, self.fdate)
        self.input_text(tdate, self.tdate)
        self.click(self.all)
        self.input_text(name, self.emp_name)
        self.click(self.search_btn)

    # def verify_search_result(self, value, fdate, tdate):
    #     """
    #     verify search function: verify search result is correct
    #     """
    #     Log.info("Verify search result!")
    #     table = self.get_element(self.rtable)
    #     table_rows = table.find_elements_by_tag_name("tr")
    #     Log.info("Total Rows: %d" % len(table_rows))
    #     if len(table_rows) >= 1:
    #         for table_num in range(1, len(table_rows)):
    #             acutal_emp_name = table_rows[table_num].find_elements_by_tag_name("td")[1].text
    #             acutal_date = table_rows[table_num].find_elements_by_tag_name("td")[0].text
    #             date = datetime.datetime.strptime(acutal_date.split(' ')[0], '%Y-%m-%d')
    #             actual_status = table_rows[table_num].find_elements_by_tag_name("td")[5].text
    #             assert value in acutal_emp_name
    #             assert fdate <= date <= tdate
    #             print actual_status
    #     else:
    #         Log.info("No result is displayed!")

    def verify_search_result(self, *args):
        table = self.get_element(self.rtable)
        table_rows = table.find_elements_by_tag_name("tr")
        Log.info("Total Rows: %d" % len(table_rows))
        page_ele = self.get_element(self.no_record_flag)
        if page_ele is not None:
            Log.info("no record....")
        else:
            if len(table_rows) >= 1:
                for table_num in range(1, len(table_rows)):
                    acutal_emp_name = table_rows[table_num].find_elements_by_tag_name("td")[1].text
                    acutal_date = table_rows[table_num].find_elements_by_tag_name("td")[0].text
                    date = datetime.datetime.strptime(acutal_date.split(' ')[0], '%Y-%m-%d')
                    actual_status = table_rows[table_num].find_elements_by_tag_name("td")[5].text
                    if len(args) == 1:
                        while args[0] in acutal_emp_name:
                            Log.info("Find the past emp!")
                            break
                    elif len(args) == 2:
                        assert args[0] <= date <= args[1]
                    elif len(args) == 0:
                        assert self.label_name in actual_status
                    else:
                        assert args[0] <= date <= args[1]
                        assert args[2] in acutal_emp_name

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

    def search_by_status(self, value):
        # self.click(self.default_checkbox)
        status = self.status_box.format(value)
        ielement = ('id', status)
        name = self.status_label.format(value)
        name_ele = ('xpath', name)
        self.click(ielement)
        self.label_name = self.get_element_text(name_ele)
        self.click(self.search_btn)
        self.click(ielement)
        self.wait(2)

    def search_by_date(self, fdate, tdate):
        self.input_text(fdate, self.fdate)
        self.input_text(tdate, self.tdate)
        if fdate > tdate:
            page_ele = self.get_element(self.validate)
            if page_ele is not None:
                Log.info("To date should be after from date!")
                self.input_text(tdate, self.tdate)
        self.click(self.all)
        self.click(self.search_btn)

    def search_by_subunit(self, value):
        self.click(self.all)
        self.set_combox_value(value, self.sub_unit)
        self.click(self.search_btn)

    def search_by_emp_status(self):
        self.click(self.all)
        self.click(self.include_past_emp)
        self.click(self.search_btn)
        self.wait(6)

    def terminate_emp(self, fname, lname, terdate):
        self.job = Job(self.driver)
        self.job.open_job_page_via_editing_emp(fname, lname)
        self.job.terminate_employment(terdate)
