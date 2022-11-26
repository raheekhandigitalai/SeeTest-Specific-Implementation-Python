# XPATHs stored under this file for re-usability and clean code in WiFiScript.py

# iOS Locators

ios_keypad_button = "//XCUIElementTypeButton[@id='Keypad']"
ios_call_button = "//XCUIElementTypeButton[@text='Call']"
ios_calling_text = "//XCUIElementTypeStaticText[contains(text(), 'calling')]"
ios_call_status_text = "(//XCUIElementTypeOther[@id='PHSingleCallParticipantLabelView']//*)[3]"

# Android Locators

android_call_state_text = "//*[@id='call_state_label']" # @text='Calling…'
android_disconnect_button = "//*[@id='disconnect_button']"
