from script import log


class TestOpenAccount:

    def test_01_open_account_success(self,lg_driver,op_driver):
        lg = lg_driver
        lg.open_url()
        lg.login("75213654147","Aa123456")
        op = op_driver
        op.open_account("张三","723001199805126417")
        res = op.get_success_result()
        log.info(f"开户结果：{res}")
        assert res == "UserRegister OK"