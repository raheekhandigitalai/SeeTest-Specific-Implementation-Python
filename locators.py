# XPATHs stored under this file for re-usability and clean code in WiFiScript.py

# iOS Locators

ios_keypad_button = "//XCUIElementTypeButton[@id='Keypad']"
ios_call_button = "//XCUIElementTypeButton[@text='Call']"
ios_calling_text = "//XCUIElementTypeStaticText[contains(text(), 'calling')]"
ios_call_status_text = "(//XCUIElementTypeOther[@id='PHSingleCallParticipantLabelView']//*)[3]"

## Android Locators

# Phone Related Locators
android_call_button = "//*[@id='dialButton']"
android_call_state_text = "//*[@id='call_state_label']" # [@text='Calling…'] [@text='Call ended']
android_disconnect_button = "//*[@id='disconnect_button']"
android_call_time_text = "//*[@id='call_time']" # This appears if call is accepted

# Message Related Locators
android_compose_new_message_button = "//*[@contentDescription='Compose new message' and @id='fab']"
android_recipient_input = "//*[@id='recipients_editor_to']"
android_message_input = "//*[@id='message_edit_text']"
android_send_message_button = "//*[@contentDescription='Send']"
android_last_sent_message_text = "(//*[@id='content_text_view'])[last()]"
android_message_received_toast = "//*[@id='toast_text_layout']"
android_new_message_text = "//*[@id='new_message_body']"

# Settings Related Locators
android_connections_button = "//*[@id='title' and @text='Connections']"
android_mobile_networks_button = "//*[@id='title' and @text='Mobile networks']"
android_volte_calls_toggle = "//*[@id='title' and @text='VoLTE calls']//parent::*/following-sibling::*[@id='widget_frame']//*[@id='switch_widget']"
