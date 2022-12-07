import time
import unittest
import configparser

import helpers
import locators

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

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
        capabilities['udid'] = '9887e8343439443447'
        capabilities['platformName'] = 'Android'
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

        helpers.device_action(self.driver, "Home")
        helpers.launch_app(self.driver, "com.samsung.android.dialer/.DialtactsActivity")

        helpers.wait_for_element_to_be_clickable(self.driver, locators.android_call_state_text)

        value = helpers.get_text_from_element(self.driver, locators.android_call_state_text)
        print(value)

        try:
            if value == "Calling…":
                helpers.seetest_logger(self.driver, "Attempting to make a call with status 'Calling…'", "true")
        except:
            helpers.seetest_logger(self.driver, value, "true")

    def test_receive_a_phone_call(self):
        print('hello world')

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(PhoneCallScenarios)
