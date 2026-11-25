import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageCreditReview(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.loan_manager = By.LINK_TEXT,"借款管理"
        self.limit_manager = By.XPATH,"//span[text()='额度管理']"
        self.app_review = By.LINK_TEXT,"额度申请审核"

        self.frame1 = By.ID,"iframe_box"
        self.membername = By.NAME,"member_name"
        self.search_btn = By.CSS_SELECTOR,"[value='搜索']"
        
        self.select_rec = By.XPATH,"/html/body/div[2]/div[3]/table/tbody/tr[1]/td[2]/span"
        self.review_btn = By.XPATH,"/html/body/div[2]/div[2]/ul/li[1]/a/span"

        self.frame2 = By.ID,"xubox_iframe1"
        self.pass_btn = By.XPATH,"/html/body/div[2]/form/table/tbody/tr[5]/td[2]/div/label[1]/span"
        self.valicode = By.NAME,"valicode"
        self.save_btn = By.CLASS_NAME,"dybtn-save"

    def menu_manager(self):
        self.click(self.loan_manager)
        self.click(self.limit_manager)
        self.click(self.app_review)

    def serch_record(self,phone):
        self.switch_frame(self.frame1)
        self.send_keys(self.select_rec,phone)
        self.click(self.search_btn)
        time.sleep(2)

    def select_record(self):
        self.click(self.select_rec)
        self.click(self.review_btn)

    def review_commit(self):
        self.switch_frame(self.frame2)
        self.click(self.pass_btn)
        self.send_keys(self.valicode,"8888")
        self.click(self.save_btn)

