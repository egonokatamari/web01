from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config import BASE_URL


class PageOpenAccount(BasePage):
    """开通账户类"""
    def __init__(self,driver):
        super().__init__(driver)
        self.open_tips_btn_loc = (By.CSS_SELECTOR,"div.new-tips > a")
        self.name_loc = (By.CSS_SELECTOR, "input[name='realname']")
        self.card_id_loc = (By.CSS_SELECTOR, "#safeName > div:nth-child(3) > input")
        self.sub_btn_loc = (By.CSS_SELECTOR, "[value='确认提交']")
        self.now_open_loc = (By.XPATH,"//input[@value='立即开通']")
        self.success_result_loc = (By.CSS_SELECTOR,"body")

#    def open_url(self):
#        self.driver.get(BASE_URL+"/common/member/login")

    def open_account(self,name,card_id):
        self.click(self.open_tips_btn_loc)
        self.send_keys(self.name_loc,name)
        self.send_keys(self.card_id_loc,card_id)
        self.click(self.sub_btn_loc)
        self.click(self.now_open_loc)

    def get_success_result(self):
        res = self.base_switch_handle(self.success_result_loc)
        return res.text