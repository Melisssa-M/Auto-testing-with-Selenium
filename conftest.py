import pytest
from selenium import webdriver
import time



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    browser.language = language
    browser.implicitly_wait(12)
    browser.link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(browser.link)
    yield browser
    time.sleep(1)
    browser.quit()
