from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
from pages.locators import Links


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = browser.link
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = browser.link
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_should_see_login_form(browser):
    link = browser.link + Links.LOGIN_LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


@pytest.mark.skip
def test_guest_should_see_registration_form(browser):
    link = browser.link + Links.LOGIN_LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


@pytest.mark.skip
def test_guest_should_see_login_page(browser):
    link = browser.link + Links.LOGIN_LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()



def test_guest_should_see_login_page_full_check(browser):
    link = browser.link + Links.LOGIN_LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()