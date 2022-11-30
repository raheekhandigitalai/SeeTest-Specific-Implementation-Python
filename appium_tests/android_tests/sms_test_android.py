import time
import unittest
import configparser

import helpers
import locators
from helpers import logger

from appium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for Android only
capabilities = DesiredCapabilities.ANDROID


class SMSScenarios(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = 'Android_Test_Python'
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '9887e8343439443447'
        capabilities['platformName'] = 'Android'
        capabilities['appPackage'] = 'com.samsung.android.messaging'
        capabilities['appActivity'] = '.ui.view.main.WithActivity'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    # def test_send_a_message(self):
    #
    #     time.sleep(5)
    #
    #     text_to_send = 'hello'
    #
    #     helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.android_compose_new_message_button)
    #     helpers.wait_for_element_to_be_clickable(self.driver, locators.android_recipient_input)
    #     helpers.text_input_on_element(self.driver, locators.android_recipient_input, "3479356442")
    #     helpers.text_input_on_element(self.driver, locators.android_message_input, text_to_send)
    #     helpers.click_on_element(self.driver, locators.android_send_message_button)
    #
    #     time.sleep(5)
    #
    #     value = helpers.get_text_from_element(self.driver, locators.android_last_sent_message_text)
    #     print(value)
    #
    #     try:
    #         if value == text_to_send:
    #             helpers.seetest_logger(self.driver, "Message Sent Successfully", "true")
    #             helpers.add_filter_tag_to_reporter(self.driver, "message_status_send", "passed")
    #     except:
    #         helpers.seetest_logger(self.driver, "Message Not Sent", "false")
    #         helpers.add_filter_tag_to_reporter(self.driver, "message_status_send", "failed")

    def test_receive_a_message(self):

        text_to_receive = 'hello'

        helpers.wait_for_element_to_be_clickable_and_click(self.driver, locators.android_message_received_toast)

        time.sleep(5)

        value = helpers.get_text_from_element(self.driver, locators.android_new_message_text)
        print(value)

        try:
            if value == text_to_receive:
                helpers.seetest_logger(self.driver, "Message Received Successfully", "true")
                helpers.add_filter_tag_to_reporter(self.driver, "message_status_receive", "passed")
        except:
            helpers.seetest_logger(self.driver, "Message Not Received", "false")
            helpers.add_filter_tag_to_reporter(self.driver, "message_status_receive", "failed")

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(SMSScenarios)
