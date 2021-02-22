"""
This file contains functions corresponding to test cases performed on the Integration Test Home Page.
"""
import time

from selenium.webdriver.support.wait import WebDriverWait

from utilities.test_data import TestData
from pages.integration_test_home_page import IntegrationTestHomePage
from tests.base_test import BaseTest


# Base class for all tests
class FillFormTest(BaseTest):
    """
    def setUp(self):
        # Calling the setUp() method of the parent class: BaseTest
        super().setUp()
    """
    def test_fill_form(self):
        print("Test Started")
        print(TestData.EMPLOYEE_NAME)
        page = IntegrationTestHomePage(self.driver)
        page.fill_employee_name(TestData.EMPLOYEE_NAME)
        print("Entered Employee name")
        page.fill_summary(TestData.SUMMARY)
        print("Entered summary")
        page.
        time.sleep(15)