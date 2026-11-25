from time import time

from selenium.webdriver.common.by import By
import time
from base.base_page import BasePage
from config import BASE_URL


class PageRegister(BasePage):
    """注册页面类"""

    def __init__(self,driver):
        """初始化方法"""
        super().__init__(driver)
        # 设置页面实例属性
        self.phone_loc = (By.ID,"phone")
        self.password_loc = (By.ID,"password")
        self.verifycode_loc = (By.ID,"verifycode")
        self.get_phone_code_btn_loc = (By.ID,"get_phone_code")
        self.get_phone_code_loc = (By.ID,"phone_code")
        self.register_btn_loc = (By.CLASS_NAME,"lg-btn")
        self.success_result = (By.CSS_SELECTOR,"#step3 > div > div > h1 ")
        self.fail_phone_exist_result = (By.CLASS_NAME,"reg-title")

    def open_url(self):
        print(BASE_URL + "/common/member/reg")
        self.driver.get(BASE_URL+"/common/member/reg")

    def register(self,phone,password,verifycode,phone_code,):
        self.send_keys(self.phone_loc,phone)
        self.send_keys(self.password_loc,password)
        self.send_keys(self.verifycode_loc,verifycode)
        self.click(self.get_phone_code_btn_loc)
        time.sleep(2)
        self.send_keys(self.get_phone_code_loc,phone_code)
        self.click(self.register_btn_loc)

    def get_success_result(self):
        res = self.find_element_wait(self.success_result)
        return res.text

    def get_fail_phone_exist(self):
        res = self.find_element_wait(self.fail_phone_exist_result)
        return res.text

