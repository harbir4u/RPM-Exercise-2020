"""
This file contains functions corresponding to test cases performed on the Integration Test Home Page.
"""
from _ast import Assert
from TestData import TestData
from IntegrationTestHomePage import IntegrationTestHomePage
from BaseTest import BaseTest
from PageLocators import PageLocators


# Base class for all tests
class FillFormTest(BaseTest):
    def setUp(self):
        # Calling the setUp() method of the parent class: BaseTest
        super().setUp()

    def test_fill_form(self):
        self.IntegrationTestHomePage = IntegrationTestHomePage(self.driver)
        text = self.IntegrationTestHomePage.fill_employee_name(PageLocators.EmployeeName, text="Hello")
        # text = self.IntegrationTestHomePage.fill_employee_name().getText()
        Assert.assertTrue(text.equals(TestData.EMPLOYEE_NAME))
