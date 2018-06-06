# coding:utf-8

import sys
import re
import random
import time
# rom config.config import BROWSER
from selenium import webdriver
#from symbol import except_clause
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
# from unittest.TestCase import ExpectedException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def get_browser_driver(browser):
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference('permissions.default.stylesheet', 2)  # Disable CSS
    firefox_profile.set_preference('permissions.default.image', 2)  # Disable image
    if re.match(r'(i|I)(e|E)', browser):
        driver = webdriver.Ie()
    elif re.match(r'(c|C)(h|H)(r|R)(o|O)(m|M)(e|E)', browser):
        driver = webdriver.Chrome()
    elif re.match(r'(f|F)(i|I)(r|R)(e|E)(f|F)(o|O)(x|X)', browser):
        driver = webdriver.Firefox(firefox_profile)
    else:
        print "Currently not support this browser {}".format(browser)
    return driver


def set_combox_value(driver,  element,  value):
    element = Select(driver.find_element(*element))
    try:
        element.select_by_visible_text(value)
    except NoSuchElementException:
        print "Could not locate the element value {}".format(value)



def check_is_alert_present(driver):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(ec.alert_is_present())
        found_alert = True
    except Exception:
        print "No alert dialog is pop up"
    return found_alert


def dismiss_alert(driver):
        driver.switch_to.alert().dismiss()
        # driver.switchTo().alert().dismiss()


def accept_alert(driver):
    alert = driver.switch_to_alert()
    alert.accept()


def random_suffix():
    #now = "%d" % (time.time() * 1000)
    #rd = random.randint(1000, 9999)
    rd = random.randint(1,100)
    #suffix = '_' + str(now) + '_' + str(rd)
    suffix = '_00' + str(rd)
    return suffix


def select_frame(driver, frame):
    driver.switch_to.parent_frame()
    driver.switch_to.frame(frame)

def check_element(driver, xpath):
    for retry in range(12):
        try:
            driver.find_element_by_xpath(xpath)
            return True
        except NoSuchElementException:
            if retry == 0:
                print("\tWait for element loading:")
            time.sleep(5)
            wait_time = (retry + 1) * 5
            print("\t%d seconds" % wait_time)
#===============================================================================
#  
# def init_case(csid, cstitle, cssummary):
#     print("\nAtmos - %s : %s" % (csid, cstitle))
#     print(cssummary, "\n")
#    

#   
#   
# def input_text(xpath, text):
#     driver.find_element_by_xpath(xpath).clear()
#     driver.find_element_by_xpath(xpath).send_keys(text)
#   
#   
# def click_button(button, xpath):
#     if button is None:
#         __button = None
#     else:
#         print("Click '%s' " % button)
#         __button = driver.find_element_by_xpath(xpath).text
#     if __button == button:
#         driver.find_element_by_xpath(xpath).click()
#     else:
#         print("Button text is not EXPECTED.")
#         print("\tEXPECTED: %s" % button)
#         print("\tACTUAL  : %s " % __button)
#         exit(1)
#   
#   
# def select_drop_down_list(xpath, value):
#     Select(driver.find_element_by_xpath(xpath)).select_by_value(value)
#   
#   
# 
#   
#   
# def enable_checkbox(xpath, rmg_node):
#     if driver.find_element_by_xpath(xpath).is_selected():
#         print("=========HAVE=SELECTED==========")
#     else:
#         print("====What is selected", driver.find_element_by_xpath(xpath).is_selected())
#         print("====Name is :", driver.find_element_by_xpath(xpath).get_attribute("name"))
#         driver.find_element_by_xpath(xpath).click()
#   
#   
# def browser_security_page():
#     if BROWSER == "ie":
#         if ec.element_to_be_clickable(".//*[@id='overridelink']"):
#             print("Click 'Continue to this website (not recommended).'")
#             click_button(None, ".//*[@id='overridelink']")
#   
#   
# def tenant_login(ip, tnt, tntadmin, passwd):
#     url = 'https://' + ip
#     driver.get(url)
#     browser_security_page()
#     input_text(".//*[@id='tenant_name']", tnt)
#     input_text(".//*[@name='username']", tntadmin)
#     input_text(".//*[@id='login_form']/table/tbody/tr[8]/td[3]/input", passwd)
#     click_button('Login', ".//*[@id='login_form']/table/tbody/tr[12]/td[2]/table/tbody/tr/td[4]/span")
#  
# #===============================================================================
# def sysadmin_login(ip, sysadmin, passwd):
#     url = "http://%s/mgmt_login" % ip
#     print("Load url: %s" % url)
#     driver.get(url)
#     browser_security_page()
#     print("Input sysadmin: %s" % sysadmin)
#     input_text(".//*[@id='username']", sysadmin)
#     print("Input sysadmin's password: %s" % passwd)
#     input_text(".//*[@id='login_form']/table/tbody/tr[8]/td[3]/input", passwd)
#     click_button('Login', ".//*[@id='login_form']/table/tbody/tr[13]/td[2]/table/tbody/tr/td[4]/span")
#===============================================================================