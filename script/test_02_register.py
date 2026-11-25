
from script import log

class TestRegister:
    def test_02_register_success(self,rg_driver):
        rg = rg_driver
        rg.open_url()
        rg.register("75213654147","Aa123456","8888","666666")
        res = rg.get_success_result()
        log.info(f"注册结果：{res}")
        assert "注册成功" in res

    def est_02_register_fail(self,rg_driver):
        rg = rg_driver
        rg.open_url()
        rg.register("45213653147","Aa123456","8888","666666")
        res = rg.get_fail_phone_exist()
        log.info(f"注册结果：{res}")
        assert "注册" in res