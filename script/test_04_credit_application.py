import time

from base.base_page import BasePage
from script import log


class TestCreditApplication():
    def test_01_credit_application_success(self,cda_driver):
        try:
            # 调用方法
            cda = cda_driver
            cda.switch_role()
            cda.apply(10000,"测试额度")
            
            # 打印日志
            res = cda.get_success_result()
            log.info(f"申请成功：{res}")
            # 断言
            assert res == "10,000.00"
            # 截图
            cda.get_shot("credit_application_success.png")
        except Exception as e:
            log.error(f"申请失败：{e}")
            cda.get_shot("credit_application_fail.png")