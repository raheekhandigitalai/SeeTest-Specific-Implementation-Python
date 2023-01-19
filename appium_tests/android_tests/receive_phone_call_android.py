import time
import unittest
import configparser

from config import helpers, locators
from appium import webdriver

from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

config = configparser.ConfigParser()
config.read('config.properties')

capabilities = {}


class ReceivePhoneCallAndroid(unittest.TestCase):

    def setUp(self):
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '%s' % helpers.get_android_udid()
        capabilities['platformName'] = 'Android'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_receive_phone_call_with_swipe(self):
        helpers.wait_for_element_to_be_clickable_custom_wait(self.driver, "//*[@id='accept_button_in_2_way']/*/*[1]", 60)

        accept_button = self.driver.find_element(By.XPATH, "//*[@id='accept_button_in_2_way']/*/*[1]")
        accept_button_location_x = accept_button.location.get('x')
        accept_button_location_y = accept_button.location.get('y')

        element_above_accept = self.driver.find_element(By.XPATH, "//*[@id='caller_info_card_area']")
        element_above_accept_location_x = element_above_accept.location.get('x')
        element_above_accept_location_y = element_above_accept.location.get('y')

        touch = TouchAction(self.driver)

        touch.long_press(x=accept_button_location_x, y=accept_button_location_y).move_to(
            x=element_above_accept_location_x, y=element_above_accept_location_y).perform().release()

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
