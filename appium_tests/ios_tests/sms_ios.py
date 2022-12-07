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


class SMSScenarios(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_ios_udid()
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = True  # If setting to False, disables report creation, may help to reduce execution time
        capabilities['bundleId'] = 'com.apple.MobileSMS'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_send_a_message(self):
        text_to_send = 'hello'

        try:
            if helpers.is_displayed(self.driver, "//*[@id='CKChat']"):
                helpers.wait_for_element_to_be_clickable_and_click(self.driver, "(//*[@XCElementType='XCUIElementTypeButton'])[1]")
        except:
            print('On main SMS Page')

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, "//*[@id='composeButton']")

        helpers.text_input_on_element(self.driver, "//XCUIElementTypeTextField[@id='To:']", "3479356442")

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, "//XCUIElementTypeTextField[@id='messageBodyField']")
        helpers.text_input_on_element(self.driver, "//XCUIElementTypeTextField[@id='messageBodyField']", "Hello")

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, "//XCUIElementTypeButton[@id='sendButton']")

        time.sleep(10)

        value = helpers.get_text_from_element(self.driver, "(//*[@class='UIAView' and contains(@id, 'Your Text Message')])[last()]")
        print(value.lower())
        print(text_to_send)

        try:
            if text_to_send in value:
                helpers.seetest_logger(self.driver, "Message Sent Successfully", "true")
                helpers.add_filter_tag_to_reporter(self.driver, "message_status_send", "passed")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Message Not Sent", "false")
            helpers.add_filter_tag_to_reporter(self.driver, "message_status_send", "failed")

    def test_receive_a_message(self):
        print('hello') # message_status_receive

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(SMSScenarios)
