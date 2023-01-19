import time
import unittest
import configparser

from config import helpers, locators
from appium import webdriver

from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

config = configparser.ConfigParser()
config.read('config.properties')

capabilities = {}


class PhoneCallMultiDeviceAndroid(unittest.TestCase):

    phone_number = "3413452774"

    def setUp(self):
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_android_udid()
        capabilities['platformName'] = 'Android'
        capabilities['appPackage'] = 'com.samsung.android.dialer'
        capabilities['appActivity'] = '.DialtactsActivity'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_make_phone_call(self):
        phone_number_list = [n for n in self.phone_number]

        helpers.click_on_element(self.driver, locators.android_keypad_button)

        for number in phone_number_list:
            helpers.click_on_element(self.driver, "//*[@id='dialpad_key_number' and @text='" + str(number) + "']")
            time.sleep(0.5)

        helpers.click_on_element(self.driver, locators.android_call_button)

        helpers.wait_for_element_to_be_clickable(self.driver, locators.android_call_state_text)

        value = helpers.get_text_from_element(self.driver, locators.android_call_state_text)
        print(value)

        try:
            if value == "Calling…":
                helpers.logger("Attempting to make a call with status 'Calling…'")
                time.sleep(10)
                helpers.click_on_element(self.driver, locators.android_disconnect_button)
        except:
            helpers.logger("Call did not go through or failed to disconnect")

    def tearDown(self):
        self.driver.quit()
