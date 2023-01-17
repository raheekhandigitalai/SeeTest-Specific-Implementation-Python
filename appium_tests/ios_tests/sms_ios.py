import time
import unittest
import configparser

from config import locators, helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the iOS Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


class SMSScenarios(unittest.TestCase):

    # currentResult = None  # Holds last result object passed to run method

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

        # Try / Catch checks whether main sms page appears, if not then perform appropriate steps
        try:
            if helpers.is_displayed(self.driver, locators.ios_header_in_sms_conversation):
                helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.ios_back_button)
        except:
            print('On main SMS Page. Continuing.')

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.ios_compose_new_message_button)

        helpers.text_input_on_element(self.driver, locators.ios_recipient_input, "3479356442")

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.ios_message_input)
        helpers.text_input_on_element(self.driver, locators.ios_message_input, text_to_send)

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.ios_send_message_button)

        time.sleep(10)

        value = helpers.get_text_from_element(self.driver, locators.ios_last_sent_message_text)

        try:
            if text_to_send in value.lower():
                helpers.seetest_logger(self.driver, "Message Sent Successfully", "true")
                helpers.add_filter_tag_to_reporter(self.driver, "message_status_send", "passed")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Message Not Sent", "false")
            helpers.add_filter_tag_to_reporter(self.driver, "message_status_send", "failed")

    def test_receive_a_message(self):
        text_to_receive = 'hello'

        helpers.device_action(self.driver, "Home")

        helpers.wait_for_element_to_be_clickable_custom_wait(self.driver, locators.ios_message_notification_popup, 30)
        helpers.click_on_element(self.driver, locators.ios_message_notification_popup)

        time.sleep(5)

        value = helpers.get_text_from_element(self.driver, "(//*[@XCElementType='XCUIElementTypeOther' and contains(text(), '" + text_to_receive + "')])[last()]")
        print(value.lower())
        print(text_to_receive)

        try:
            if text_to_receive in value.lower():
                helpers.seetest_logger(self.driver, "Message Received Successfully", "true")
                helpers.add_filter_tag_to_reporter(self.driver, "message_status_receive", "passed")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Message Not Received", "false")
            helpers.add_filter_tag_to_reporter(self.driver, "message_status_receive", "failed")

    def tearDown(self):
        # Ending the device reservation session
        helpers.handle_teardown(self, self.driver)
        self.driver.quit()
