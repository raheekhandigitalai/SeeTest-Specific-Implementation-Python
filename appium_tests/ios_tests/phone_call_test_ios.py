import time
import unittest
import configparser

import helpers
import locators

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the iOS Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


class MakeAPhoneCall(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = 'Phone_Call_Test'
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '00008020-0005656621A2002E'
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = True  # If setting to False, disables report creation, may help to reduce execution time
        capabilities['bundleId'] = 'com.apple.mobilephone'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_wifi_connection(self):

        helpers.wait_for_element_to_be_clickable(self.driver, locators.ios_keypad_button)
        helpers.click_on_element(self.driver, locators.ios_keypad_button)

        phone_number = [3, 4, 7, 9, 3, 5, 6, 0, 0, 0]

        for number in phone_number:
            helpers.click_on_element(self.driver, "//XCUIElementTypeButton[@id='" + str(number) + "']")
            time.sleep(0.5)

        helpers.click_on_element(self.driver, locators.ios_call_button)

        helpers.wait_for_element_to_be_clickable(self.driver, locators.ios_calling_text)

        time.sleep(5)

        value = helpers.get_text_from_element(self.driver, locators.ios_call_status_text)
        print(value)

        if value == "Call Failed":
            helpers.seetest_logger(self.driver, "The Call Failed", "false")
            helpers.add_filter_tag_to_reporter(self.driver, "call_status", "failed")
        else:
            helpers.seetest_logger(self.driver, "The Call Is Successful", "true")
            helpers.add_filter_tag_to_reporter(self.driver, "call_status", "passed")

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(MakeAPhoneCall)
# runner.run(suite)
