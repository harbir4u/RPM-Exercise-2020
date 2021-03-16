"""
This file contains the child class of BasePage class and contains specific functions for use in the tests
"""
from selenium.webdriver.common.by import By
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

    def enter_employee_name(self, text):
        self.enter_text(self.locator.EmployeeName, text)

    def enter_summary(self, text):
        self.enter_text(self.locator.Summary, text)

    def select_department_from_dropdown(self, text):
        self.select_from_dropdown(self.locator.Department, text)

    def enter_salary(self, text):
        self.enter_text(self.locator.Salary, text)
        # self.driver.find_element(By.ID, "FL:_ctl4:_ctl3").send_keys(text)

    def enter_address(self, lat, long):
        self.enter_text(self.locator.AddressLat, lat)
        self.enter_text(self.locator.AddressLong, long)

    def select_work_location_from_dropdown(self, text):
        self.select_from_dropdown(self.locator.WorkLocation, text)

    def enter_date_of_joining(self, text):
        self.enter_text(self.locator.DateOfJoining, text)

    def select_employee_active_yes(self):
        self.click(self.locator.EmployeeActiveYes)

    def enter_cubicle_length(self, text):
        self.enter_text(self.locator.CubicleLength, text)

    def select_length_metric(self, text):
        self.select_from_dropdown(self.locator.CubicleLengthMetric, text)

    def enter_cubicle_width(self, text):
        self.enter_text(self.locator.CubicleWidth, text)

    def select_width_metric(self, text):
        self.select_from_dropdown(self.locator.CubicleWidthMetric, text)

    def enter_cubicle_color(self, text):
        self.enter_text(self.locator.CubicleColor, text)

    def fill_car_details(self, row, column, text):
        options = self.driver.find_element(By.XPATH,
                                           "//*[text() = 'Car Details']/..//table//tr[%s]/td[%s]//input" % (
                                               row, column))
        options.send_keys(text)

    def click_submit_button(self):
        self.click(self.locator.SubmitButton)
