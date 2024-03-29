import unittest
import configparser

from config import helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for Android only
capabilities = DesiredCapabilities.ANDROID


class ADBCommandAndroid(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_android_udid()
        capabilities['platformName'] = 'Android'
        capabilities['generateReport'] = helpers.get_generate_report()

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_adb_command(self):
        print(helpers.run_adb(self.driver, "adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'"))

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()
