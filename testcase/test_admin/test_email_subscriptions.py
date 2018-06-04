import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.admin.config.email_config import EmailConfig
from pageobjects.admin.config.email_sub import EmailSub
from pageobjects.login import Login


class Testemailsubscriptions(unittest.TestCase):
    """
    Test Reset Button edit email notification
    """
    menu = config.EMAIL_SUB
    browser = config.BROWSER
    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.emailsub = EmailSub(cls.driver)
        # cls.emailsub.max_browser()
        EmailConfig(cls.driver).switch_menu(cls.menu)

    def test_edit_notification(self):
        self.emailsub.enable_notification()
        self.emailsub.disable_notification()

    @classmethod
    def tearDownClass(cls):
        cls.emailsub.quit_browser()

if __name__ == "__main__":
    unittest.main()


