# XPATHs stored under this file for re-usability and clean code in WiFiScript.py

# iOS Locators

ios_keypad_button = "//XCUIElementTypeButton[@id='Keypad']"
ios_call_button = "//XCUIElementTypeButton[@text='Call']"
ios_calling_text = "//XCUIElementTypeStaticText[contains(text(), 'calling')]"
ios_call_status_text = "(//XCUIElementTypeOther[@id='PHSingleCallParticipantLabelView']//*)[3]"

# Android Locators

android_call_state_text = "//*[@id='call_state_label']" # @text='Calling…'
android_disconnect_button = "//*[@id='disconnect_button']"

android_compose_new_message_button = "//*[@contentDescription='Compose new message' and @id='fab']"
android_recipient_input = "//*[@id='recipients_editor_to']"
android_message_input = "//*[@id='message_edit_text']"
android_send_message_button = "//*[@contentDescription='Send']"
android_last_sent_message_text = "(//*[@id='content_text_view'])[last()]"
android_message_received_toast = "//*[@id='toast_text_layout']"
android_new_message_text = "//*[@id='new_message_body']"
