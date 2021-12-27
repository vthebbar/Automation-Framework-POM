from selenium.webdriver.common.by import By
from PageObjects.PagesBase import PagesBase
from Config.config import TestInfo

class LoginPage(PagesBase):

    """Element locators"""

    txt_emailid_id = (By.ID,"input-email")
    txt_password_id = (By.ID,"input-password")
    btn_login_xpath = (By.XPATH,"//input[@type='submit' and @value='Login']")

    lnk_forgotPassword_xpath = (By.XPATH,"//a[text()='Continue']")
    lnk_registerAcct_xpath = (By.XPATH,"//a[text()='Forgotten Password']")

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestInfo.login_page_url)

    """Action methods"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    def is_register_link_present(self):
        return self.verify_presence_of_element(self.lnk_registerAcct_xpath)

    def is_forgot_password_link_present(self):
        return self.verify_presence_of_element(self.lnk_forgotPassword_xpath)

    def do_login(self,userid, password):
        self.do_send_keys(self.txt_emailid_id, userid)
        self.do_send_keys(self.txt_password_id, password)
        self.do_click(self.btn_login_xpath)




