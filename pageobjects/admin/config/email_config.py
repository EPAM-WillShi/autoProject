# -*- coding: utf-8 -*-
'''
Created on 2018��4��26��

@author: Angelia_Yao
'''
from pageobjects.admin.admin import Admin
from lib.log import Log

class EmailConfig(Admin):
    """
    Email config page components
    """
    page_title = ('xpath', ".//h1[text()='Mail Configuration']")
    edit_btn = ('id', 'editBtn')
    edit_xpath =('xpath',  './/input[@id="editBtn"]')
    reset_btn = ('id', 'resetBtn')
    sent_as = ('id', 'emailConfigurationForm_txtMailAddress')
    send_method = ('id', 'emailConfigurationForm_cmbMailSendingMethod')
    path = ('id', 'emailConfigurationForm_txtSendmailPath')
    send_chk = ('id', 'emailConfigurationForm_chkSendTestEmail')
    test_email = ('id', 'emailConfigurationForm_txtTestEmail')
    smtp_host = ('id', 'emailConfigurationForm_txtSmtpHost')
    smtp_port = ('id', 'emailConfigurationForm_txtSmtpPort')
    use_smtp = ('id', 'emailConfigurationForm_optAuth_login')
    smtp_user = ('id', 'emailConfigurationForm_txtSmtpUser')
    smtp_psd = ('id', 'emailConfigurationForm_txtSmtpPass')
    tls = ('id', 'emailConfigurationForm_optSecurity_tls')
    save_btn = ('xpath', ".//input[@id='editBtn']")

    def __init__(self, browser):
        super(Admin, self).__init__(browser)

    def switch_menu(self):
        """
        Back to Email Configuration page
        """
        self.click_menu("Admin")
        self.click_menu("Configuration")
        self.click_menu("Email Configuration")

    def validate_title(self, ptitle):
        assert ptitle == self.get_element_text(self.page_title)
        Log.info("Arrive mail configuration page")

    def select_sendmothod(self, sentas, sendmothod):
        self.click(self.edit_btn)
        self.input_text(sentas, self.sent_as)
        self.set_combox_value(sendmothod, self.send_method)

    def enter_smtpinfo(self, smtphost, smtpport, smtpuser, smtppsd):
        self.input_text(smtphost, self.smtp_host)
        self.input_text(smtpport, self.smtp_port)
        self.click(self.use_smtp)
        self.input_text(smtpuser, self.smtp_user)
        self.input_text(smtppsd, self.smtp_psd)
        self.click(self.tls)

    def enter_testemail(self, testemail):
        self.click(self.send_chk)
        self.input_text(testemail, self.test_email)
        self.click(self.save_btn)

    def check_info(self, sentas, smtphost, smtpport, smtpuser, attkey):
        print self.get_element_attribute(self.sent_as, attkey)
        print self.get_element_attribute(self.smtp_host, attkey)
        assert sentas == self.get_element_attribute(self.sent_as, attkey)
        assert smtphost == self.get_element_attribute(self.smtp_host, attkey)
        assert smtpport == self.get_element_attribute(self.smtp_port, attkey)
        assert smtpuser == self.get_element_attribute(self.smtp_user, attkey)
        self.sleep(3)
        if self.get_element_attribute(self.test_email, attkey) is None:
            print 'pass'
        else:
            print 'failed'
        self.check_element_selected(self.use_smtp)
        self.check_element_selected(self.tls)
        self.sleep(3)

    def edit_email(self, method, method1, path, attkey):
        self.click(self.edit_xpath)
        self.set_combox_value(method, self.send_method)
        self.input_text(path, self.path)
        self.click(self.save_btn)
        print self.get_element_attribute(self.send_method, attkey)
        print self.get_element_attribute(self.path, attkey)
        assert method1 == self.get_element_attribute(self.send_method, attkey)
        assert path == self.get_element_attribute(self.path, attkey)
        Log.info("edit successfully")


