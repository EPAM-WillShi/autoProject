import unittest
from config import config
from com import utils
from lib.log import Log
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.login import Login
# from lib.basepage import BasePage
# from pageobjects.mainpage import MainPage


class TestReset(unittest.TestCase):
    """
    Test Reset Button
    """
    browser = config.BROWSER
    first_name = 'Linda'
    epid = '0001'
    sup_name = 'John'
    status = 'Full-Time Permanent'
    job_title = 'HR Manager'
    sub_unit = 'Administration'


    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.pim = EmployeeList(cls.driver)
        # cls.bps=BasePage(cls.driver)
        cls.pim.max_browser()

    def test_case7_search_condition(self):
        """
        Input search condition, search and reset result
        """
        self.pim.wait(3)
        self.pim.input_search_text(self.first_name,self.pim.search_empname)
        self.pim.input_search_text(self.epid, self.pim.search_empid)
        self.pim.input_search_text(self.sup_name, self.pim.search_empsupname)
        self.pim.select_downlist_option(self.status, self.pim.search_empsts)
        self.pim.select_downlist_option(self.job_title, self.pim.search_empjobtl)
        self.pim.select_downlist_option(self.sub_unit,self.pim.search_subunit)

    def test_case8_search_result(self):
        self.pim.click(self.pim.search_btn)
        self.pim.wait_unit_el_present(self.pim.row1_column2)
        self.assertEqual(self.epid,self.pim.get_search_result(self.pim.row1_column2), 'failed')

    def test_case9_reset_button(self):
        self.pim.get_reset_result(self.pim.row2_column2)
        assert u'All' == self.pim.get_first_select(self.pim.search_empsts)
        Log.info("Reset successfully")

    @classmethod
    def tearDownClass(cls):
        cls.pim.quit_browser()


if __name__ == "__main__":
    unittest.main()
