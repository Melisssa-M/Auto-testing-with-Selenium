from pages.locators import ProductPageLocators
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    product_page.solve_quiz_and_get_code()
