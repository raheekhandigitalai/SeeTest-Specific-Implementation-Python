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


class DeviceSettingsScenarios(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '9887e8343439443447'
        capabilities['platformName'] = 'Android'
        capabilities['appPackage'] = 'com.android.settings'
        capabilities['appActivity'] = '.Settings'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def change_volte_settings(self):
        helpers.wait_for_element_to_be_clickable(self.driver, locators.android_connections_button)
        helpers.click_on_element(self.driver, locators.android_connections_button)

        helpers.wait_for_element_to_be_clickable(self.driver, locators.android_mobile_networks_button)
        helpers.click_on_element(self.driver, locators.android_mobile_networks_button)

        helpers.wait_for_element_to_be_clickable(self.driver, locators.android_volte_calls_toggle)

        value = helpers.get_text_from_element(self.driver, locators.android_volte_calls_toggle)
        print(value)

        try:
            if value == 'On':
                helpers.seetest_logger(self.driver, "voLTE call is enabled, attempting to toggle Off and On", "true")
                helpers.click_on_element(self.driver, locators.android_volte_calls_toggle)
                time.sleep(3)
                helpers.click_on_element(self.driver, locators.android_volte_calls_toggle)
        except:
            helpers.seetest_logger(self.driver, "voLTE call is not enabled, attempting to toggle on", "true")
            helpers.click_on_element(self.driver, locators.android_volte_calls_toggle)

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(DeviceSettingsScenarios)