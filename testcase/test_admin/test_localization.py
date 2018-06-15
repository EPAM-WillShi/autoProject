import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.admin.config.email_config import EmailConfig
from pageobjects.admin.config.localization import Localization
from pageobjects.login import Login


class TestEditlocalization(unittest.TestCase):
    """
    Test Reset Button edit email notification
    """
    menu = config.EMAIL_LOCAL
    browser = config.BROWSER
    ptitle1 = 'Localization'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.editlocal = Localization(cls.driver)
        # cls.emailsub.max_browser()
        EmailConfig(cls.driver).switch_menu(cls.menu)

    def test_edit_notification(self):
        self.editlocal.edit_local(self.ptitle1)

    @classmethod
    def tearDownClass(cls):
        cls.editlocal.quit_browser()

if __name__ == "__main__":
    unittest.main()
