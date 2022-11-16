**How to set up the environment**

Open a Terminal window in the project root folder, and type in the following commands:

```commandline
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

Above steps creates a local virtual environment where Python3, Pip3 and all relevant dependencies reside.

To run tests, use the following command:

```commandline
 ./env/bin/python3 -m unittest appium_script_ios.py
```

Changing the **.py** file reference would run relevant test case.