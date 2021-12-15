from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_number', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f'http://selenium1py.pythonanywhere.com/{browser.language}/catalogue/coders-at-work_207/?promo={promo_number}'
    product_page = ProductPage(browser, link)
    product_page.open()
    browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    product_page.solve_quiz_and_get_code()
    price_of_item = browser.find_element(*ProductPageLocators.PRICE_OF_ITEM).text
    price_pop_up = browser.find_element(*ProductPageLocators.PRICE_POP_UP).text
    name_of_item = browser.find_element(*ProductPageLocators.NAME_OF_ITEM).text
    name_pop_up = browser.find_element(*ProductPageLocators.NAME_POP_UP).text
    assert price_of_item == price_pop_up and name_of_item == name_pop_up, f"{price_of_item} != {price_pop_up} or {name_of_item} != {name_pop_up}, {promo_number}"
