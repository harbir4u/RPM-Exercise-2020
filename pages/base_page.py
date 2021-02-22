"""
This file contains the parent class for all the pages in the Integration Test.
It contains all generic functions available to all pages.
"""
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    # This function is called every time a new object of the BasePage class is created.
    def __init__(self, driver, base_url='https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 4

    # This function clicks on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # This function enters text in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # This function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # the web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    #  This function stores text from a locator which is passed through it and returns the text
    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
