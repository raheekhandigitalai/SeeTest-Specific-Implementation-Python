import unittest
import configparser

import helpers
from helpers import logger

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for Android only
capabilities = DesiredCapabilities.ANDROID


class CheckDeviceWiFiStateAndroid(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = 'Android_Test_Python'
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = ''
        capabilities['platformName'] = 'Android'
        capabilities['generateReport'] = False  # Disable report creation, will help to reduce execution time

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_wifi_connection(self):
        # Storing device Serial Number to variable
        device_udid = self.driver.capabilities['udid']
        logger(device_udid)

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(CheckDeviceWiFiStateAndroid)