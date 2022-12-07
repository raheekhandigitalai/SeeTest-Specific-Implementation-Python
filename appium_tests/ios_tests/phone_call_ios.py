import time
import unittest
import configparser

import helpers
import locators

from appium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the iOS Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


class PhoneCallScenarios(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_ios_udid()
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = True  # If setting to False, disables report creation, may help to reduce execution time
        capabilities['bundleId'] = 'com.apple.mobilephone'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_make_a_phone_call(self):
        helpers.wait_for_element_to_be_clickable(self.driver, locators.ios_keypad_button)
        helpers.click_on_element(self.driver, locators.ios_keypad_button)

        phone_number = [3, 4, 7, 9, 3, 5, 6, 4, 4, 2]

        for number in phone_number:
            helpers.click_on_element(self.driver, "//XCUIElementTypeButton[@id='" + str(number) + "']")
            time.sleep(0.5)

        helpers.click_on_element(self.driver, locators.ios_call_button)

        helpers.wait_for_element_to_be_clickable(self.driver, locators.ios_calling_text)

        time.sleep(5)

        value = helpers.get_text_from_element(self.driver, locators.ios_call_status_text)
        print(value)

        time.sleep(5)

        try:
            if value == "calling…":
                helpers.seetest_logger(self.driver, "Attempting to make a call with status: 'Calling…'", "true")
                helpers.click_on_element(self.driver, locators.ios_end_call_button)
                helpers.seetest_logger(self.driver, "The Call Is Successful", "true")
                helpers.add_filter_tag_to_reporter(self.driver, "call_status_request", "passed")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Could not make a call, status: " + value, "false")
            helpers.add_filter_tag_to_reporter(self.driver, "call_status_request", "failed")

    # This Test Case will work assuming there is an incoming call
    def test_receive_a_phone_call(self):

        helpers.wait_for_element_to_be_clickable_custom_wait(self.driver, locators.ios_decline_call_button, 30)

        try:
            if helpers.is_displayed(self.driver, locators.ios_decline_call_button):
                helpers.seetest_logger(self.driver, "Call Received Successfully", "true")
                helpers.click_on_element(self.driver, locators.ios_decline_call_button)
                helpers.add_filter_tag_to_reporter(self.driver, "call_status_receive", "passed")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Call Not Received", "false")
            helpers.add_filter_tag_to_reporter(self.driver, "call_status_receive", "failed")

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(PhoneCallScenarios)
