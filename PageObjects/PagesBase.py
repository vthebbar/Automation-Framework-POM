from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

'''Base page for all pages, contains common/generic action methods for all pages'''
''' This is base page for other pages'''

class PagesBase:

    def __init__(self, driver):
        self.driver = driver

    def do_send_keys(self, locator, value):
        wait = WebDriverWait(self.driver,10)
        wait.until(ec.visibility_of_element_located(locator)).send_keys(value)

    def get_element_text(self, locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element.text

    def get_title(self, title_vale):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.title_is(title_vale))
        return self.driver.title

    def do_click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(locator)).click()

    def do_navigation(self,locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(locator)).click()

    def move_to_element(self,locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(locator).click().perform()

    def verify_presence_of_element(self,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.visibility_of_element_located(locator))
        return bool(element)
