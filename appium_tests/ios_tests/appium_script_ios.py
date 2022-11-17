import unittest
import configparser

import helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


class CheckDeviceWiFiStateiOS(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = 'iOS_Test_Python'
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '00008020-0005656621A2002E'
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = False  # Disable report creation, will help to reduce execution time
        capabilities['bundleId'] = 'com.apple.Preferences'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_wifi_connection(self):
        self.driver.find_element(By.XPATH, "//*[@id='WIFI']").click()

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(CheckDeviceWiFiStateiOS)