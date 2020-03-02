from pages.ProductPage import ProductPage
from time import sleep


class TestLogin():

    # def test_login(self, login):
    #     page = ProductPage()
    #     assert True

    def test_sign_out(self, login):
        page = ProductPage()
        sleep(2)
        page.hover_burger_menu()
        page.sign_out()


