## How to set up the environment

Open a Terminal window in the project root folder, and type in the following commands:

```commandline
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

Above steps creates a local virtual environment where Python3, Pip3 and all relevant dependencies reside.

## Setting up the Tests

Let's review the changes needed to make sure tests can get started successfully:

Update **config.properties**:

1. Access Key: [Obtaining your Access Key](https://docs.experitest.com/display/TET/Obtaining+Access+Key)
2. Target Cloud URL where the tests will run
3. Device UDIDs to specify which devices the tests should run on, an easy way to find device UDID:

![img.png](images/devices_page_list_view.png)

## Running Tests

To run all tests from a single Class, use the following command (_replace the **.py** file reference to run relevant tests_):

```commandline
./env/bin/python3 -m unittest appium_tests.ios_tests.boiler_template_ios.BoilerTemplateiOS
```

There are number of ways to trigger tests depending on what you want to achieve. Here is an example if you want to run a specific Test Case from a Class:

```commandline
./env/bin/python3 -m unittest appium_tests.ios_tests.sms_ios.SMSScenarios.test_send_a_message
```

For further explanation, unittest library can be explored from Python's official documentation:

https://docs.python.org/3/library/unittest.html

## Additional References

[Capabilities in Appium Based Tests](https://docs.experitest.com/display/TE/Capabilties+in+Appium+Based+Tests)

