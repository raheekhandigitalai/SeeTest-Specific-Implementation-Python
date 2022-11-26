import unittest
import configparser

import helpers
from helpers import logger

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        capabilities['udid'] = 'R5CT3192GVE'
        capabilities['platformName'] = 'Android'
        capabilities['appPackage'] = 'com.experitest.ExperiBank'
        capabilities['appActivity'] = '.LoginActivity'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def phone_call_test(self):
        print('hello world')

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(CheckDeviceWiFiStateAndroid)