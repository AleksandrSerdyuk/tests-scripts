import pytest

from webdriver import web_driver
from utils.config import url
from pages.ProductPage import ProductPage
from pages.modals.create_your_account import Modal
from utils.config import email, password


@pytest.yield_fixture()
def driver():
    web_driver.start(url)
    yield
    web_driver.quit()


@pytest.yield_fixture()
def login(driver):
    #check loged in user

    page = ProductPage()
    modal = Modal()
    page.click_my_orders()
    modal.click_sign_in()
    modal.login(email, password)
