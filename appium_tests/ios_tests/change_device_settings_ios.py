import unittest
import configparser

from config import helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By

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
        capabilities['generateReport'] = False  # Disable report creation, will help to reduce execution time
        capabilities['bundleId'] = 'com.apple.Preferences'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_change_volte_settings(self):
        self.driver.find_element(By.XPATH, "//*[@id='WIFI']").click()

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(DeviceSettingsScenarios)
