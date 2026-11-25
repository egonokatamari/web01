import json

import pytest

from page.page_login import PageLogin
from script import log
from tools import DriverTools, read_json


class TestLogin:

    def est_01_login_success(self, lg_driver):
        # 准备数据
        # 调用方法
        lg = lg_driver
        lg.open_url()
        lg.login("13800001001","Aa123456")
        # 打印日志
        res = lg.get_success_result()
        # print(f"登陆结果：{res}")
        log.info(f"登陆结果：{res}")
        # 断言
        assert lg.get_success_result() == "13800001001"


    def est_02_login_fail_pwd_error(self,driver):
        # 准备数据
        # 调用方法
        lg =  driver
        lg.open_url()
        lg.login("13800001001","666123")
        # 打印日志
        res = lg.get_fail_pwd_error()
        # print(f"登陆结果：{res}")
        log.info(f"登陆结果：{res}")
        # 断言
        assert "密码错误" in lg.get_fail_pwd_error()

    @pytest.mark.parametrize("phone,pwd,expect",read_json("login_data.json"))
    def test_01_login(self,lg_driver,phone,pwd,expect):
        lg = lg_driver
        lg.open_url()
        lg.login(phone,pwd)
        # 打印日志
        # 判断
        if expect == phone:
            res = lg.get_success_result()
        else:
            res = lg.get_fail_pwd_error()
        # print(f"登陆结果：{res}")
        log.info(f"登陆结果：{res}")
        # 断言
        assert expect in res