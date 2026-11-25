from script import log


class TestBackLogin:
    def test_01_back_login_success(self,bl_driver):
        bl = bl_driver
        bl.open_url()
        bl.back_login("admin","HM_2023_test")
        res = bl.get_lg_success_re()
        log.info(f"后台登录结果：{res}")
        assert "欢迎光临" in res
        bl.get_shot("back_login_result1")

