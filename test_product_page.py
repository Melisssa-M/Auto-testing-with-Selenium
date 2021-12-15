from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
import pytest


@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/{browser.language}/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    product_page.solve_quiz_and_get_code()


def test_price_and_name_are_same_in_basket(browser):
    test_guest_can_add_product_to_basket(browser)
    price_of_item = browser.find_element(*ProductPageLocators.PRICE_OF_ITEM).text
    price_pop_up = browser.find_element(*ProductPageLocators.PRICE_POP_UP).text
    name_of_item = browser.find_element(*ProductPageLocators.NAME_OF_ITEM).text
    name_pop_up = browser.find_element(*ProductPageLocators.NAME_POP_UP).text
    assert price_of_item == price_pop_up and name_of_item == name_pop_up, f"{price_of_item} != {price_pop_up} or {name_of_item} != {name_pop_up} "

