from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config import BACK_URL


class PageBackLogin(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.username = (By.ID,"username")
        self.password = (By.ID,"password")
        self.valicode = (By.ID,"valicode")
        self.lg_btn = (By.CLASS_NAME,"login-button")
        self.lo_success = (By.XPATH,"//span[contains(@class,'user-info')]")


    def open_url(self):
        self.driver.get(BACK_URL)

    def back_login(self,username,password):
        self.send_keys(self.username,username)
        self.send_keys(self.password,password)
        self.send_keys(self.valicode,"8888")
        self.click(self.lg_btn)

    def get_lg_success_re(self):
        return self.find_element_wait(self.lo_success).text