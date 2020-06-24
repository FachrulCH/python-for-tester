from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class TestGoogling():
    def test_search_fachrul(self, browser:webdriver.Remote):
        browser.get('https://google.co.id')
        browser.find_element_by_name('q').send_keys('Fachrul Choliluddin linkedin'+ Keys.ENTER)
        time.sleep(3)
        assert 'Fachrul Choliluddin' in browser.title
        results = browser.find_elements_by_css_selector('.r a h3')
        target = random.choice(results)
        print('hasil', target.text)
        target.click()
        time.sleep(5)
        assert 'fachrul' in str(browser.title).lower()