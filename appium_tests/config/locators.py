import os
import sys

sys.path.append(os.path.dirname(__file__))

# XPATHs stored under this file for re-usability and clean code

#############################################

## iOS Locators

# Phone Related Locators
ios_keypad_button = "//XCUIElementTypeButton[@id='Keypad']"
ios_call_button = "//XCUIElementTypeButton[@text='Call']"
ios_calling_text = "//XCUIElementTypeStaticText[contains(text(), 'calling')]"
ios_call_status_text = "(//XCUIElementTypeOther[@id='PHSingleCallParticipantLabelView']//*)[3]"
ios_end_call_button = "//*[@id='End call']"
ios_accept_call_button = "//XCUIElementTypeButton[@id='Accept' and @text='Answer call']"
ios_decline_call_button = "//XCUIElementTypeButton[@id='Decline']"
ios_incoming_call_notification = "//*[@id='Incoming call']"

# Message Related Locators

ios_header_in_sms_conversation = "//*[@id='CKChat']"
ios_back_button = "(//*[@XCElementType='XCUIElementTypeButton'])[1]"
ios_compose_new_message_button = "//*[@id='composeButton']"
ios_recipient_input = "//XCUIElementTypeTextField[@id='To:']"
ios_message_input = "//XCUIElementTypeTextField[@id='messageBodyField']"
ios_send_message_button = "//XCUIElementTypeButton[@id='sendButton']"
ios_last_sent_message_text = "(//*[@class='UIAView' and contains(@id, 'Your Text Message')])[last()]"
ios_message_notification_popup = "//*[@accessibilityLabel='NotificationShortLookView']"

# Device Settings Related Locators

ios_cellular_button = "//XCUIElementTypeCell[@id='Cellular']"
ios_cellular_plans_primary_button = "//*[@accessibilityLabel='CELLULAR PLANS']/following-sibling::*[1]"
ios_voice_and_data_button = "//XCUIElementTypeCell[@id='Voice & Data']"
ios_selected_voice_and_data_option = "//*[@id='checkmark']//parent::XCUIElementTypeCell"
ios_4g_option = "//XCUIElementTypeCell[@id='4G']"
ios_lte_option = "//XCUIElementTypeCell[@id='LTE']"

#############################################

## Android Locators

# Phone Related Locators
android_keypad_button = "//*[@id='tab_text_view' and @text='Keypad']"
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

# Device Settings Related Locators
android_connections_button = "//*[@id='title' and @text='Connections']"
android_mobile_networks_button = "//*[@id='title' and @text='Mobile networks']"
android_volte_calls_toggle = "//*[@id='title' and @text='VoLTE calls']//parent::*/following-sibling::*[@id='widget_frame']//*[@id='switch_widget']"
