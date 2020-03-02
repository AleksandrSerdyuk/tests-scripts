from .locators import ProductLocators as _product_locators
from .locators import HeaderLocators as _header_locators
from webelements import InputField, Button, TextElement, Element
from pages.BasePage import BasePage


class Header:
    """
    The class describes header of site
    """
    MY_ORDERS_BUTTON = Button(_header_locators.MY_ORDERS)
    BURGER_MENU = Element(_header_locators.BURGER_MENU)
    SIGN_OUT = Button(_header_locators.SIGN_OUT)

    def click_my_orders(self):
        self.MY_ORDERS_BUTTON.click()

    def hover_burger_menu(self):
        self.BURGER_MENU.move_to()

    def sign_out(self):
        self.SIGN_OUT.click()


class ProductPage(BasePage, Header):
    """
    The class describes page of product
    """
    PRODUCT_TITLE = TextElement(_product_locators.TITLE_PRODUCT)

    @property
    def product_title(self):
        self.wait_for_page_to_open()
        return self.PRODUCT_TITLE.text

    def is_opened(self):
        return self.PRODUCT_TITLE.is_displayed()
