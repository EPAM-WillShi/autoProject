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

    add_btn = ("xpath", "//input[@id='buttonAdd']")
    save_btn = ("xpath", "//input[@id='btnSave']")
    assert_path = "//div[@class='message success fadable']"
    custom_field_panel = ("ID", "customFieldListPane")
    custom_field_name = ("xpath", "//input[@id='customField_name']")
    custom_screen_ele = ("ID", "customField_screen")
    custom_type_ele = ("ID", "customField_type")

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

    def select_screen(self, screen):
        """
        Select a screen value in the drop-down list
        """
        self.set_combox_value(screen, self.custom_screen_ele)

    def select_type(self, type):
        """
        Select a type value in the drop-down list
        """
        self.set_combox_value(type, self.custom_type_ele)

    def click_edit_save_button(self):
        """
        click edit or save button
        """
        element = self.get_element(self.save_btn)
        element.click()

    def assert_custom_message(self):
        """
        verify it will appear Successfully Saved message
        """
        element = self.driver.find_element_by_xpath(self.assert_path)
        print element.text

    def add_custom_field(self, name, screen, type):
        """
        Add a new custom field record and check the record is saved successfully
        """
        if self.get_element_attribute(self.custom_field_panel, "style") != "display: none;":
            self.get_element(self.add_btn).click()
            self.input_text(name, self.custom_field_name)
            self.select_screen(screen)
            self.select_type(type)
            self.click_edit_save_button()
            self.assert_custom_message()
        else:
            self.input_text(name, self.custom_field_name)
            self.select_screen(screen)
            self.select_type(type)
            self.click_edit_save_button()
            self.assert_custom_message()



