import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.admin.config.email_config import EmailConfig
from pageobjects.login import Login


class Testemailconfig(unittest.TestCase):
    """
    Test save amd edit email configuration
    """
    browser = config.BROWSER
    menu = config.EMAIL_CON
    ptitle = "Mail Configuration"
    sentas = "287326935@qq.com"
    sendmothod = "SMTP"
    sendmothod1 = "Sendmail"
    sendmothod2 = "sendmail"
    path = "D:\Anne"
    smtphost = "smtp.qq.com"
    smtpport = "587"
    smtpuser = "287326935@qq.com"
    smtppsd = "49ba59abbe56e057"
    testemail = "anne_tang@epam.com"
    attkey = "value"

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.emailcof = EmailConfig(cls.driver)
        cls.emailcof.max_browser()
        cls.emailcof.switch_menu(cls.menu)

    def test_save_email_config(self):
        self.emailcof.validate_title(self.ptitle)
        self.emailcof.select_sendmothod(self.sentas,self.sendmothod)
        self.emailcof.enter_smtpinfo(self.smtphost, self.smtpport,self.smtpuser, self.smtppsd)
        self.emailcof.enter_testemail(self.testemail)
        self.emailcof.check_info(self.sentas, self.smtphost, self.smtpport,self.smtpuser, self.attkey)    #
    # def test_edit_email_config(self):
    #     self.emailcof.switch_menu()
        self.emailcof.edit_email(self.sendmothod1, self.sendmothod2, self.path, self.attkey)

    @classmethod
    def tearDownClass(cls):
        cls.emailcof.quit_browser()

if __name__ == "__main__":
    unittest.main()
