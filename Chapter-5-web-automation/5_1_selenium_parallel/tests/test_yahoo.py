from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class TestYahoo():
    def test_search_fachrul(self, browser: webdriver.Remote):
        browser.get('https://id.yahoo.com')
        browser.find_element_by_id('header-search-input').send_keys('github Fachrul Choliluddin' + Keys.ENTER)
        time.sleep(3)
        results = browser.find_elements_by_css_selector('h3.title')
        target = random.choice(results)
        print(target.text)
        target.click()
        time.sleep(3)
        assert 'fachrul' in str(browser.title).lower()
