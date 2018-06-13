# -*- coding: utf-8 -*-
"""
Created on 2018/5/29
@author: Joanna Li
"""
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lib.log import Log
from pageobjects.admin.admin import Admin


class WorkShifts(Admin):
    """
    Work Shifts page
    """
    # work shifts main page objects
    shiftspage_title = ('xpath', "//h1[text()='Work Shifts']")
    add_btn = ('ID', 'btnAdd')
    delete_btn = ('ID', 'btnDelete')

    # add work shifts page object
    add_edit_flag = ('ID', 'workShiftHeading')
    shift_name = ('ID', 'workShift_name')
    workhour_from = ('ID', 'workShift_workHours_from')
    workhour_to = ('ID', 'workShift_workHours_to')
    time_rang = ('CLASS_NAME', 'time_range_duration')
    selectEle = ('ID', 'workShift_availableEmp')
    selectoptions = ('xpath', '//select[@id="workShift_availableEmp"]/option')
    startpart = 0.2
    endpart = 0.3
    assignEle = ('ID', 'workShift_assignedEmp')
    add_employee_btn = ('ID', 'btnAssignEmployee')
    remove_employee_btn = ('ID', 'btnRemoveEmployee')
    save_btn = ('ID', 'btnSave')
    cancel_btn = ('ID', 'btnCancel')
    namelink = '//a[text()="{}"]'
    frompath = '//a[text()="{}"]/../../td[3]'
    topath = '//a[text()="{}"]/../../td[4]'
    durationpath = '//a[text()="{}"]/../../td[5]'
    message = ('XPATH', '//*[@class="message success fadable"]')

    # delete objects
    ok_btn = ('ID', 'dialogDeleteBtn')
    element = '//a[text()="{}"]/../../td[1]/input'

    def __init__(self, browser):
        super(WorkShifts, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Work Shifts")
        self.wait_unit_el_present(self.shiftspage_title)
        self.wait_unit_el_present(self.add_btn)
        Log.info("Arrive at Work shift page and shows normally")

    def add_one_work_shift(self, add_name, workhourfrom, workhourto):
        """
        Add a new work shift only select one employee
        """
        Log.info("Start to add a work shift only assigning one employee")
        self.click(self.add_btn)
        assert self.get_element_text(self.add_edit_flag) == 'Add Work Shift'
        self.input_text(add_name, self.shift_name)
        self.set_combox_value(workhourfrom, self.workhour_from)
        self.set_combox_value(workhourto, self.workhour_to)
        if self.check_employee_exists(self.selectEle) != 0:
            self.select_option(self.selectEle, 0)
            self.click(self.add_employee_btn)
            self.click(self.save_btn)
            self.assert_message("Successfully Saved")
            Log.info("Add a new shift only with one employee successfully")
        else:
            self.click(self.save_btn)
            self.assert_message("Successfully Saved")
            Log.info("Add a new shift without assigning employee successfully because there is no one in list")

    def add_multiple_work_shift(self, add_name, workhourf, workhourt, workdur):
        """
        Add a new work shift select all employees
        """
        self.sleep(2)
        Log.info("Start to add a work shift assigning multiple employees")
        self.click(self.add_btn)
        assert self.get_element_text(self.add_edit_flag) == 'Add Work Shift'
        if self.check_employee_exists(self.selectEle) != 0:
            self.input_text(add_name, self.shift_name)
            self.set_combox_value(workhourf, self.workhour_from)
            self.set_combox_value(workhourt, self.workhour_to)
            self.assign_mutilple_work_shift()
            self.click(self.save_btn)
            self.assert_message("Successfully Saved")
            assert self.get_element(('xpath', self.namelink.format(add_name)))
            self.verify_shift_fields(add_name, workhourf, workhourt, workdur)
            Log.info("Add a new shift with multiple employees successfully")
        else:
            Log.info("There is no employee to assign, do nothing")

    def assign_mutilple_work_shift(self):
        """
        Select multiple employees in available employees and assign
        """
        Log.info('Start to select mutiple employees')
        select = self.get_element(self.selectEle)
        empoptions = select.find_elements_by_tag_name('option')
        startsel = int(len(empoptions) * self.startpart)
        endsel = int((len(empoptions) * self.endpart))
        ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        for no in xrange(startsel, endsel):
            self.select_option(self.selectEle, no)
        ActionChains(self.driver).key_up(Keys.CONTROL).perform()
        Log.info("Multiple employees are selected")
        self.click(self.add_employee_btn)
        try:
            select = self.get_element(self.assignEle)
            assignemp = select.find_elements_by_tag_name('option')
            assert len(assignemp) == (endsel-startsel)
            Log.info("The selected employees assigned to successfully")
        except Exception:
            Log.info("The selected employees failed to assign")

    def remove_multiple_work_shift(self):
        """
        Select employee in assigned employees list and remove
        """
        Log.info('Start to remove mutiple employees')
        select = self.get_element(self.assignEle)
        empoptions_orig = select.find_elements_by_tag_name('option')
        startsel = int(len(empoptions_orig) * self.startpart)
        endsel = int((len(empoptions_orig) * self.endpart))
        ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        for no in xrange(startsel, endsel):
            self.select_option(self.assignEle, no)
        ActionChains(self.driver).key_up(Keys.CONTROL).perform()
        Log.info("Multiple employees are removed")
        self.click(self.remove_employee_btn)
        empoptions_curr = select.find_elements_by_tag_name('option')
        assert len(empoptions_curr) == (len(empoptions_orig)-(endsel - startsel))
        Log.info("The selected employees removed back successfully")

    def check_employee_exists(self, ele):
        """
        Check if there is employee existing in Available employee list
        """
        Log.info('Start to check if there are employees in available employee list')
        try:
            select = self.get_element(ele)
            empno = len(select.find_elements_by_tag_name('option'))
            return empno
        except NoSuchElementException:
            Log.info('There is no employee in %s list' %ele)
            return 0

    def verify_shift_fields(self, shift_name, workhourf, workhourt, workduration):
        """
        Verify whether work_from hour and work_to hour and duration show correctly in table
        """
        Log.info('Start to verify if all fields in table match added or updated work shift')
        shiftdict = self.get_all_fields(shift_name)
        # fselector = ('xpath', self.frompath.format(shift_name))
        # fromh = self.get_element(fselector).text
        # tselector = ('xpath', self.topath.format(shift_name))
        # toh = self.get_element(tselector).text
        # dselector = ('xpath', self.durationpath.format(shift_name))
        # durationh = self.get_element(dselector).text
        assert shiftdict['shiftfromhour'] == workhourf
        Log.info('The From hour is showing in table correctly')
        assert shiftdict['shifttohour'] == workhourt
        Log.info('The To hour is showing in table correctly')
        assert shiftdict['shiftduration'] == '{:.2f}'.format(float(workduration))
        Log.info('The duration is showing in table correctly')

    def get_all_fields(self, shift_name):
        """
        Get value for each field in shift table
        """
        Log.info('Start to get all work shift in table')
        fselector = ('xpath', self.frompath.format(shift_name))
        fromh = self.get_element(fselector).text
        tselector = ('xpath', self.topath.format(shift_name))
        toh = self.get_element(tselector).text
        dselector = ('xpath', self.durationpath.format(shift_name))
        durationh = self.get_element(dselector).text
        shift_dict = {'shiftname': shift_name,'shiftfromhour':fromh,'shifttohour':toh,'shiftduration':durationh}
        return shift_dict

    def edit_work_shit(self, orig_name, edit_name, edit_workhourf, edit_workhourt, edit_duration):
        """
        Edit work shift when click shift name in table
        """
        self.sleep(2)
        Log.info('Start to edit a work shift after clicking shift name in table')
        # shiftdict = self.get_all_fields(orig_name)
        selector = ('xpath', self.namelink.format(orig_name))
        self.click(selector)
        self.sleep(3)
        assert self.get_element(self.add_edit_flag).text == 'Edit Work Shift'
        self.input_text(edit_name, self.shift_name)
        self.set_combox_value(edit_workhourf, self.workhour_from)
        self.set_combox_value(edit_workhourt, self.workhour_to)
        if self.check_employee_exists(self.assignEle) != 0:
            self.remove_multiple_work_shift()
        if self.check_employee_exists(self.selectEle) != 0:
            self.select_option(self.selectEle, 0)
            self.click(self.add_employee_btn)
        self.click(self.save_btn)
        self.verify_shift_fields(edit_name, edit_workhourf, edit_workhourt, edit_duration)
        Log.info("Update a work shift only with one employee successfully")

    def delete_work_shift(self, shift_name):
        """
        Delete work shift
        """
        self.sleep(2)
        Log.info("Start to delete a work shift")
        checkbox = self.element.format(shift_name)
        ielement = ('XPATH', checkbox)
        self.click(ielement)
        self.sleep(2)
        self.click(self.delete_btn)
        self.sleep(2)
        self.click(self.ok_btn)
        self.assert_message("Successfully Deleted")
        assert (self.get_element(('xpath', self.namelink.format(shift_name))) is None)
        Log.info("The work shift: %s is deleted successfully" %shift_name)

    def assert_message(self, return_message):
        """
        Assert the result of current operation
        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)

