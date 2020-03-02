from selenium.webdriver.common.by import By


class HeaderLocators:
    MY_ORDERS = (By.CSS_SELECTOR, 'div.calc-btn.button.button-new.button-dashboard.header')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div.header-search.js-app-search-suggest > form > button')
    BURGER_MENU = (By.CSS_SELECTOR, 'div.nav__right-side__hamburger-logo.user-logo.ng-star-inserted')
    SIGN_OUT = (By.CSS_SELECTOR, 'section div.auth div')


class ProductLocators:
    TITLE_PRODUCT = (By.CSS_SELECTOR, 'body h1')
