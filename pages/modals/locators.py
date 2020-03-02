from selenium.webdriver.common.by import By


class ModalLocators:
    SIGN_IN = (By.CSS_SELECTOR, '#sign-in')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'div.form-group.ng-tns-c68-0 > div:nth-child(2) > input')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.form-group.ng-tns-c68-0 > div:nth-child(4) > input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'div.form-group__submit__content_button.ng-tns-c68-0 > button')



