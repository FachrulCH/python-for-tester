from selenium.webdriver.common.by import By
from selenium import webdriver

class GoogleResultPage():
    SEARCH_INPUT = (By.NAME, 'q')
    RESULT_LINK = (By.CSS_SELECTOR, '.r a h3')

    def __init__(self, browser: webdriver.Remote):
        self.browser = browser

    def get_search_input(self):
        return self.browser.find_element(*self.SEARCH_INPUT).get_attribute('value')

    def title(self):
        return self.browser.title