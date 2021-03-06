"""
This file contains the Base class for all tests, as it opens a new browser session browser. It is called in the
test classes to open a new browser session, perform actions and quit browser session
"""
import unittest
from selenium import webdriver
from utilities.test_data import TestData


class BaseTest(unittest.TestCase):

    # This function is called every time a new object of the BaseTest class is created.
    def setUp(self):
        # Calls geckodriver to open a new Firefox browser session
        self.driver = webdriver.Firefox(executable_path=TestData.GECKODRIVER_PATH)

        # Load browser in maximized window
        # self.driver.maximize_window()
        self.driver.get("https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html")

    def tearDown(self):
        self.driver.quit()
