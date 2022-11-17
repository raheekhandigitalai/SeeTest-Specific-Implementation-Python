import time
import unittest
import configparser

import helpers
import locators

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the iOS Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


class SendSMSTest(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = 'SMS_Test'
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '00008020-0005656621A2002E'
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = True  # If setting to False, disables report creation, may help to reduce execution time
        capabilities['bundleId'] = 'com.apple.MobileSMS'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_wifi_connection(self):

        try:
            if helpers.is_displayed(self.driver, "//*[@id='CKChat']"):
                helpers.wait_for_element_to_be_clickable_and_click(self.driver, "(//*[@XCElementType='XCUIElementTypeButton'])[1]")
        except:
            print('On main SMS Page')

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, "//*[@id='composeButton']")

        helpers.text_input_on_element(self.driver, "//XCUIElementTypeTextField[@id='To:']", "3479356000")

        helpers.click_on_element(self.driver, "//XCUIElementTypeTextField[@id='messageBodyField']")
        helpers.text_input_on_element(self.driver, "//XCUIElementTypeTextField[@id='messageBodyField']", "Hello World")
        helpers.click_on_element(self.driver, "//XCUIElementTypeButton[@id='sendButton']")

        time.sleep(5)

        if helpers.is_displayed(self.driver, "(//XCUIElementTypeStaticText[contains(text(), 'Not Delivered')])[1]"):
            helpers.seetest_logger(self.driver, "Message Delivery Failed", "false")
            helpers.add_filter_tag_to_reporter(self.driver, "message_status", "failed")
        else:
            helpers.seetest_logger(self.driver, "Message Delivery Is Successful", "true")
            helpers.add_filter_tag_to_reporter(self.driver, "message_status", "passed")

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(SendSMSTest)
# runner.run(suite)
