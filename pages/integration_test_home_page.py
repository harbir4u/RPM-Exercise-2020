"""
This file contains the child class of BasePage class and contains specific functions for use in the tests
"""
from selenium.webdriver.support.select import Select
from utilities.page_locators import PageLocators
from utilities.test_data import TestData
from pages.base_page import BasePage


# Contains functions that perform actions on the Integration Test HomePage
class IntegrationTestHomePage(BasePage):

    def __init__(self, driver):
        self.locator = PageLocators
        self.testdata = TestData
        super().__init__(driver)

    def fill_employee_name(self, text):
        self.enter_text(self.locator.EmployeeName, text)

    def fill_summary(self, text):
        self.enter_text(self.locator.Summary, text)

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
