import os
from config import PATH
from anyio.streams import file
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools import GetLog


class BasePage:
    """所有页面的父类"""
    def __init__(self, driver):
        self.driver = driver

    def find_element_wait(self,locator,timeout=10):
        """封装显式等待，返回找到的元素"""
        try:
            return WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            GetLog.get_log().error(f"元素定位超市，定位信息：{locator},错误详情：{e}")
            raise # 重新抛出异常供上层处理

    def click(self,locator,timeout=10):
        """封装点击操作"""
        element = self.find_element_wait(locator,timeout)
        element.click()

    def send_keys(self,locator,text,timeout=10):
        element = self.find_element_wait(locator,timeout)
        element.clear()
        element.send_keys(text)

    def get_shot(self,file_name):
        """截图"""
        file_path = os.path.join(PATH, './img', file_name+'.png')
        self.driver.get_screenshot_as_file(file_path)

    def switch_frame(self,loc):
        frame_ele = self.find_element_wait(loc)
        self.driver.switch_to.frame(frame_ele)