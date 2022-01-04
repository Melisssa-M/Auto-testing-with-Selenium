from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_POP_UP = (By.CSS_SELECTOR, "div.fade.in > div > p:nth-child(1) > strong")
    PRICE_OF_ITEM = (By.CSS_SELECTOR, "p.price_color")
    NAME_OF_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    NAME_POP_UP = (By.CSS_SELECTOR, ".product_main h1")


class Links:
    LOGIN_LINK = 'accounts/login/'
    PRODUCT_FOR_TEST_LINK = 'catalogue/coders-at-work_207/'
    PRODUCT_FOR_TEST_2_LINK = 'catalogue/the-city-and-the-stars_95/'


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
