# -*- coding: utf-8 -*-
"""
Created on 2018/6/6
@author: Molly Xue
"""

from decimal import *
from lib.log import Log
from pageobjects.admin.admin import Admin


class PayGrades(Admin):
    """
    Pay Grades page
    """
    # Define declaration for Page Grades Page
    add_btn = ('ID', 'btnAdd')
    delete_btn = ('ID', 'btnDelete')
    message = ('XPATH', "//*[@class='message success fadable']")
    pay_grade_list = ('XPATH', "//td[2]")
    element = '//a[text()="{}"]/../../td[1]/input'

    # Define declaration for Add Pay Grade
    name = ('ID', 'payGrade_name')
    save_btn = ('ID', 'btnSave')
    cancel_btn = ('ID', 'btnCancel')

    # Define declaration for Assigned Currencies
    currency_add_btn = ('ID', 'btnAddCurrency')
    currency_box = ('ID', 'payGradeCurrency_currencyName')
    min_salary = ('ID', 'payGradeCurrency_minSalary')
    max_salary = ('ID', 'payGradeCurrency_maxSalary')
    currency_save_btn = ('ID', 'btnSaveCurrency')
    add_currency = '//a[text()="{}"]/../../td[3]'
    add_min_sal = '//a[text()="{}"]/../../td[3]'
    add_max_sal = '//a[text()="{}"]/../../td[4]'

    # Define declaration for Delete confirmation dialog
    del_ok_btn = ('ID', 'dialogDeleteBtn')
    del_cancel_btn = ('XPATH', "//input[@value='Cancel']")

    def __init__(self, browser):
        super(PayGrades, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Pay Grades")
        Log.info("Arrive Admin Pay Grades page")

    def cancel_adding_pay_grades(self, add_name):
        """
        Try to cancel adding a pay grade

        """
        Log.info("Start to cancel adding a pay grade")
        self.click(self.add_btn)
        self.clear_text(self.name)
        self.input_text(add_name, self.name)
        self.sleep(1)
        self.click(self.cancel_btn)
        self.sleep(1)
        assert not add_name in self.get_elements_texts(self.pay_grade_list)
        Log.info("Add operation is being canceled successfully")

    def add_pay_grades(self, add_name):
        """
        Try to add a pay grade

        """
        Log.info("Start to add a pay grade")
        self.click(self.add_btn)
        self.clear_text(self.name)
        self.input_text(add_name, self.name)
        self.sleep(1)
        self.click(self.save_btn)
        self.sleep(2)
        Log.info("Add a pay grade successfully")

    def click_cancel_button(self):
        """
        Click on cancel button in Add Pay Grade page

        """
        self.click(self.cancel_btn)

    def edit_pay_grades_name(self, add_name, modify_name):
        """
        Edit the name of Pay Grades

        """
        Log.info("Start to edit Pay Grade name")
        edit_element = ('LINK_TEXT', add_name)
        self.click(edit_element)
        self.sleep(1)
        self.click(self.save_btn)
        self.sleep(1)
        self.clear_text(self.name)
        self.input_text(modify_name, self.name)
        self.sleep(1)
        self.click(self.save_btn)
        Log.info("Edit action completed")

    def edit_pay_grades_add_currency(self, modify_name, currency_name, min_sal, max_sal):
        """
        Add a currency for the Pay Grade

        """
        Log.info("Start to add a currency to Pay Grade")
        edit_element = ('LINK_TEXT', modify_name)
        self.sleep(1)
        self.click(edit_element)
        self.sleep(1)
        self.click(self.currency_add_btn)
        self.sleep(1)
        self.clear_text(self.currency_box)
        self.input_text(currency_name, self.currency_box)
        self.sleep(1)
        self.input_text(min_sal, self.min_salary)
        self.sleep(1)
        self.input_text(max_sal, self.max_salary)
        self.sleep(1)
        self.click(self.currency_save_btn)
        Log.info("Add a currency to Pay Grade action completed")

    def check_currency_addto_edit(self, currency_name, min_sal, max_sal):
        """
        Check the currency is added in the Assign Currency list

        """
        Log.info("Start to check currency add to edit for pay grades")
        currency = str(currency_name)[6:]
        col_name = ('LINK_TEXT', currency)
        min_salary = ("XPATH", self.add_min_sal.format(currency))
        max_salary = ("XPATH", self.add_max_sal.format(currency))
        added_min_salary = self.get_element_text(min_salary).encode("utf-8").replace(",", "")
        added_max_salary = self.get_element_text(max_salary).encode("utf-8").replace(",", "")
        assert self.get_element(col_name).is_displayed
        assert Decimal(added_min_salary) == Decimal(min_sal)
        assert Decimal(added_max_salary) == Decimal(max_sal)
        Log.info("Currency is added to edit for pay grades successfully")

    def check_currency_addto_paygrades(self, modify_name, currency_name):
        """
        Check the currency is added in the pay grade main page

        """
        Log.info("Start to check currency add to pay grades")
        add_currency = str(currency_name)[6:]
        assign_currency = self.add_currency.format(modify_name)
        self.sleep(2)
        ele = ('XPATH', assign_currency)
        assert add_currency == self.get_element_text(ele).encode("utf-8")
        Log.info("Currency is added successfully in Pay Grades successfully")

    def cancel_delete_pay_grades(self, modify_name):
        """
        Cancel deleting a pay grade

        """
        Log.info("Start to check and then try to delete a pay grade and final cancel action")
        checkbox = self.element.format(modify_name)
        self.click(('XPATH', checkbox))
        self.click(self.delete_btn)
        self.wait_unit_el_present(self.del_cancel_btn)
        self.click(self.del_cancel_btn)
        assert modify_name in self.get_elements_texts(("XPATH", "//td[2]"))
        self.click(('XPATH', checkbox))
        Log.info("Delete operation is being canceled successfully")

    def delete_pay_grades(self, modify_name):
        """
        delete a pay grade

        """
        Log.info("Start to delete a pay grade")
        checkbox = self.element.format(modify_name)
        self.click(('XPATH', checkbox))
        self.click(self.delete_btn)
        self.wait_unit_el_present(self.del_ok_btn)
        self.click(self.del_ok_btn)
        Log.info("Delete a pag grade successfully")

    def assert_message(self, return_message):
        """
        Assert the result of current operation
        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)