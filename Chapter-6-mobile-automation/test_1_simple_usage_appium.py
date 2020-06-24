"""
Let's start automation for android app
asume you already have:
1. Appium server up and running in port 4723
2. Have installed Google Meet app in your android

"""

from appium import webdriver

caps = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'appPackage': 'com.google.android.apps.meetings',
    'appActivity': '.splash.SplashActivity',
    'noReset': True
}


def test_direct_usage():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(5)
    driver.find_element_by_id('enter_meeting_code_button').click()
    driver.quit()