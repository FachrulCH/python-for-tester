from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class TestGoogling():
    def test_search_fachrul(self, browser:webdriver.Remote):
        browser.get('https://duckduckgo.com/')
        browser.find_element_by_id('search_form_input_homepage').send_keys('instagram Fachrul Choliluddin'+ Keys.ENTER)
        time.sleep(3)
        assert 'Fachrul Choliluddin' in browser.title
        results = browser.find_elements_by_css_selector('h2.result__title')
        target = random.choice(results)
        print('hasil', target.text)
        target.click()
        time.sleep(5)
        assert 'fachrul' in str(browser.title).lower()