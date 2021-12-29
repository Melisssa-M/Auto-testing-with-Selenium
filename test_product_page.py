from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.locators import Links
import pytest


@pytest.mark.skip
@pytest.mark.parametrize('promo_number', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f'{browser.link}{Links.PRODUCT_FOR_TEST_LINK}?promo={promo_number}'
    product_page = ProductPage(browser, link)
    product_page.open()
    browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    product_page.solve_quiz_and_get_code()
    price_of_item = browser.find_element(*ProductPageLocators.PRICE_OF_ITEM).text
    price_pop_up = browser.find_element(*ProductPageLocators.PRICE_POP_UP).text
    name_of_item = browser.find_element(*ProductPageLocators.NAME_OF_ITEM).text
    name_pop_up = browser.find_element(*ProductPageLocators.NAME_POP_UP).text
    assert price_of_item == price_pop_up and name_of_item == name_pop_up, f"{price_of_item} != {price_pop_up} or {name_of_item} != {name_pop_up}, {promo_number}"


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = browser.link + Links.PRODUCT_FOR_TEST_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_OF_ITEM), \
        "Success message is presented, but should not be"


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = browser.link + Links.PRODUCT_FOR_TEST_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_OF_ITEM), \
        "Success message is presented, but should not be"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = browser.link + Links.PRODUCT_FOR_TEST_LINK
    product_page = ProductPage(browser, link)
    product_page.open()
    browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    assert product_page.is_disappeared(*ProductPageLocators.NAME_OF_ITEM), \
        "Success message is presented, but should disappear"