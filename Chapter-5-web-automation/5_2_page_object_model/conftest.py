import pytest
from selenium import webdriver
import os


@pytest.fixture()
def browser():
    # driver = webdriver.Chrome()
    driver = get_browser()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def get_browser():
    number = os.getenv('PYTEST_XDIST_WORKER')
    count = os.getenv('PYTEST_XDIST_WORKER_COUNT')
    print(f"number: {number} \t count: {count}")

    if count is None:
        return webdriver.Chrome()
    
    if number == 'gw1':
        return webdriver.Safari()
    else:
        return webdriver.Chrome()