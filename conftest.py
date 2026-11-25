import pytest

from page.page_back_login import PageBackLogin
from page.page_login import PageLogin
from page.page_open_account import PageOpenAccount
from page.page_register import PageRegister
from page.token_application import PageApplication
from tools import DriverTools


@pytest.fixture(scope="function")
def lg_driver():
    driver = DriverTools.get_driver()
    lg = PageLogin(driver)
    yield lg
    DriverTools.quit_driver()

@pytest.fixture(scope="function")
def rg_driver():
    driver = DriverTools.get_driver()
    rg = PageRegister(driver)
    yield rg
    DriverTools.quit_driver()

@pytest.fixture(scope="function")
def op_driver():
    driver = DriverTools.get_driver()
    op = PageOpenAccount(driver)
    yield op
    DriverTools.quit_driver()

@pytest.fixture(scope="function")
def cda_driver():
    dr = DriverTools.get_driver()
    lg = PageLogin(dr)
    lg.open_url()
    lg.login("13800001001","Aa123456")
    cda = PageApplication(dr)
    yield cda
    DriverTools.quit_driver()

@pytest.fixture(scope="function")
def bl_driver():
    driver = DriverTools.get_driver()
    bl = PageBackLogin(driver)
    yield bl
    DriverTools.quit_driver()