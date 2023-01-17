import time
import unittest
import configparser

from config import locators, helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


class DeviceSettingsScenarios(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_ios_udid()
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = True  # Disable report creation, will help to reduce execution time
        capabilities['bundleId'] = 'com.apple.Preferences'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_change_volte_settings(self):
        helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.ios_cellular_button)
        helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.ios_cellular_plans_primary_button)
        helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.ios_voice_and_data_button)

        value = helpers.get_text_from_element(self.driver, locators.ios_selected_voice_and_data_option)
        print(value)

        try:
            if value == 'LTE':
                helpers.seetest_logger(self.driver, "LTE is enabled, attempting to toggle Off and On", "true")
                helpers.click_on_element(self.driver, locators.ios_4g_option)
                time.sleep(3)
                helpers.click_on_element(self.driver, locators.ios_lte_option)
        except:
            helpers.seetest_logger(self.driver, "LTE is disabled, attempting to toggle On", "true")
            helpers.click_on_element(self.driver, locators.ios_lte_option)

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()
