from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestSearching:

    @classmethod
    def setup_class(cls):
        print("Before test")
        cls.DRIVER = webdriver.Chrome()
        cls.DRIVER.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        print("After test")
        cls.DRIVER.quit()

    def test_searching_golife(self):
        print("Test searching golife")
        self.DRIVER.get('https://google.co.id')
        search_box = self.DRIVER.find_element_by_name('q')
        search_box.send_keys('Golife'+ Keys.ENTER)
        time.sleep(3)
        print(self.DRIVER.title)

    def test_searching_gojek(self):
        self.DRIVER.get('https://google.co.id')
        search_box = self.DRIVER.find_element_by_name('q')
        search_box.send_keys('Gojek'+ Keys.ENTER)
        time.sleep(3)
        print(self.DRIVER.title)
