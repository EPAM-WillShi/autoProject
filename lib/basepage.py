# -*- coding: utf-8 -*-
"""
Created on 2018/4/2
@author: Angelia_Yao
"""

import os
import time
import random
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from lib.log import Log
from config.config import UPLOAD_PATH


class BasePage(object):
    """
    Base page class, common elements and actions
    """
    def __init__(self, driver):
        try:
            self.driver = driver
            #  self.driver.implicitly_wait(10) # 设置隐式等待时间为10s
        except Exception, e:
            print e
            raise NameError('The driver {} error'.format(driver))
        
    def refresh_page(self):
        """
        Refresh page
        """
        self.driver.refresh()
        
    def open_browser(self, url):
        """
        Open browser
        """
        self.driver.get(url)

    def back_browser(self):
        """
        Back browser
        """
        self.driver.back()

    def forward_browser(self):
        """
        Forward browser
        """
        self.driver.forward()
            
    def max_browser(self):
        """
        Maximum browser
        """
        self.driver.maximize_window()   
         
    def close_browser(self):
        """
        Close browser tab
        """
        self.driver.close()

    def quit_browser(self):
        """
        Close browser all tab
        """
        self.driver.quit()

    def sleep(self, seconds):
        """
        Sleep some time
        """
        time.sleep(seconds)
    
    def wait(self, seconds):
        """
        Implicitly wait
        """ 
        self.driver.implicitly_wait(seconds) 
          
    def wait_unit_el_present(self, keys, sec=15):
        """
        Display wait,wait until element display, time out 15 sec
        """
        wait = WebDriverWait(self.driver, sec)
        key = keys[0]
        value = keys[1]
        if key in ['XPATH', 'xpath']:
            locator = (By.XPATH, value)
        elif key in ['link_text', 'LINK_TEXT']:
            locator = (By.LINK_TEXT, value)
        elif key in ['ID', 'id']:
            locator = (By.ID, value)
        elif key in ['NAME', 'name']:
            locator = (By.NAME, value)
        elif key in ['CLASS_NAME', 'class_name']:
            locator = (By.CLASS_NAME, value)
        elif key in ['TAG', 'tag']:
            locator = (By.TAG_NAME, value)
        try:
            element = wait.until(ec.presence_of_element_located(locator))
            return element
        except BaseException, e:
            Log.error(e)
            self.get_windows_img()
            return None

    def get_windows_img(self):
        """
        save the screenshot
        """
        file_path = "screenshots//"
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            Log.info("Save screen shot to screenshots")
        except NameError as e:
            Log.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()
        
    def get_current_window(self):
        """
        Get current window page
        """
        return self.driver.current_window_handle

    def switch_to_frame(self, frame_name):
        """
        Switch to frame
        """ 
        self.driver.switch_to_frame(frame_name)
        
    def switch_to_window(self, window_name):
        """
        Switch to window
        """
        self.driver.switch_to_window(window_name)
        
    def switch_to_default(self):
        """
        Switch to default page
        """
        self.driver.switch_to_default_content()
             
    def switch_to_alert(self):
        """
        Switch to alert window
        """
        self.driver.switch_to_alert()

    def accept_alert(self):
        """
        Accept the alert
        """
        alert = self.driver.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        """
        Dismiss alert
        """
        self.driver.switch_to.alert().dismiss()
    
    def get_elements_texts(self, keys):
        """
        Get one group elements texts
        """
        text_list = []
        try:
            elements = self.get_elements(keys)
            for element in elements:
                text = element.text
                text_list.append(text.encode("utf-8"))
        except BaseException, e:
            Log.error(" Unable to find the element, please "
                      "check your keys %s" % keys)
            Log.error(e)
        return text_list
                    
    def is_element_visible(self, xpath):
        """
        Check if element visible
        """
        flag = False
        try:
            element = self.wait_unit_el_present(xpath)
            if element is not None:
                flag = True
            #         for retry in range(5):
            #             try:
            #                 self.driver.find_element_by_xpath(xpath)
            #                 flag = True
            #             except NoSuchElementException:
            #                 if retry == 0:
            #                     print("\tWait for element loading:")
            #                 time.sleep(5)
            return flag
        except BaseException, e:
            Log.error(e)

    def get_element(self, keys):
        """
        Get one element, keys is a tuple
        """
        try:
            get_method = keys[0]
            element = keys[1]
        except Exception:
            raise ValueError(
                "please transfer the correct list params,like () or []")

        if get_method in ['ID', 'id']:
            element = (By.ID, element)
        elif get_method in ['NAME', 'name']:
            element = (By.NAME, element)
        elif get_method in ['XPATH', 'xpath']:
            element = (By.XPATH, element)
        elif get_method in ['LINK_TEXT', 'link_text']:
            element = (By.LINK_TEXT, element)
        elif get_method in ['CLASS_NAME', 'class_name']:
            element = (By.CLASS_NAME, element)
        elif get_method in ['XPATH', 'xpath']:
            element = (By.XPATH, element)
        elif get_method in ['TAG', 'tag']:
            element = (By.TAG_NAME, element)
        try:
            return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(element))
        except NoSuchElementException:
            return None
        except TimeoutException:
            return None
        
    def get_element_text(self, keys):
        """
        Get element text
        """
        try:
            element = self.get_element(keys)
            if element is None:
                Log.error("Could not locate the element value {}".format(keys))
            else:
                return element.text
        except BaseException, e:
            Log.error(e)

    def get_element_attribute(self, keys, attkey):
        """
        Get element attribute value
        """
        try:
            element = self.get_element(keys)
            if element is None:
                return None
            else:
                value = element.get_attribute(attkey)
                return value
        except BaseException, e:
            Log.error(e)

    def get_elements(self, keys):
        """
        Get one group elements
        """
        try:
            get_method = keys[0]
            elements = keys[1]
        except Exception:
            raise ValueError(
                "please transfer the correct list params,like () or []")
        if get_method in ['XPATH', 'xpath']:
            elements = self.driver.find_elements_by_xpath(elements)
        elif get_method in ['NAME', 'name']:
            elements = self.driver.find_elements_by_name(elements)
        elif get_method in ['LINK_TEXT', 'link_text']:
            elements = self.driver.find_elements_by_link_text(elements)
        elif get_method in ['CLASS_NAME', 'class_name']:
            elements = self.driver.find_elements_by_class_name(elements)
        elif get_method in ['TAG', 'tag']:
            elements = self.driver.find_elements_by_tag_name(elements)
        return elements

    def input_text(self, value, keys):
        """
        Input text
        """
        try:
            element = self.get_element(keys)
            if element is None:
                return None
            else:
                element.clear()  # added by Linda
                element.send_keys(value)
        except BaseException, e:
            Log.error(e)

    def clear_text(self, keys):
        """
        Clear the text box
        """
        try:
            element = self.get_element(keys)
            if element is None:
                return None
            else:
                self.get_element(keys).clear()
        except BaseException, e:
            Log.error(e)

    def press_enter_key(self, keys):
        """
        Todo  need test later
        """
        try:
            self.get_element(keys).send_keys(Keys.ENTER)
        except BaseException, e:
            Log.error(e)

    def click(self, keys):
        """
        Click button
        """
        try:
            element = self.get_element(keys)
            if element is None:
                raise Exception
            else:
                self.get_element(keys).click()
        except BaseException, e:
            Log.error(e)

    def get_page_title(self):
        """
        Get page title
        """
        try:
            Log.info("Current page title is %s" % self.driver.title)
            return self.driver.title
        except BaseException, e:
            Log.error(e)

    def script(self, src):
        """
        Run script
        """
        self.driver.execute_script(src)
        
    def set_combox_value(self, value, keys):
        """
        Choose combox value
        """
        try:
            element = self.get_element(keys)
            if element is None:
                Log.error("Could not locate the element value {}".format(keys))
            else:
                Select(element).select_by_visible_text(value)
        except NoSuchElementException:
            Log.error("Could not locate the element value {}".format(value))

    def get_first_select(self, keys):
        """
        get select option first value
        """
        try:
            value1 = Select(self.get_element(keys)).first_selected_option.text
            return value1
        except BaseException, e:
            Log.error(e)

    def select_option(self, keys, option):
        """
        select option
        """
        try:
            value = Select(self.get_element(keys)).select_by_index(option)
            return value
        except BaseException, e:
            Log.error(e)

    def get_page_url(self):
        """
        Get page title
        """
        try:
            Log.info("Current page title is %s" % self.driver.current_url)
            return self.driver.current_url
        except BaseException, e:
            Log.error(e)

    #  Added by Anne
    def check_element_selected(self, keys):
        """
        Check radio or checkbox is selected or not
        """
        try:
            self.get_element(keys).is_selected()
            print("Enabled")
        except Exception as e:
            print ('disabled', format(e))

    # Added by Linda
    def get_all_window(self):
        """
        Get current window page
        """
        try:
            return self.driver.window_handles
        except BaseException, e:
            Log.error(e)

    def upload_file(self, value, keys):
        """
        Upload a file - added by Linda
        """
        try:
            element = self.get_element(keys)
            if element is None:
                return None
            else:
                path = os.path.abspath(UPLOAD_PATH)
                if "testcase" in path:
                    path = path.split("testcase")[0]
                    path = os.path.join(path, UPLOAD_PATH)
                path = os.path.join(path, value)
                Log.info("The path is %s." % path)
                element.send_keys(path)
        except BaseException, e:
            Log.error(e)

    def mouse_move_to_element(self, keys):
        """
        Mouse move to the element - Added by Linda
        """
        try:
            mouse = self.get_element(keys)
            if mouse is not None:
                ActionChains(self.driver).move_to_element(mouse).perform()
        except BaseException, e:
            Log.error(e)

    def get_random_data(self, keys):
        """
        Get random data - Added by Linda
        """
        try:
            elements = self.get_elements(keys)
            element = choice(elements)
            element_text = element.text
            return element_text
        except Exception, e:
            Log.error(e)

    def select_random_list(self, keys):
        """
        select a random value from dropdown list
        """
        value = self.get_element_text(keys).encode('utf-8')
        value_list = value.rsplit('\n')
        length = len(value_list)
        if value[0] == '--Select--':
            num = random.randint(1, length - 1)
        elif value[0] == '-- Month --':
            num = random.randint(1, length - 1)
        else:
            num = random.randint(0, length - 1)
        self.select_option(keys, num)

    def element_is_displayed(self, keys):
        try:
            element = self.get_element(keys)
            if element is not None:
                element.is_displayed()
        except BaseException, e:
            Log.error(e)

