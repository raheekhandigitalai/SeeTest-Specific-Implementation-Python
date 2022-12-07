## How to set up the environment

Open a Terminal window in the project root folder, and type in the following commands:

```commandline
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

Above steps creates a local virtual environment where Python3, Pip3 and all relevant dependencies reside.

## Running Tests

To run all tests from a single Class, use the following command (_replace the **.py** file reference to run relevant tests_):

```commandline
./env/bin/python3 -m unittest appium_tests/ios_tests/appium_script_ios.py
```

There are number of ways to trigger tests depending on what you want to achieve. Here is an example if you want to run a specific Test Case from a Class:

```commandline
./env/bin/python3 -m unittest appium_tests.android_tests.sms_test_android.SMSScenarios.test_receive_a_message
```

For further explanation, unittest library can be explored from Python's official documentation:

https://docs.python.org/3/library/unittest.html