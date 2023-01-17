import threading
import phone_call_android
import phone_call_ios


# Define separate method to start Android Script for making a call
def run_phone_call_android_test():
    android_test = phone_call_android.PhoneCallMultiDeviceAndroid()
    try:
        android_test.setUp()
        android_test.test_make_phone_call()
        android_test.tearDown()
    except Exception as e:
        android_test.tearDown()
        raise Exception(e)


# Define a seperate method to start iOS Script for receiving a call
def run_phone_call_ios_test():
    ios_test = phone_call_ios.PhoneCallMultiDeviceiOS()
    try:
        ios_test.setUp()
        ios_test.receive_phone_call()
        ios_test.tearDown()
    except Exception as e:
        ios_test.tearDown()
        raise Exception(e)


# Create 2 threads to run both iOS & Android Script in parallel
# To run the script, run following command from the Terminal: python3 appium_tests/multi_device_phone_call.py
if __name__ == "__main__":
    threads = list()
    for index in range(2):
        thread_android = threading.Thread(target=run_phone_call_android_test, args=())
        thread_ios = threading.Thread(target=run_phone_call_ios_test, args=())

        threads.append(thread_android)
        threads.append(thread_ios)

        thread_android.start()
        thread_ios.start()

        for thread in enumerate(threads):
            thread.join()
