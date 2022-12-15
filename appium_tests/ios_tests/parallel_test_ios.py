import unittest
import configparser
from concurrencytest import ConcurrentTestSuite, fork_for_tests

from config import helpers

from appium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

# config.properties reader
config = configparser.ConfigParser()
config.read('config.properties')

# Pre-defining the Android Capabilities as this Class is designed for iOS only
capabilities = DesiredCapabilities.IPHONE


def login_scenario(driver, username, password):
    driver.find_element_by_xpath("//*[@name='usernameTextField']").send_keys(username)
    driver.find_element_by_xpath("//*[@name='passwordTextField']").send_keys(password)
    driver.find_element_by_xpath("//*[@name='loginButton']").click()


class ParallelTestsiOS(unittest.TestCase):

    def setUp(self):
        # Capabilities for the session
        capabilities['testName'] = self._testMethodName
        capabilities['accessKey'] = '%s' % helpers.get_access_key()
        capabilities['platformName'] = 'iOS'
        capabilities['deviceQuery'] = "@os='ios' and @category='PHONE' and contains(@name, 'XR')"
        capabilities['generateReport'] = True  # Disable report creation, will help to reduce execution time
        capabilities['app'] = 'cloud:com.experitest.ExperiBank'
        capabilities['bundleId'] = 'com.experitest.ExperiBank'

        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                                       command_executor=helpers.get_cloud_url())

    def test_verify_app_launch(self):
        helpers.wait_for_element_to_be_clickable(self.driver, "//*[@name='usernameTextField']")

        value = helpers.get_text_from_element(self.driver, "//*[@name='usernameTextField']")

        try:
            if value == 'Username':
                helpers.seetest_logger(self.driver, "Successfully landed on the Login Page", "true")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Username Field does not have correct text", "false")

    def test_positive_scenario(self):
        login_scenario(self.driver, "company", "company")
        helpers.wait_for_element_to_be_clickable(self.driver, "//XCUIElementTypeStaticText[@id='Make Payment']")

        value = helpers.get_text_from_element(self.driver, "//XCUIElementTypeStaticText[@id='Make Payment']")

        try:
            if value == 'Make Payment':
                helpers.seetest_logger(self.driver, "Successfully landed on the Dashboard Page", "true")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Make Payment button does not have correct value", "false")

    def test_negative_scenario(self):
        login_scenario(self.driver, "incorrectuser", "incorrectpassword")
        helpers.wait_for_element_to_be_clickable(self.driver, "//XCUIElementTypeStaticText[contains(@id, 'Invalid')]")

        value = helpers.get_text_from_element(self.driver, "//XCUIElementTypeStaticText[contains(@id, 'Invalid')]")

        try:
            if value == 'Invalid username or password!':
                helpers.seetest_logger(self.driver, "Invalid Credentials Pop-up successfully appeared", "true")
        except NoSuchElementException:
            helpers.seetest_logger(self.driver, "Pop-up does not seem to have correct value", "false")

    def tearDown(self):
        # Ending the device reservation session
        self.driver.quit()


# Helps run the test using unittest framework
runner = unittest.TextTestRunner()
suite = unittest.TestLoader().loadTestsFromTestCase(ParallelTestsiOS)
concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(3))
runner.run(concurrent_suite)
