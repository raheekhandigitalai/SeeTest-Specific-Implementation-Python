import configparser

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser()
config.read('config.properties')


def logger(message):
    print(message)


# Function - Waiting on element to be clickable
def wait_for_element_to_be_clickable(driver, xpath):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))


# Function - Waiting on element to be clickable with custom wait
def wait_for_element_to_be_clickable_custom_wait(driver, xpath, time_to_wait):
    WebDriverWait(driver, time_to_wait, poll_frequency=0.3).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))


# Function - Waiting on element to be clickable and click if found
def wait_for_element_to_be_clickable_and_click(driver, xpath):
    wait_for_element_to_be_clickable(driver, xpath)
    driver.find_element(By.XPATH, xpath).click()


# Function - Get Text from current element to help perform assertions
def get_text_from_element(driver, xpath):
    value = driver.find_element(By.XPATH, xpath).text
    return value


# Function - Get all elements with the same XPATH in a list format
def find_elements(driver, xpath):
    items = driver.find_elements(By.XPATH, xpath)
    return items


# Function - Click on the Element specified
def click_on_element(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()


# Function - Send Text Input to the Element specified
def text_input_on_element(driver, xpath, text_input):
    driver.find_element(By.XPATH, xpath).send_keys(text_input)


# Function - Understand if Element is Displayed,  to help perform assertions
def is_displayed(driver, xpath):
    return driver.find_element(By.XPATH, xpath).is_displayed()


# Function - Attempt to click on Element, if not found then Swipe and Attempt Click
# https://docs.experitest.com/display/TE/SwipeWhileNotFound
def click_element_else_swipe_and_click(driver, xpath, start_offset):
    try:
        if driver.find_element(By.XPATH, xpath).is_displayed():
            driver.find_element(By.XPATH, xpath).click()
    except:
        driver.execute_script("seetest:client.swipeWhileNotFound(\"DOWN\"," + str(start_offset) +
                              ", 1000, \"NATIVE\", \"xpath=" + xpath + "\", 0, 1500, 2, true)")


# Method Name - client.run()
# Function - Allows us to run ADB commands directly on Android Devices
def run_adb(driver, adb_prompt):
    return driver.execute_script("seetest:client.run(\"" + adb_prompt + "\")")


# Method Name - client.deviceAction()
# Function - Allows us to perform actions you can physically do on a Mobile Device.
# Few examples: Home (Going to Home Page), Switch Orientation (Landscape / Portrait).
# https://docs.experitest.com/display/TE/DeviceAction
def device_action(driver, action):
    driver.execute_script("seetest:client.deviceAction(\"" + action + "\")")


# Method Name - client.launch()
# Function - Allows us to launch any iOS / Android Application mid-test execution.
# https://docs.experitest.com/display/TE/Launch
def launch_app(driver, app_name):
    driver.execute_script("seetest:client.launch(\"" + app_name + "\", \"false\", \"false\")")


# Method Name - client.report()
# Function - Adds a step within the generated Video Report after Test Execution.
# The step adds a custom input comment and status (passed / failed) to
# mark a step within the test as a success or failure.
# https://docs.experitest.com/display/TE/Report
def seetest_logger(driver, message, status):
    driver.execute_script("seetest:client.report(\"" + message + "\", \"" + status + "\")")


# Method Name - client.addTestProperty()
# Function - Creates a custom filter set with a key value pair combination.
# Allows for easy Test Execution report viewing / generating by applying filters.
# https://docs.experitest.com/display/TE/AddTestProperty
def add_filter_tag_to_reporter(driver, test_property, status):
    driver.execute_script("seetest:client.addTestProperty(\"" + test_property + "\",\"" + status + "\")")


# Method Name - client.setReportStatus
# Function - Allows us to change the final Test Report status.
# First Parameter Values Accepted - Passed, Failed, Skipped
# Second Parameter Value Accepted - Any String to convey a message output
#
def set_report_status(driver, status, message):
    driver.execute_script("seetest:client.setReportStatus(\"" + status + "\",\"" + message + "\")")


# Function - Sometimes the test itself passed but may have steps that are marked as
# failed. A common example is using WebDriverWait, when waiting on element, and if
# element is not found right away, the first steps are marked as failed.
# To make sure appropriate Test Results are generated, this method has been re-used.
# Reference - https://gist.github.com/hynekcer/1b0a260ef72dae05fe9611904d7b9675
def handle_teardown(self, driver):
    if hasattr(self._outcome, 'errors'):
        # Python 3.4 - 3.10  (These two methods have no side effects)
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
    else:
        # Python 3.11+
        result = self._outcome.result
    ok = all(test != self for test, text in result.errors + result.failures)

    # Demo output:  (print short info immediately - not important)
    if ok:
        print('\nOK: %s' % (self.id(),))
        # self.driver.execute_script("seetest:client.setReportStatus(\"Passed\",\"Test Passed\")")
        set_report_status(driver, "Passed", "Test Passed")
    for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
        for test, text in errors:
            if test is self:
                # the full traceback is in the variable `text`
                msg = [x for x in text.split('\n')[1:]
                       if not x.startswith(' ')][0]
                print("\n\n%s: %s\n     %s" % (typ, self.id(), msg))


def get_access_key():
    return config.get('seetest_authorization', 'access_key')


def get_cloud_url():
    return config.get('seetest_urls', 'cloud_url')


def get_android_udid():
    return config.get('device_information', 'android_udid')


def get_ios_udid():
    return config.get('device_information', 'ios_udid')


def get_generate_report():
    return config.get('reporting', 'generate_report')
