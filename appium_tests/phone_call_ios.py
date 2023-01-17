import unittest
import configparser

from config import helpers, locators
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

config = configparser.ConfigParser()
config.read('config.properties')

capabilities = {}


class PhoneCallMultiDeviceiOS(unittest.TestCase):

    def setUp(self):
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_ios_udid()
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def receive_phone_call(self):
        helpers.wait_for_element_to_be_clickable_custom_wait(self.driver, locators.ios_decline_call_button, 60)

        try:
            if helpers.is_displayed(self.driver, locators.ios_decline_call_button):
                helpers.logger("Call Received Successfully")
                helpers.click_on_element(self.driver, locators.ios_decline_call_button)
        except NoSuchElementException as e:
            helpers.logger("Call Not Received / Something went wrong.")
            helpers.logger(e)

    def tearDown(self):
        self.driver.quit()
