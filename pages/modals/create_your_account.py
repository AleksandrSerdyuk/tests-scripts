from webelements import InputField, Button, TextElement
from pages.modals.locators import ModalLocators
from pages.BasePage import BasePage


class Modal(BasePage):
    """
    The class describes page of product
    """
    SIGN_IN_BUTTON = Button(ModalLocators.SIGN_IN)
    EMAIL_FIELD = InputField(ModalLocators.EMAIL_FIELD)
    PASSWORD_FIELD = InputField(ModalLocators.PASSWORD_FIELD)
    SUBMIT_BUTTON = Button(ModalLocators.SUBMIT_BUTTON)

    def click_sign_in(self):
        self.SIGN_IN_BUTTON.click()

    def login(self, email, password):
        self.EMAIL_FIELD.send_keys(email)
        self.PASSWORD_FIELD.send_keys(password)
        self.SUBMIT_BUTTON.click()
