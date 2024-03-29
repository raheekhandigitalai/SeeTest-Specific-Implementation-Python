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


class BoilerTemplateiOS(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_ios_udid()
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = False  # Disable report creation, will help to reduce execution time
        capabilities['app'] = 'cloud:com.experitest.ExperiBank'  # To install Application from the Cloud
        capabilities['bundleId'] = 'com.experitest.ExperiBank'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_scenario_01(self):
        self.driver.find_element(By.XPATH, "//*[@name='usernameTextField']").send_keys("company")
        self.driver.find_element(By.XPATH, "//*[@name='passwordTextField']").send_keys("company")
        self.driver.find_element(By.XPATH, "//*[@name='loginButton']").click()

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()
