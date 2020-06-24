from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GoogleHomePage():
    URL = 'https://www.google.co.id/'
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, browser: webdriver.Remote):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)

    def search_for(self, something: str):
        search_box = self.browser.find_element(*self.SEARCH_INPUT)
        search_box.send_keys(something + Keys.ENTER)
        time.sleep(3)