"""
This file contains the child class of BasePage class and contains specific functions for use in the Tests
"""
from selenium.webdriver.support.select import Select
from PageLocators import PageLocators
from TestData import TestData
from BasePage import BasePage


# Contains functions that perform actions on the Integration Test HomePage
class IntegrationTestHomePage(BasePage):

    def __init__(self, driver):
        self.locator = PageLocators
        self.testdata = TestData
        super(IntegrationTestHomePage, self).__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def fill_employee_name(self, by_locator, text):
        self.enter_text(*self.locator.EmployeeName, text)

    def fill_summary(self):
        self.driver.enter_text(PageLocators.Summary, TestData.SUMMARY)

    def select_department_from_dropdown(self, value):
        dropdownlist = self.driver.find_elements(PageLocators.Department)
        for element in dropdownlist:
            if element.text == value:
                element.click()
                break

    def select_work_location_from_dropdown(self, value):
        dropdownlist = self.driver.find_elements(PageLocators.WorkLocation)
        for element in dropdownlist:
            if element.text == value:
                element.click()
                break

    def select_length_metric(self, value):
        select = Select(self.driver.find_elements(PageLocators.CubicleLengthMetric))
        select.select_by_visible_text(value)

    def select_width_metric(self, value):
        select = Select(self.driver.find_elements(PageLocators.CubicleWidthMetric))
        select.select_by_visible_text(value)

    def fill_car_details_table(self, row, column, text):
        options = self.driver.find_element(PageLocators.CarDetails % (row, column))
        options.send_keys(text)
