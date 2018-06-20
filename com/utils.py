# coding:utf-8
import re
import platform
from datetime import datetime, timedelta
from string import digits as dig
from string import ascii_lowercase as lc
from string import ascii_uppercase as up
from string import punctuation as pun
from random import randrange, choice, randint
from selenium import webdriver
from lib.log import Log


def get_browser_driver(browser):
    platform_type = platform.system()
    if platform_type == 'Linux':
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        driver = webdriver.Chrome(chrome_options=option)
        return driver
    elif platform_type == 'Windows':
        if re.match(r'(i|I)(e|E)', browser):
            driver = webdriver.Ie()
        elif re.match(r'(c|C)(h|H)(r|R)(o|O)(m|M)(e|E)', browser):
            driver = webdriver.Chrome()
        elif re.match(r'(f|F)(i|I)(r|R)(e|E)(f|F)(o|O)(x|X)', browser):
            driver = webdriver.Firefox()
        else:
            print "Currently not support this browser {}".format(browser)
        return driver
    else:
        print "Currently not support this platform {}".format(platform_type)


def input_random_number(*args):
    try:
        if len(args) == 0:
            number_length = randrange(4, 8)
        else:
            number_length = args[0]
        number = ''.join(choice(dig)for _ in range(number_length))
    except Exception, e:
        Log.error("% s, please transfer one digit param." % e)
    Log.info("Input the number: % s" % number)
    return number


def input_random_text(*args):
    try:
        if len(args) == 0:
            text_length = randrange(4, 8)
        else:
            text_length = args[0]
        text = ''.join(choice(lc) for _ in range(text_length))
    except Exception, e:
        Log.error("% s, please transfer one digit param." % e)
        text = text.capitalize()
    Log.info("Input the password: % s" % text)
    return text


def input_random_password(*args):
    try:
        if len(args) == 0:
            password_length = randrange(4, 8)
        else:
            password_length = args[0]
        password = ''.join(choice(lc + up + dig + pun)for _ in range(password_length))
    except Exception, e:
        Log.error("% s, please transfer one digit param." % e)
    Log.info("Input the password: % s" % password)
    return password


def input_random_date(*args):
    now = datetime.now()
    try:
        if len(args) == 0:
            day = randint(1, 30)
            before_now = now - timedelta(day)
            after_now = now + timedelta(day)
            date = choice([before_now, after_now])
        else:
            args = datetime.strptime(args[0], '%Y-%m-%d').date()
            duration = randint(1, 10)
            date = args + timedelta(duration)
        date_format = date.strftime("%Y-%m-%d")
    except Exception, e:
        Log.error("% s, please transfer one date, its format is 'YYYY/MM/DD'." % e)
    Log.info("Generate the date: %s " % date_format)
    return date_format


# # ===============================================================================
# def set_combox_value(driver,  element,  value):
#     element = Select(driver.find_element(*element))
#     try:
#         element.select_by_visible_text(value)
#     except NoSuchElementException:
#         print "Could not locate the element value {}".format(value)
#
#
# def check_is_alert_present(driver):
#     wait = WebDriverWait(driver, 10)
#     try:
#         wait.until(ec.alert_is_present())
#         found_alert = True
#     except Exception:
#         print "No alert dialog is pop up"
#     return found_alert
#
#
# def dismiss_alert(driver):
#         driver.switch_to.alert().dismiss()
#         # driver.switchTo().alert().dismiss()
#
#
# def accept_alert(driver):
#     alert = driver.switch_to_alert()
#     alert.accept()
#
#
def random_suffix():
    # now = "%d" % (time.time() * 1000)
    # rd = random.randint(1000, 9999)
    rd = randint(1, 100)
    # suffix = '_' + str(now) + '_' + str(rd)
    suffix = '_00' + str(rd)
    return suffix

#
# def select_frame(driver, frame):
#     driver.switch_to.parent_frame()
#     driver.switch_to.frame(frame)
#
#
# def check_element(driver, xpath):
#     for retry in range(12):
#         try:
#             driver.find_element_by_xpath(xpath)
#             return True
#         except NoSuchElementException:
#             if retry == 0:
#                 print("\tWait for element loading:")
#             time.sleep(5)
#             wait_time = (retry + 1) * 5
#             print("\t%d seconds" % wait_time)
# ===============================================================================
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
# ===============================================================================
