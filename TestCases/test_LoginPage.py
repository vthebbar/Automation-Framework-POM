import pytest
from Config.config import TestInfo
from PageObjects.LoginPage import LoginPage
from TestCases.test_Base import BaseTest
from Utility.Logger import LogGen

class TestLogin_001(BaseTest):

    logger = LogGen.log_gen()

    logger.info("*****Start of TestLogin_001******")

    def test_forgot_password_link_visible(self,driver_setup):
        self.logger.info("****starting test_forgot_password_link_visible()*****")
        self.driver = driver_setup
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_forgot_password_link_present()
        # assert flag, "Forgot password link not found"
        if flag == True:
            self.logger.info("*****Passed -test_forgot_password_link_visible() ***")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Snapshots\\"+"test_forgot_password_link_visible.png")
            self.driver.close()
            self.logger.info("******Failed - test_forgot_password_link_visible()**********")
            assert False

    def test_signup_link_visible(self,driver_setup):
        self.driver = driver_setup
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_register_link_present()
        #assert flag, "Register link element not found"
        if flag == True:
            self.logger.info("*** Passed -test_signup_link_visible *** ")
            assert True
            self.driver.close()
        else:
            self.logger.info("*** Failed - test_signup_link_visible ***")
            self.driver.save_screenshot(".\\Snapshots\\"+"test_signup_link_visible.png")
            self.driver.close()
            assert False

    def test_login_page_title(self,driver_setup):
        self.logger.info("*** Starting - test_login_page_title ***")
        self.driver = driver_setup
        self.loginPage = LoginPage(self.driver)
        act_title = self.loginPage.get_login_page_title(TestInfo.login_page_title)
        #assert act_title == TestInfo.login_page_title , "Title not as expected"
        if act_title == TestInfo.login_page_title:
            assert True
            self.logger.info("*** Passed - test_login_page_title ")
            self.driver.close()
        else:
            self.logger.info("*** Failed -test_login_page_title *** ")
            self.driver.save_screenshot(".\\Snapshots\\"+"test_login_page_title.png")
            self.driver.close()
            assert False

    def test_login(self,driver_setup):
        self.logger.info("*** Starting -test_login ")
        self.driver = driver_setup
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestInfo.login_id, TestInfo.password)
        #assert self.driver.title == TestInfo.home_page_title
        if self.driver.title == TestInfo.home_page_title:
            self.logger.info("****Passed -test_login *** ")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Failed-test_login ***")
            self.driver.save_screenshot(".\\Snapshots\\"+"test_login.png")
            self.driver.close()
            assert False
    logger.info("*****End of TestLogin_001******")




