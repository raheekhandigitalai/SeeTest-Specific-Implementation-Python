import time
import unittest
import configparser

from config import locators, helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for Android only
capabilities = DesiredCapabilities.ANDROID


class PhoneCallScenarios(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_android_udid()
        capabilities['platformName'] = 'Android'
        capabilities['generateReport'] = True  # If setting to False, disables report creation, may help to reduce execution time
        capabilities['appPackage'] = 'com.samsung.android.dialer'
        capabilities['appActivity'] = '.DialtactsActivity'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_make_a_phone_call(self):
        phone_number = [3, 4, 7, 9, 3, 5, 6, 4, 4, 2]

        for number in phone_number:
            helpers.click_on_element(self.driver, "//*[@id='dialpad_key_number' and @text='" + str(number) + "']")
            time.sleep(0.5)

        helpers.click_on_element(self.driver, locators.android_call_button)

        # helpers.device_action(self.driver, "Home")
        # helpers.launch_app(self.driver, "com.samsung.android.dialer/.DialtactsActivity")

        helpers.wait_for_element_to_be_clickable(self.driver, locators.android_call_state_text)

        value = helpers.get_text_from_element(self.driver, locators.android_call_state_text)
        print(value)

        try:
            if value == "Calling…":
                helpers.seetest_logger(self.driver, "Attempting to make a call with status 'Calling…'", "true")
                helpers.click_on_element(self.driver, locators.android_disconnect_button)
        except:
            helpers.seetest_logger(self.driver, value, "true")

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()
