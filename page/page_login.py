# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法
import time
from selenium.webdriver.common.by import By

from config import BASE_URL
from tools import DriverTools
from base.base_page import BasePage


class PageLogin(BasePage):
    """登陆页面类"""

    def __init__(self,driver):
        """初始化方法"""
        super().__init__(driver)
        # 设置页面实例属性
        self.username_loc = (By.ID,"keywords")
        self.password_loc = (By.ID,"password")
        self.login_button_loc = (By.ID,"login-btn")
        # 成功结果元素属性
        self.success_result = (By.CLASS_NAME,"a-link1")
        # 密码错误元素属性
        self.fail_pwd_error_result = (By.CSS_SELECTOR,"#err")

    def open_url(self):
        print(BASE_URL + "/common/member/login")
        self.driver.get(BASE_URL+"/common/member/login")

    def login(self,username,password):
        # 输入账号
        # self.driver.find_element(*self.username).send_keys("13800001001")
        self.send_keys(self.username_loc,username)
        # 输入密码
        # self.driver.find_element(*self.password).send_keys("Aa123456")
        self.send_keys(self.password_loc,password)
        # 点击登录
        # self.driver.find_element(*self.login_button).click()
        self.click(self.login_button_loc)
        time.sleep(3)

    def get_success_result(self):
        res = self.find_element_wait(self.success_result)
        return res.text

    def get_fail_pwd_error(self):
        res = self.find_element_wait(self.fail_pwd_error_result)
        return res.text
if __name__ == "__main__":
    try:
        driver = DriverTools.get_driver()
        lg = PageLogin(driver)
        # 打开页面
        lg.open_url()
        # 操作登录
        lg.login("13800001001","Aa123456")
    finally:
        DriverTools.quit_driver()


