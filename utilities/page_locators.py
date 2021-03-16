"""
This file contains locators for all the pages in the Integration Test Application
"""
from selenium.webdriver.common.by import By


class PageLocators(object):
    # --- Integration Test Home Page Locators ---
    EmployeeName = By.ID, "FL:_ctl0:_ctl3"
    Summary = (By.ID, "FL:_ctl1:_ctl4")
    # Department = (By.XPATH, '//select[@id="FL:_ctl3:_ctl3"]/option')
    Department = (By.ID, "FL:_ctl3:_ctl3")
    Salary = (By.ID, "FL:_ctl4:_ctl3")
    AddressLat = (By.ID, "FL_latTxt_5")
    AddressLong = (By.ID, "FL_longTxt_5")
    # WorkLocation = (By.ID, "FL:_ctl6:_ctl3")
    WorkLocation = (By.XPATH, '//select[ @ id = "FL:_ctl6:_ctl3"]')
    DateOfJoining = (By.ID, "FL:_ctl8:_ctl3")
    EmployeeActiveYes = (By.ID, "FL__ctl3_9")
    EmployeeActiveNo = (By.ID, "FL__ctl5_9")
    CubicleLength = (By.XPATH, "(//*[text() = 'Employee Details']/..//table//input)[1]")
    CubicleLengthMetric = (By.XPATH, "(//*[text() = 'Employee Details']/..//table//select)[1]")
    CubicleWidth = (By.XPATH, "(//*[text() = 'Employee Details']/..//table//input)[2]")
    CubicleWidthMetric = (By.XPATH, "(//*[text() = 'Employee Details']/..//table//select)[2]")
    CubicleColor = (By.XPATH, "(//*[text() = 'Employee Details']/..//table//input)[3]")
    CarDetails = (By.XPATH, "//*[text() = 'Car Details']/..//table//tr[%s]/td[%s]//input")
    SubmitButton = (By.XPATH, "//button[@class='btn btn-primary']")

    # --- Integration Test Results Page Locators ---
