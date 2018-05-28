# -*- coding: utf-8 -*-
from pageobjects.time.time import Time
from lib.log import Log


class Customers(Time):
    """
    Time Customers page main components
    """
    add_bth = ('ID', 'btnAdd')
    name_input = ('ID', 'addCustomer_customerName')
    description_input = ('ID', 'addCustomer_description')
    save_bth = ('ID', 'btnSave')

    # Delete projects
    get_total_row_ele = ("XPATH", "//tr")
    name_ele_value = "//tr[{}]/td[2]"
    check_name_ele_value = "//tr[{}]/td[1]"
    delete_btn_ele = ('ID', 'btnDelete')
    ok_btn_ele = ('ID', 'dialogDeleteBtn')
    success_flag = ("xpath", "//div[@class='message success fadable']")

    def __init__(self, browser):
        super(Customers, self).__init__(browser)
        self.click_menu("Project Info")
        self.click_menu("Customers")

    def add_customer(self, name, description):
        '''
        Create a customer
        '''
        self.click(self.add_bth)
        self.input_text(name, self.name_input)
        self.input_text(description, self.description_input)
        self.click(self.save_bth)
        Log.info("Create customer successfully!")

    def check_customer(self, customer_name):
        """
        Select customer
        """
        rows = self.get_elements(self.get_total_row_ele)  # Obtain all rows
        for row in range(1, len(rows)):
            get_name_ele_value = self.name_ele_value.format(row)
            name = self.get_element_text(("XPATH", get_name_ele_value))  # Obtain customer name of this row.
            if name.startswith(customer_name):  # If obtained customer name includes customer_name, check it.
                check_customer_ele_value = self.check_name_ele_value.format(row)
                self.click(("XPATH", check_customer_ele_value))
            else:  # If obtained customer name doesn't include customer_name, check the next name.
                row += 1

    def delete_customer(self, customer_name):
        """
        Delete a customer
        """
        try:
            self.check_customer(customer_name)
            self.click(self.delete_btn_ele)
            self.click(self.ok_btn_ele)
        except Exception:
            Log.exception("No customer is found!")


