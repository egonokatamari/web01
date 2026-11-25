from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageApplication(BasePage):
    """额度申请页面类"""
    def __init__(self,driver):
        super().__init__(driver)

        self.change_acc = (By.XPATH,"//em[text()='借款账户']")
        # self.change_acc = (By.CSS_SELECTOR,"div.change-role>a")
        self.application = (By.LINK_TEXT,"申请额度")
        self.token =(By.NAME,"amount_account")
        self.description = (By.CLASS_NAME,"lg-area")
        self.verifycode = (By.ID,"verifycode")
        self.commit_btn = (By.CSS_SELECTOR,"[type='submit']")
        self.application_success = (By.XPATH,"//*[@id='amount_list']/tr[1]/td[3]")

    def switch_role(self):
        self.click(self.change_acc)

    def apply(self,token,description):
        self.click(self.application)
        self.send_keys(self.token,token)
        self.send_keys(self.description,description)
        self.send_keys(self.verifycode,"8888")
        self.click(self.commit_btn)

    def get_success_result(self):
        res = self.find_element_wait(self.application_success)
        return res.text

