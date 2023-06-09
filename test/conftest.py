import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    time.sleep(30)
    browser.quit()
