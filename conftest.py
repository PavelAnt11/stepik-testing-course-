import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en")


# pytest --language=es test_items.py
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.set_preference('intl.accept_languages', user_language)
    browser = webdriver.Firefox(options=options)
    # fp = webdriver.FirefoxProfile()
    # fp.set_preference("intl.accept_languages", user_language)
    # browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit()
