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


def click_on_element(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()


def text_input_on_element(driver, xpath, text_input):
    driver.find_element(By.XPATH, xpath).send_keys(text_input)


# Function - Attempt to click on Element, if not found then Swipe and Attempt Click
def click_element_else_swipe_and_click(driver, xpath, start_offset):
    try:
        if driver.find_element(By.XPATH, xpath).is_displayed():
            driver.find_element(By.XPATH, xpath).click()
    except:
        driver.execute_script("seetest:client.swipeWhileNotFound(\"DOWN\"," + str(start_offset) +
                              ", 1000, \"NATIVE\", \"xpath=" + xpath + "\", 0, 1500, 2, true)")


# Function - Understand if Element is Displayed,  to help perform assertions
def is_displayed(driver, xpath):
    return driver.find_element(By.XPATH, xpath).is_displayed()


# method Name - client.deviceAction()
# Function - Allows us to perform actions you can physically do on a Mobile Device.
# Few examples: Home (Going to Home Page), Switch Orientation (Landscape / Portrait).
# https://docs.experitest.com/display/TE/DeviceAction
def device_action(driver, action):
    driver.execute_script("seetest:client.deviceAction(\"" + action + "\")")


# Method Name - client.launch()
# Function - Allows us to launch any iOS / Android Application mid-test execution.
def launch_app(driver, app_name):
    driver.execute_script("seetest:client.launch(\"" + app_name + "\", \"false\", \"false\")")


# Method Name - client.report()
# Function - Adds a step within the generated Video Report after Test Execution.
# The step adds a custom input comment and status (passed / failed) to
# mark a step within the test as a success or failure.
def seetest_logger(driver, message, status):
    driver.execute_script("seetest:client.report(\"" + message + "\", \"" + status + "\")")


# Method Name - client.addTestProperty()
# Function - Creates a custom filter set with a key value pair combination.
# Allows for easy Test Execution report viewing / generating by applying filters.
def add_filter_tag_to_reporter(driver, test_property, status):
    driver.execute_script("seetest:client.addTestProperty(\"" + test_property + "\",\"" + status + "\")")


def get_access_key():
    return config.get('seetest_authorization', 'access_key')


def get_cloud_url():
    return config.get('seetest_urls', 'cloud_url')


def get_android_udid():
    return config.get('device_information', 'android_udid')


def get_ios_udid():
    return config.get('device_information', 'ios_udid')
