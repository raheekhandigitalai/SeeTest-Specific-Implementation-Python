import logging
import threading
import appium_script_ios
import appium_script_android
import helpers


def start_appium_script_ios():
    # Instantiating the Appium Script Class
    appium_session_ios = appium_script_ios.CheckDeviceWiFiStateiOS()

    try:
        # Setting up Appium Session
        appium_session_ios.setUp()
        # Running the Appium Script itself
        appium_session_ios.test_wifi_connection()
        # Tearing down the Appium Session once done
        appium_session_ios.tearDown()
    except Exception as e:
        # If Script fails for some reason, making sure Appium Session still ends and doesn't leave sessions hanging
        appium_session_ios.tearDown()
        raise Exception(e)


def start_appium_script_android():
    # Instantiating the Appium Script Class
    appium_session_android = appium_script_android.CheckDeviceWiFiStateAndroid()

    try:
        # Setting up Appium Session
        appium_session_android.setUp()
        # Running the Appium Script itself
        appium_session_android.test_wifi_connection()
        # Tearing down the Appium Session once done
        appium_session_android.tearDown()
    except Exception as e:
        # If Script fails for some reason, making sure Appium Session still ends and doesn't leave sessions hanging
        appium_session_android.tearDown()
        raise Exception(e)


if __name__ == "__main__":
    start_appium_script_ios()
