import json
import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config import PATH

class DriverTools:
    driver = None

    """浏览器驱动工具"""
    @classmethod
    def get_driver(cls):
        """获取浏览器驱动"""
        if cls.driver is None:
            # 打开浏览器（创建浏览器驱动对象）
            path = r"D:\WebDriver\chromedriver.exe"
            ser = Service(executable_path=path)
            cls.driver = webdriver.Chrome(service=ser)
            # 浏览器最大化
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


def read_json(file_name):
    """
    读取JSON文件并转换为格式为 [(), (), ...] 的列表
    :param file_name: json 文件名
    :return: 列表
    """
    data = []
    # 拼接文件路径：全局路径 + "/data/" + 文件名
    file_path = os.path.join(PATH,"data",file_name)

    # 以只读模式、UTF-8 编码打开文件
    with open(file_path, mode='r', encoding='utf-8') as f:
        # 将 JSON 文件解析为 Python 对象 (通常是一个包含字典的列表)
        tmp = json.load(f)

        # 遍历解析出来的列表
        for i in tmp:
            # 提取字典中所有的值 (values)，并转换为元组 (tuple)
            a = tuple(i.values())
            # 将元组追加到 data 列表中
            data.append(a)

    # 返回最终的列表
    return data


import logging
import logging.handlers
from config import PATH  # 假设你的路径是从 config.py 导入的


class GetLog:
    # 日志器
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename =os.path.join(PATH,"log","web.log")
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,  # 日志文件名
                                                           when="midnight",  # 日志归档时间
                                                           interval=1,  # 每天归档一次
                                                           backupCount=3,  # 保留3天日志
                                                           encoding="utf-8")  # 日志编码格式

            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)

        # 返回日志器
        return cls.__log

if __name__ == "__main__":
    DriverTools.get_driver().get("https://baidu.com")
    DriverTools.quit_driver()