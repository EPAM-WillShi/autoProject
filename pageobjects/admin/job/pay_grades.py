# -*- coding: utf-8 -*-
"""
Created on 2018/4/26
@author: Dora Zhu
"""
from decimal import *
from lib.log import Log
from pageobjects.admin.admin import Admin


class PayGrades(Admin):
    """
    PayGrades page functions
    """
    add_btn = ('ID', 'btnAdd')
    delete_btn = ('ID', 'btnDelete')
    main_flag = ('ID', 'Pay Grades')
    add_flag = "//*[text()='Add Pay Grade']"
    edit_flag = ('ID', 'Edit Pay Grade')
    name = ('ID', 'payGrade_name')
    save_btn = ('ID', 'btnSave')
    cancel_btn = ('ID', 'btnCancel')
    add_currency = '//a[text()="{}"]/../../td[3]'

    # delete objects
    del_ok_btn = ('ID', 'dialogDeleteBtn')
    del_cancel_btn = ('XPATH', "//input[@value='Cancel']")
    message = ('XPATH', "//*[@class='message success fadable']")
    element = '//a[text()="{}"]/../../td[1]/input'

    # edit objects
    name_box = ('ID', 'payGrade_name')
    currency_box = ('ID', 'payGradeCurrency_currencyName')
    min_salary = ('ID', 'payGradeCurrency_minSalary')
    max_salary = ('ID', 'payGradeCurrency_maxSalary')
    currency_add_btn = ('ID', 'btnAddCurrency')
    currency_save_btn = ('ID', 'btnSaveCurrency')
    add_min_sal = '//a[text()="{}"]/../../td[3]'
    add_max_sal = '//a[text()="{}"]/../../td[4]'

    def __init__(self, browser):
        super(PayGrades, self).__init__(browser)
        self.click_menu("Job")
        self.click_menu("Pay Grades")
        Log.info("Arrive Admin Pay Grades page")

    def cancel_adding_pay_grades(self, add_name):
        """
        Cancel adding a pay grade

        """
        self.click(self.add_btn)
        self.clear_text(self.name)
        self.input_text(add_name, self.name)
        self.click(self.cancel_btn)
        assert not add_name in self.get_elements_texts(("XPATH", "//td[2]"))
        Log.info("Add operation is being canceled")

    def add_pay_grades(self, add_name):
        """
        Add a pay grade

        """
        Log.info("Start to add a pay grade")
        self.click(self.add_btn)
        self.clear_text(self.name)
        self.input_text(add_name, self.name)
        self.click(self.save_btn)

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
        self.click(self.save_btn)
        self.clear_text(self.name_box)
        self.input_text(modify_name, self.name_box)
        self.click(self.save_btn)

    def edit_pay_grades_add_currency(self, modify_name, currency_name, min_sal, max_sal):
        """
        Add a currency for the Pay Grade

        """
        Log.info("Start to add a currency to Pay Grade")
        edit_element = ('LINK_TEXT', modify_name)
        self.click(edit_element)
        self.click(self.currency_add_btn)
        self.clear_text(self.currency_box)
        self.input_text(currency_name, self.currency_box)
        self.input_text(min_sal, self.min_salary)
        self.input_text(max_sal, self.max_salary)
        self.click(self.currency_save_btn)

    def check_currency_addto_edit(self, currency_name, min_sal, max_sal):
        """
        Check the currency is added in the Assign Currency list

        """
        Log.info("Checking if currency is added successfully in Assigned Currency")
        currency = str(currency_name)[6:]
        col_name = ('LINK_TEXT', currency)
        min_salary = ("XPATH", self.add_min_sal.format(currency))
        max_salary = ("XPATH", self.add_max_sal.format(currency))
        added_min_salary = self.get_element_text(min_salary).encode("utf-8").replace(",", "")
        added_max_salary = self.get_element_text(max_salary).encode("utf-8").replace(",", "")
        assert self.get_element(col_name).is_displayed
        assert Decimal(added_min_salary) == Decimal(min_sal)
        assert Decimal(added_max_salary) == Decimal(max_sal)
        Log.info("Currency is added successfully in Assigned Currency")

    def check_currency_addto_paygrades(self, modify_name, currency_name):
        """
        Check the currency is added in the pay grade main page

        """
        add_currency = str(currency_name)[6:]
        assign_currency = self.add_currency.format(modify_name)
        self.sleep(2)
        ele = ('XPATH', assign_currency)
        assert add_currency == self.get_element_text(ele).encode("utf-8")
        Log.info("Currency is added successfully in Pay Grades")

    def cancel_delete_pay_grades(self, modify_name):
        """
        Cancel deleting a pay grade

        """
        checkbox = self.element.format(modify_name)
        self.click(('XPATH', checkbox))
        Log.info("Start to delete a pay grade")
        self.click(self.delete_btn)
        self.wait_unit_el_present(self.del_cancel_btn)
        self.click(self.del_cancel_btn)
        assert modify_name in self.get_elements_texts(("XPATH", "//td[2]"))
        Log.info("Delete operation is being canceled")
        self.click(('XPATH', checkbox))

    def delete_pay_grades(self, modify_name):
        """
        delete a pay grade

        """
        checkbox = self.element.format(modify_name)
        self.click(('XPATH', checkbox))
        Log.info("Start to delete a pay grade")
        self.click(self.delete_btn)
        self.wait_unit_el_present(self.del_ok_btn)
        self.click(self.del_ok_btn)

    def assert_message(self, return_message):
        """
        Assert the result of current operation

        """
        assert return_message in self.get_element_text(self.message)
        Log.info(return_message)

