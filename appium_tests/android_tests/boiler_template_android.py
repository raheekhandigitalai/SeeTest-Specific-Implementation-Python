import unittest
import configparser

from config import helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for Android only
capabilities = DesiredCapabilities.ANDROID


class BoilerTemplateAndroid(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_android_udid()
        capabilities['platformName'] = 'Android'
        capabilities['generateReport'] = True  # If setting to False, disables report creation, may help to reduce execution time
        capabilities['app'] = 'cloud:com.experitest.ExperiBank/.LoginActivity'
        capabilities['appPackage'] = 'com.experitest.ExperiBank'
        capabilities['appActivity'] = '.LoginActivity'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_scenario_01(self):
        self.driver.find_element(By.ID, "com.experitest.ExperiBank:id/usernameTextField").send_keys("company")
        self.driver.find_element(By.ID, "com.experitest.ExperiBank:id/passwordTextField").send_keys("company")
        self.driver.find_element(By.ID, "com.experitest.ExperiBank:id/loginButton").click()

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()
