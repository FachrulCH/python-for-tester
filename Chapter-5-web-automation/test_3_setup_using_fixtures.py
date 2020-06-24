from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope='class')
def driver():
    # _driver = webdriver.Chrome()
    _driver = webdriver.Safari()
    _driver.implicitly_wait(5)
    yield _driver
    _driver.quit()


class TestWebFixtures():
    def test_search_golife(self, driver: webdriver.Remote):
        driver.get('https://google.co.id')
        driver.find_element_by_name('q').send_keys('Golife' +Keys.ENTER)
        time.sleep(3)
        assert driver.title == 'Golife - Penelusuran Google'

    def test_search_gojek(self, driver: webdriver.Remote):
        driver.get('https://google.co.id')
        driver.find_element_by_name('q').send_keys('Gojek'+Keys.ENTER)
        time.sleep(3)
        assert 'Gojek' in driver.title
