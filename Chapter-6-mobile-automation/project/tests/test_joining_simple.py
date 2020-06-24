import time
from appium import webdriver

caps = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'appPackage': 'com.google.android.apps.meetings',
    'appActivity': '.splash.SplashActivity',
    'noReset': True,
    'automationName': 'UiAutomator2'
}


class TestJoiningSimple():
    driver = None

    def create_driver(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def test_join_meeting(self):
        self.create_driver()
        self.driver.find_element_by_id('enter_meeting_code_button').click()
        time.sleep(3)
        self.driver.find_element_by_id('join_meeting_edittext').send_keys('wfn-enks-pcj')
        self.driver.find_element_by_id('join_meeting_positive_button').click()
        self.driver.find_element_by_id('greenroom_join_button').click()
        assert self.driver.find_element_by_id('greenroom_sub_header').text == "You'll join the meeting when someone lets you in"
        time.sleep(5)
        self.driver.quit()
