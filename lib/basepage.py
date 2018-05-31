# -*- coding: utf-8 -*-
'''
Created on 2018/4/2
@author: Angelia_Yao
'''

import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from lib.log import Log
from config.config import UPLOAD_PATH


class BasePage(object):
    """
    Base page class, common elements and actions
    """
    def __init__(self, driver):
        try:
            self.driver = driver
            #self.driver.implicitly_wait(10) # 设置隐式等待时间为10s
        except Exception,e:
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
        Maxmium browser
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
          
    def wait_unit_el_present(self, keys):
        """
        Display wait,wait until element display, time out 15 sec
        """
        wait = WebDriverWait(self.driver, 15)
        key = keys[0]
        value = keys[1]
        if key in ['XPATH', 'xpath']:
            locator = (By.XPATH, value)
        elif key in ['link_text', 'LINK_TEXT']:
            locator = (By.LINK_TEXT, value)
        elif key in ['ID','id']:
            locator = (By.ID, value)
        elif key  in ['NAME', 'name']:
            locator = (By.NAME, value)
        elif key in ['CLASS_NAME', 'class_name']:
            element = (By.CLASS_NAME, value)
        elif key in ['TAG', 'tag']:
            element = (By.TAG_NAME, value)                      
        try:
            element = wait.until(ec.presence_of_element_located(locator))
        except Exception:
            Log.exception("Failed to wait element!")
            self.get_windows_img()
        self.sleep(2)
        return element
    
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
        # type: (object) -> object
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
            Log.error(" Unable to find the element, please \
              check your keys %s" % keys)
            Log.error(e)
        return text_list
                    
    def is_element_visible(self, xpath):
        """
        Check if element visible
        """
        flag = False
 
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
            return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(element))
        except NoSuchElementException:
            return None
        except TimeoutException:
            return None
        
    def get_element_text(self, keys):
        # type: (object) -> object
        """
        Get element text
        """
        element = self.get_element(keys)
        if element is None:
            return None
        else:
            return element.text

    def get_element_attribute(self, keys, attkey):
        # type: (object, object) -> object
        """
        Get element attribute value
        """
        element = self.get_element(keys)        
        if element is None:
            return None
        else:
            value = element.get_attribute(attkey)
            return value
        
    def get_elements(self, keys):
        # type: (object) -> object
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
        element = self.get_element(keys)
        if element is None:
            return None
        else:
            element.clear()  # added by Linda
            element.send_keys(value)
            
    def clear_text(self, keys):
        """
        Clear the text box
        """
        element = self.get_element(keys)
        if element is None:
            return None
        else:
            self.get_element(keys).clear()
            
    def press_enter_key(self, keys):
        """
        Todo  need test later
        """
        self.get_element(keys).send_keys(Keys.ENTER)

    def click(self, keys):
        """
        Click button
        """
        element = self.get_element(keys)
        if element is None:
            raise Exception
        else:        
            self.get_element(keys).click()  

    def get_page_title(self):
        """
        Get page title
        """
        Log.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    def script(self, src):
        """
        Run script
        """
        self.driver.execute_script(src)
        
    def set_combox_value(self, value, keys):
        # type: (object, object) -> object
        """
        Choose combox value
        """
        try:
            Select(self.get_element(keys)).select_by_visible_text(value)
        except NoSuchElementException:
            print "Could not locate the element value {}".format(value)
            sys.exit(-1)

    def get_first_select(self, keys):
        """
        get select option first value
        """

        value1 = Select(self.get_element(keys)).first_selected_option.text
        return value1

    def select_option(self, keys, option):
        """
        select option
        """
        value = Select(self.get_element(keys)).select_by_index(option)
        return value

    def get_page_url(self):
        """
        Get page title
        """
        Log.info("Current page title is %s" % self.driver.current_url)
        return self.driver.current_url

    # Added by Linda
    def get_all_window(self):
        """
        Get current window page
        """
        return self.driver.window_handles

    def upload_file(self, value, keys):
        """
        Upload a file - added by Linda
        """
        element = self.get_element(keys)
        if element is None:
            return None
        else:
            path = os.getcwd().split("testcase")[0]
            element.send_keys(path + UPLOAD_PATH + value)

