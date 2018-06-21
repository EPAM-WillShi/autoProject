import unittest
from config import config
from com import utils
from pageobjects.performance.configure.trackers import Trackers
from pageobjects.pim.employee_list import EmployeeList
from pageobjects.login import Login
# from pageobjects.pim.add_employee import AddEmployee


class TestAddTracker(unittest.TestCase):
    browser = config.BROWSER
    trackername = 'test'
    empname = 'Robert Craig'
    first_name = 'Robert'
    last_name = 'Craig'
    avareview = 'Hannah Flores'
    tableid = 'resultTable'
    # win_name = 'OrangeHRM - Confirmation Required'
    # first_name = 'anne'
    # last_name = 'tang'

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.get_browser_driver(cls.browser)
        cls.login = Login(cls.driver)
        cls.login.open_browser(config.LOGIN_URL)
        cls.login.login(config.USER_NAME, config.PASSWORD)
        cls.employee_list = EmployeeList(cls.driver)
        cls.employee_list.add_employee(cls.first_name, cls.last_name)
        cls.tracker = Trackers(cls.driver)
        # cls.addemp = AddEmployee(cls.driver)
        # cls.bps=BasePage(cls.driver)
        # cls.tracker.max_browser()

    def test_case1_add_pertracker(self):
        self.tracker.add_pertracker(self.trackername, self.empname, self.avareview)
        self.tracker.validate_added_tracker(self.tracker.new_add)

    def test_case2_delete_added_tracker(self):
        self.tracker.select_checkbox(self.tracker.record_checkbox)
        self.tracker.delete_added_tracker(self.tracker.delete_btn, self.tracker.del_cancel, self.tracker.del_OK)
        self.tracker.check_delete_record(self.tracker.new_add)

    @classmethod
    def tearDownClass(cls):
        cls.tracker.quit_browser()


if __name__ == "__main__":
    unittest.main()
