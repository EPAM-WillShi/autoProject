"""
Created on 2018/04/27

@author: Julia_Zhu
"""
from lib.log import Log
from pageobjects.mainpage import MainPage


class PIM(MainPage):
    """
    PIM page main components
    """
    menuBar = ".//*[@id='{}']"
    configurationMenu = "Configuration"

    #add_btn = ("xpath", "//input[@id='buttonAdd']")
    save_btn = ("xpath", "//input[@id='btnSave']")
    assert_path = "//div[@class='message success fadable']"
    show_nickname = ("xpath", "//input[@id='configPim_chkDeprecateFields']")
    show_ssn = ("xpath", "//input[@id='configPim_chkShowSSN']")
    show_sin = ("xpath", "//input[@id='configPim_chkShowSIN']")
    show_us = ("xpath", "//input[@id='configPim_chkShowTax']")

    def __init__(self, browser):
        super(PIM, self).__init__(browser)
        self.switch_main_menu("PIM")
        Log.info("Arrive PIM page")

    def click_menu(self, menuname):
        """
        Click PIM page menu
        """
        Log.info("Click the %s menuname")
        menu_name = menuname.title()
        try:
            element = self.get_element(("link_text", menu_name))
            element.click()
        except:
            if menu_name == "Optional Fields":
                newmenu = "menu_pim_{}".format("configurePim")
            else:
                newmenu = "menu_pim_{}".format(menuname)
            menu = self.menuBar.format(newmenu)
            try:
                element = self.get_element(("xpath", menu))
                element.click()
            except BaseException, e:
                print e
                Log.error(e)
                raise "Element %s not found" % menuname

    def click_edit_save_button(self):
        """
        click edit or save button
        """
        element = self.get_element(self.save_btn)
        element.click()

    def assert_optional_message(self):
        """
        verify it will appear Successfully Saved message
        """
        element = self.driver.find_element_by_xpath(self.assert_path)
        print element.text

    def edit_pim_config(self, show1, show2, show3, show4):
        """
        click edit button, select select each checkbox and check the checkbox is selected
        """
        self.click_edit_save_button()
        element_nickename = self.get_element(self.show_nickname)
        element_ssn = self.get_element(self.show_ssn)
        element_sin= self.get_element(self.show_sin)
        element_us = self.get_element(self.show_us)
        if element_nickename.is_selected() != show1:
            element_nickename.click()
        if element_ssn.is_selected() != show2:
            element_ssn.click()
        if element_sin.is_selected() != show3:
            element_sin.click()
        if element_us.is_selected() != show4:
            element_us.click()

        self.click_edit_save_button()

        self.assert_optional_message()

    def assert_selected_values(self, show1, show2, show3, show4):
        """
        Verify the selected checkbox value is correct
        """
        assert show1 == self.get_element(self.show_nickname).is_selected()
        assert show2 == self.get_element(self.show_ssn).is_selected()
        assert show3 == self.get_element(self.show_sin).is_selected()
        assert show4 == self.get_element(self.show_us).is_selected()

        print self.get_element(self.show_nickname).is_selected()
        print self.get_element(self.show_ssn).is_selected()
        print self.get_element(self.show_sin).is_selected()
        print self.get_element(self.show_us).is_selected()

