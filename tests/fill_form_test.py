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
        page = IntegrationTestHomePage(self.driver)
        page.enter_employee_name(TestData.EMPLOYEE_NAME)
        print("Entered Employee name:", TestData.EMPLOYEE_NAME)
        page.enter_summary(TestData.SUMMARY)
        print("Entered summary:", TestData.SUMMARY)
        page.select_department_from_dropdown(TestData.DEPARTMENT)
        print("Selected Department:", TestData.DEPARTMENT)
        page.enter_salary(TestData.SALARY)
        print("Entered Salary")
        page.enter_address(TestData.ADDRESS_LAT, TestData.ADDRESS_LONG)
        print("Entered Address Lat:", TestData.ADDRESS_LAT)
        print("Entered Address Long:", TestData.ADDRESS_LONG)
        page.select_work_location_from_dropdown(TestData.WORK_LOCATION)
        print("Selected Work Location:", TestData.WORK_LOCATION)
        page.enter_date_of_joining(TestData.DATE_OF_JOINING)
        print("Entered Date of Joining:", TestData.DATE_OF_JOINING)
        page.select_employee_active_yes()
        page.enter_cubicle_length(TestData.CUBICLE_LENGTH)
        print("Entered Cubicle Length:", TestData.CUBICLE_LENGTH)
        page.enter_cubicle_width(TestData.CUBICLE_WIDTH)
        print("Entered Cubicle Width:", TestData.CUBICLE_WIDTH)
        page.select_length_metric(TestData.METRIC)
        print("Selected Length Metric:", TestData.METRIC)
        page.select_width_metric(TestData.METRIC)
        print("Selected Width Metric:", TestData.METRIC)
        page.enter_cubicle_color(TestData.CUBICLE_COLOR)
        print("Selected Cubicle Color:", TestData.CUBICLE_COLOR)
        page.fill_car_details(2, 2, TestData.CAR1_BRAND)
        print("Entered Car 1 Brand:", TestData.CAR1_BRAND)
        page.fill_car_details(2, 3, TestData.CAR1_MODEL)
        print("Entered Car 1 Model:", TestData.CAR1_MODEL)
        page.fill_car_details(2, 4, TestData.CAR1_MODEL_YEAR)
        print("Entered Car 1 Model year:", TestData.CAR1_MODEL_YEAR)
        page.fill_car_details(2, 5, TestData.CAR1_TRIM)
        print("Entered Car 1 Trim:", TestData.CAR1_TRIM)
        page.fill_car_details(2, 6, TestData.CAR1_COLOR)
        print("Entered Car 1 Color:", TestData.CAR1_COLOR)
        page.fill_car_details(2, 7, TestData.CAR1_LICENCE_PLATE)
        print("Entered Car 1 Licence plate:", TestData.CAR1_LICENCE_PLATE)
        page.fill_car_details(3, 2, TestData.CAR2_BRAND)
        print("Entered Car 2 Brand:", TestData.CAR2_BRAND)
        page.fill_car_details(3, 3, TestData.CAR2_MODEL)
        print("Entered Car 2 Model:", TestData.CAR2_MODEL)
        page.fill_car_details(3, 4, TestData.CAR2_MODEL_YEAR)
        print("Entered Car 2 Model year:", TestData.CAR2_MODEL_YEAR)
        page.fill_car_details(3, 5, TestData.CAR2_TRIM)
        print("Entered Car 2 Trim:", TestData.CAR2_TRIM)
        page.fill_car_details(3, 6, TestData.CAR2_COLOR)
        print("Entered Car 2 Color:", TestData.CAR2_COLOR)
        page.fill_car_details(3, 7, TestData.CAR2_LICENCE_PLATE)
        print("Entered Car 2 Licence plate:", TestData.CAR2_LICENCE_PLATE)
        page.click_submit_button()
        print("Submit button clicked")
        time.sleep(15)
