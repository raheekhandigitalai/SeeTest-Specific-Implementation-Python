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
from selenium.webdriver.support import expected_conditions as EC

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


class CheckDeviceWiFiStateiOS(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = 'iOS_Test_Python'
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['udid'] = '00008020-0005656621A2002E'
        capabilities['platformName'] = 'iOS'
        capabilities['autoDismissAlerts'] = True  # This helps to handle unexpected native pop-ups
        capabilities['generateReport'] = True  # If setting to False, disables report creation, may help to reduce execution time
        capabilities['bundleId'] = 'com.apple.mobilephone'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_wifi_connection(self):

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//XCUIElementTypeButton[@id='Keypad']")))
        self.driver.find_element(By.XPATH, "//XCUIElementTypeButton[@id='Keypad']").click()

        phone_number = [3, 4, 7, 9, 3, 5, 6, 0, 0, 0]

        for number in phone_number:
            self.driver.find_element(By.XPATH, "//XCUIElementTypeButton[@id='" + str(number) + "']").click()
            time.sleep(0.5)

        self.driver.find_element(By.XPATH, "//XCUIElementTypeButton[@text='Call']").click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//XCUIElementTypeStaticText[contains(text(), 'calling')]")))

        time.sleep(5)

        value = self.driver.find_element(By.XPATH, "(//XCUIElementTypeOther[@id='PHSingleCallParticipantLabelView']//*)[3]").text
        print(value)

        if value == "Call Failed":
            self.driver.execute_script("seetest:client.report(\"The Call Failed\", \"false\")")
            self.driver.execute_script("seetest:client.addTestProperty(\"call_status\",\"failed\")")
        else:
            self.driver.execute_script("seetest:client.report(\"The Call Is Successful\", \"true\")")
            self.driver.execute_script("seetest:client.addTestProperty(\"call_status\",\"passed\")")

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(CheckDeviceWiFiStateiOS)
# runner.run(suite)
