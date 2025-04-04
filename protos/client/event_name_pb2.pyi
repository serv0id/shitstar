from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EventNameNative(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_NAME_UNSPECIFIED: _ClassVar[EventNameNative]
    EVENT_NAME_APP_OPENED: _ClassVar[EventNameNative]
    EVENT_NAME_APP_CLOSED: _ClassVar[EventNameNative]
    EVENT_NAME_HEARTBEAT: _ClassVar[EventNameNative]
    EVENT_NAME_REPORTED_ISSUE: _ClassVar[EventNameNative]
    EVENT_NAME_MILESTONE_CLICKED: _ClassVar[EventNameNative]
    EVENT_NAME_STARTED_VIDEO: _ClassVar[EventNameNative]
    EVENT_NAME_WATCHED_VIDEO: _ClassVar[EventNameNative]
    EVENT_NAME_FAILED_VIDEO: _ClassVar[EventNameNative]
    EVENT_NAME_FAILED_RETRY_VIDEO: _ClassVar[EventNameNative]
    EVENT_NAME_SKIPPED_VIDEO: _ClassVar[EventNameNative]
    EVENT_NAME_ADD_TO_WATCHLIST: _ClassVar[EventNameNative]
    EVENT_NAME_REMOVED_FROM_WATCHLIST: _ClassVar[EventNameNative]
    EVENT_NAME_NOTIFICATION_CLICKED: _ClassVar[EventNameNative]
    EVENT_NAME_NOTIFICATION_RECEIVED: _ClassVar[EventNameNative]
    EVENT_NAME_GET_INSTALLED_APPS: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_CAPTION_SETTING: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_LANGUAGE: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_STREAM_QUALITY: _ClassVar[EventNameNative]
    EVENT_NAME_FAILED_PLAYBACK_API: _ClassVar[EventNameNative]
    EVENT_NAME_SUBMITTED_PARENTAL_PIN: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGED_NOTIFICATION_PERMISSION: _ClassVar[EventNameNative]
    EVENT_NAME_PAGE_LOADED: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_PAGE_PAYMENT: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_INITIATED: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_FAILED: _ClassVar[EventNameNative]
    EVENT_NAME_PURCHASED_SUBSCRIPTION: _ClassVar[EventNameNative]
    EVENT_NAME_ERASED_SEARCH: _ClassVar[EventNameNative]
    EVENT_NAME_EXIT_SEARCH: _ClassVar[EventNameNative]
    EVENT_NAME_QUERIED_SEARCH: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_SEARCH_PAGE: _ClassVar[EventNameNative]
    EVENT_NAME_APP_STARTUP_TIME: _ClassVar[EventNameNative]
    EVENT_NAME_AD_REQUESTED: _ClassVar[EventNameNative]
    EVENT_NAME_AD_RECEIVED: _ClassVar[EventNameNative]
    EVENT_NAME_AD_LOAD_ERROR: _ClassVar[EventNameNative]
    EVENT_NAME_AD_PLAY_ERROR: _ClassVar[EventNameNative]
    EVENT_NAME_MISSED_TRANSLATION: _ClassVar[EventNameNative]
    EVENT_NAME_FAILED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_STARTED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_COMPLETED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_PAUSED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_RESUMED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_DELETED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_STOPPED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_WATCH_ATTEMPT: _ClassVar[EventNameNative]
    EVENT_NAME_LOGGED_OUT: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_AD_FREE_NUDGE: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_AD_FREE_NUDGE: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_LANGUAGE_POPUP: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_LANGUAGE_POPUP: _ClassVar[EventNameNative]
    EVENT_NAME_PRELOADED_ARTWORK: _ClassVar[EventNameNative]
    EVENT_NAME_MILESTONE_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_WATCH_PAGE: _ClassVar[EventNameNative]
    EVENT_NAME_PAGE_LOAD_FAILED: _ClassVar[EventNameNative]
    EVENT_NAME_WIDGET_LOAD_FAILED: _ClassVar[EventNameNative]
    EVENT_NAME_BUG_REPORT: _ClassVar[EventNameNative]
    EVENT_NAME_SETTINGS_OPTION_NUDGE_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_SETTINGS_OPTION_NUDGE_CLICKED: _ClassVar[EventNameNative]
    EVENT_NAME_APPLIED_SEARCH_FILTER: _ClassVar[EventNameNative]
    EVENT_NAME_TAPPED_SEARCH: _ClassVar[EventNameNative]
    EVENT_NAME_HELP_ITEM_CLICKED: _ClassVar[EventNameNative]
    EVENT_NAME_HELP_SEARCHED: _ClassVar[EventNameNative]
    EVENT_NAME_HELP_PAGE_VISITED: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_PAYMENT_METHODS: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_PAYMENT_STATUS: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_X_INITIATED: _ClassVar[EventNameNative]
    EVENT_NAME_AD_ERROR: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_X_REQUEST: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_X_RESPONSE: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_X_ERROR: _ClassVar[EventNameNative]
    EVENT_NAME_ONBOARDING_VIDEO_STARTED: _ClassVar[EventNameNative]
    EVENT_NAME_ONBOARDING_VIDEO_FAILED: _ClassVar[EventNameNative]
    EVENT_NAME_ONBOARDING_VIDEO_BUFFERED: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_UPGRADE_NUDGE: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_UPGRADE_NUDGE: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_ERROR_SCREEN_ITEM: _ClassVar[EventNameNative]
    EVENT_NAME_EXITED_ERROR_SCREEN: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_VOTING_BUTTON: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_VOTING_BUTTON: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_VOTING_PAGE: _ClassVar[EventNameNative]
    EVENT_NAME_QUIT_VOTING_PAGE: _ClassVar[EventNameNative]
    EVENT_NAME_FAILED_VOTING: _ClassVar[EventNameNative]
    EVENT_NAME_DOWNLOADS_MIGRATED: _ClassVar[EventNameNative]
    EVENT_NAME_IMPRESSED_SEARCH: _ClassVar[EventNameNative]
    EVENT_NAME_PROTO_TEST_MINERVA: _ClassVar[EventNameNative]
    EVENT_NAME_PROTO_TEST_MINERVA2: _ClassVar[EventNameNative]
    EVENT_NAME_WATCH_TAB_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_CARD_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_WATCH_TAB_INTERACTED: _ClassVar[EventNameNative]
    EVENT_NAME_HELP_AND_SETTINGS_WIDGET_CLICKED: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_HELP_AND_SETTINGS_WIDGET: _ClassVar[EventNameNative]
    EVENT_NAME_CARD_CLICKED: _ClassVar[EventNameNative]
    EVENT_NAME_INAPP_RATING_TRIGGERED: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_NEXT_CONTENT: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_PLAYBACK_SPEED: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_PLAYER_ORIENTATION: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_VOLUME: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_BRIGHTNESS: _ClassVar[EventNameNative]
    EVENT_NAME_CHANGE_FILL_STATUS: _ClassVar[EventNameNative]
    EVENT_NAME_STARTED_GESTURE_ONBOARDING: _ClassVar[EventNameNative]
    EVENT_NAME_COMPLETED_GESTURE_ONBOARDING: _ClassVar[EventNameNative]
    EVENT_NAME_SUBSCRIBED_UPCOMING_CONTENT: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_SPLASH_PAGE: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_ERROR_PAGE: _ClassVar[EventNameNative]
    EVENT_NAME_SEARCH_HISTORY: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_CAST_BUTTON: _ClassVar[EventNameNative]
    EVENT_NAME_FAILED_CAST_ATTEMPT: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_CASTING_DEVICE_LIST: _ClassVar[EventNameNative]
    EVENT_NAME_SELECTED_CASTING_DEVICE: _ClassVar[EventNameNative]
    EVENT_NAME_RECEIVED_CASTING_CONNECTION_STATUS: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_CAST_CONTROL_WINDOW: _ClassVar[EventNameNative]
    EVENT_NAME_MINIMISED_CAST_CONTROL: _ClassVar[EventNameNative]
    EVENT_NAME_DISCONNECTED_CASTING: _ClassVar[EventNameNative]
    EVENT_NAME_RECAPTCHA_ERROR: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_ENGAGEMENT_WIDGET: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_ENGAGEMENT_TAB: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_PLAY_NOW: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_SECTION: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_HINT: _ClassVar[EventNameNative]
    EVENT_NAME_ENGAGED_SECTION: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_SECTION_RESULT: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_ENGAGEMENT_RESULT: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_PAGE_LOAD_ERROR: _ClassVar[EventNameNative]
    EVENT_NAME_ADS_RESOLVED: _ClassVar[EventNameNative]
    EVENT_NAME_WATCH_PRELOAD: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_PAYMENT: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_REDEEM: _ClassVar[EventNameNative]
    EVENT_NAME_REDEEM_COUPON_EVENT: _ClassVar[EventNameNative]
    EVENT_NAME_REDEEM_USER_CONFIRMATION_EVENT: _ClassVar[EventNameNative]
    EVENT_NAME_TOKEN_MISMATCHED: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_PAYMENT_HISTORY: _ClassVar[EventNameNative]
    EVENT_NAME_PIN_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_PIN_CLICKED: _ClassVar[EventNameNative]
    EVENT_NAME_VERIFIED_SNA_EVURL: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_REDEEM_COUPON: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_REDEEM_USER_CONFIRMATION_WIDGET: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_SHARE_ENGAGEMENT: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_CLAIM_REWARD: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_INFO_BUTTON: _ClassVar[EventNameNative]
    EVENT_NAME_PAYMENT_METHOD_ACTION: _ClassVar[EventNameNative]
    EVENT_NAME_VIEWED_PERMISSION_DIALOG: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_PERMISSION_DIALOG: _ClassVar[EventNameNative]
    EVENT_NAME_UPDATED_APP_LANGUAGE: _ClassVar[EventNameNative]
    EVENT_NAME_USP_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_SGAI_STITCH: _ClassVar[EventNameNative]
    EVENT_NAME_SGAI_ERROR: _ClassVar[EventNameNative]
    EVENT_NAME_PAGE_CONTENT_LOADED: _ClassVar[EventNameNative]
    EVENT_NAME_FROZEN_FRAME: _ClassVar[EventNameNative]
    EVENT_NAME_USER_INTERACTION_IN_PAUSE: _ClassVar[EventNameNative]
    EVENT_NAME_SUBMITTED_COMMENT: _ClassVar[EventNameNative]
    EVENT_NAME_CLICKED_MAXVIEW_MODE_SWITCHER: _ClassVar[EventNameNative]
    EVENT_NAME_PRELOAD_JOURNEY: _ClassVar[EventNameNative]
    EVENT_NAME_CACHE_WRITE: _ClassVar[EventNameNative]
    EVENT_NAME_CACHE_HIT: _ClassVar[EventNameNative]
    EVENT_NAME_CACHE_DELETE: _ClassVar[EventNameNative]
    EVENT_NAME_CACHE_CLEAR: _ClassVar[EventNameNative]
    EVENT_NAME_EVICTED_CONTENT_RATING_CARD: _ClassVar[EventNameNative]
    EVENT_NAME_SURVEY_WIDGET_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_SUBMITTED_SURVEY: _ClassVar[EventNameNative]
    EVENT_NAME_QUEUED_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_START_API_PREFETCH: _ClassVar[EventNameNative]
    EVENT_NAME_DOWNLOAD_CLEANUP_SUCCESS: _ClassVar[EventNameNative]
    EVENT_NAME_DOWNLOAD_ATTEMPT: _ClassVar[EventNameNative]
    EVENT_NAME_RETRY_DOWNLOAD: _ClassVar[EventNameNative]
    EVENT_NAME_DOWNLOAD_ACTIVITY: _ClassVar[EventNameNative]
    EVENT_NAME_NUDGE_VIEWED: _ClassVar[EventNameNative]
    EVENT_NAME_TRAY_INTERACTED: _ClassVar[EventNameNative]
    EVENT_NAME_TAB_INVOKED: _ClassVar[EventNameNative]
    EVENT_NAME_BUFFER: _ClassVar[EventNameNative]
    EVENT_NAME_PLAYBACK_BUFFER: _ClassVar[EventNameNative]
    EVENT_NAME_TRACK_PREFETCH_API: _ClassVar[EventNameNative]
    EVENT_NAME_ACTION_SHEET_CLOSED: _ClassVar[EventNameNative]
EVENT_NAME_UNSPECIFIED: EventNameNative
EVENT_NAME_APP_OPENED: EventNameNative
EVENT_NAME_APP_CLOSED: EventNameNative
EVENT_NAME_HEARTBEAT: EventNameNative
EVENT_NAME_REPORTED_ISSUE: EventNameNative
EVENT_NAME_MILESTONE_CLICKED: EventNameNative
EVENT_NAME_STARTED_VIDEO: EventNameNative
EVENT_NAME_WATCHED_VIDEO: EventNameNative
EVENT_NAME_FAILED_VIDEO: EventNameNative
EVENT_NAME_FAILED_RETRY_VIDEO: EventNameNative
EVENT_NAME_SKIPPED_VIDEO: EventNameNative
EVENT_NAME_ADD_TO_WATCHLIST: EventNameNative
EVENT_NAME_REMOVED_FROM_WATCHLIST: EventNameNative
EVENT_NAME_NOTIFICATION_CLICKED: EventNameNative
EVENT_NAME_NOTIFICATION_RECEIVED: EventNameNative
EVENT_NAME_GET_INSTALLED_APPS: EventNameNative
EVENT_NAME_CHANGE_CAPTION_SETTING: EventNameNative
EVENT_NAME_CHANGE_LANGUAGE: EventNameNative
EVENT_NAME_CHANGE_STREAM_QUALITY: EventNameNative
EVENT_NAME_FAILED_PLAYBACK_API: EventNameNative
EVENT_NAME_SUBMITTED_PARENTAL_PIN: EventNameNative
EVENT_NAME_CHANGED_NOTIFICATION_PERMISSION: EventNameNative
EVENT_NAME_PAGE_LOADED: EventNameNative
EVENT_NAME_VIEWED_PAGE_PAYMENT: EventNameNative
EVENT_NAME_PAYMENT_INITIATED: EventNameNative
EVENT_NAME_PAYMENT_FAILED: EventNameNative
EVENT_NAME_PURCHASED_SUBSCRIPTION: EventNameNative
EVENT_NAME_ERASED_SEARCH: EventNameNative
EVENT_NAME_EXIT_SEARCH: EventNameNative
EVENT_NAME_QUERIED_SEARCH: EventNameNative
EVENT_NAME_VIEWED_SEARCH_PAGE: EventNameNative
EVENT_NAME_APP_STARTUP_TIME: EventNameNative
EVENT_NAME_AD_REQUESTED: EventNameNative
EVENT_NAME_AD_RECEIVED: EventNameNative
EVENT_NAME_AD_LOAD_ERROR: EventNameNative
EVENT_NAME_AD_PLAY_ERROR: EventNameNative
EVENT_NAME_MISSED_TRANSLATION: EventNameNative
EVENT_NAME_FAILED_DOWNLOAD: EventNameNative
EVENT_NAME_STARTED_DOWNLOAD: EventNameNative
EVENT_NAME_COMPLETED_DOWNLOAD: EventNameNative
EVENT_NAME_PAUSED_DOWNLOAD: EventNameNative
EVENT_NAME_RESUMED_DOWNLOAD: EventNameNative
EVENT_NAME_CHANGED_DOWNLOAD: EventNameNative
EVENT_NAME_DELETED_DOWNLOAD: EventNameNative
EVENT_NAME_STOPPED_DOWNLOAD: EventNameNative
EVENT_NAME_WATCH_ATTEMPT: EventNameNative
EVENT_NAME_LOGGED_OUT: EventNameNative
EVENT_NAME_CLICKED_AD_FREE_NUDGE: EventNameNative
EVENT_NAME_VIEWED_AD_FREE_NUDGE: EventNameNative
EVENT_NAME_CLICKED_LANGUAGE_POPUP: EventNameNative
EVENT_NAME_VIEWED_LANGUAGE_POPUP: EventNameNative
EVENT_NAME_PRELOADED_ARTWORK: EventNameNative
EVENT_NAME_MILESTONE_VIEWED: EventNameNative
EVENT_NAME_VIEWED_WATCH_PAGE: EventNameNative
EVENT_NAME_PAGE_LOAD_FAILED: EventNameNative
EVENT_NAME_WIDGET_LOAD_FAILED: EventNameNative
EVENT_NAME_BUG_REPORT: EventNameNative
EVENT_NAME_SETTINGS_OPTION_NUDGE_VIEWED: EventNameNative
EVENT_NAME_SETTINGS_OPTION_NUDGE_CLICKED: EventNameNative
EVENT_NAME_APPLIED_SEARCH_FILTER: EventNameNative
EVENT_NAME_TAPPED_SEARCH: EventNameNative
EVENT_NAME_HELP_ITEM_CLICKED: EventNameNative
EVENT_NAME_HELP_SEARCHED: EventNameNative
EVENT_NAME_HELP_PAGE_VISITED: EventNameNative
EVENT_NAME_VIEWED_PAYMENT_METHODS: EventNameNative
EVENT_NAME_VIEWED_PAYMENT_STATUS: EventNameNative
EVENT_NAME_PAYMENT_X_INITIATED: EventNameNative
EVENT_NAME_AD_ERROR: EventNameNative
EVENT_NAME_PAYMENT_X_REQUEST: EventNameNative
EVENT_NAME_PAYMENT_X_RESPONSE: EventNameNative
EVENT_NAME_PAYMENT_X_ERROR: EventNameNative
EVENT_NAME_ONBOARDING_VIDEO_STARTED: EventNameNative
EVENT_NAME_ONBOARDING_VIDEO_FAILED: EventNameNative
EVENT_NAME_ONBOARDING_VIDEO_BUFFERED: EventNameNative
EVENT_NAME_VIEWED_UPGRADE_NUDGE: EventNameNative
EVENT_NAME_CLICKED_UPGRADE_NUDGE: EventNameNative
EVENT_NAME_CLICKED_ERROR_SCREEN_ITEM: EventNameNative
EVENT_NAME_EXITED_ERROR_SCREEN: EventNameNative
EVENT_NAME_VIEWED_VOTING_BUTTON: EventNameNative
EVENT_NAME_CLICKED_VOTING_BUTTON: EventNameNative
EVENT_NAME_VIEWED_VOTING_PAGE: EventNameNative
EVENT_NAME_QUIT_VOTING_PAGE: EventNameNative
EVENT_NAME_FAILED_VOTING: EventNameNative
EVENT_NAME_DOWNLOADS_MIGRATED: EventNameNative
EVENT_NAME_IMPRESSED_SEARCH: EventNameNative
EVENT_NAME_PROTO_TEST_MINERVA: EventNameNative
EVENT_NAME_PROTO_TEST_MINERVA2: EventNameNative
EVENT_NAME_WATCH_TAB_VIEWED: EventNameNative
EVENT_NAME_CARD_VIEWED: EventNameNative
EVENT_NAME_WATCH_TAB_INTERACTED: EventNameNative
EVENT_NAME_HELP_AND_SETTINGS_WIDGET_CLICKED: EventNameNative
EVENT_NAME_CLICKED_HELP_AND_SETTINGS_WIDGET: EventNameNative
EVENT_NAME_CARD_CLICKED: EventNameNative
EVENT_NAME_INAPP_RATING_TRIGGERED: EventNameNative
EVENT_NAME_CLICKED_NEXT_CONTENT: EventNameNative
EVENT_NAME_CHANGE_PLAYBACK_SPEED: EventNameNative
EVENT_NAME_CHANGE_PLAYER_ORIENTATION: EventNameNative
EVENT_NAME_CHANGE_VOLUME: EventNameNative
EVENT_NAME_CHANGE_BRIGHTNESS: EventNameNative
EVENT_NAME_CHANGE_FILL_STATUS: EventNameNative
EVENT_NAME_STARTED_GESTURE_ONBOARDING: EventNameNative
EVENT_NAME_COMPLETED_GESTURE_ONBOARDING: EventNameNative
EVENT_NAME_SUBSCRIBED_UPCOMING_CONTENT: EventNameNative
EVENT_NAME_VIEWED_SPLASH_PAGE: EventNameNative
EVENT_NAME_VIEWED_ERROR_PAGE: EventNameNative
EVENT_NAME_SEARCH_HISTORY: EventNameNative
EVENT_NAME_CLICKED_CAST_BUTTON: EventNameNative
EVENT_NAME_FAILED_CAST_ATTEMPT: EventNameNative
EVENT_NAME_VIEWED_CASTING_DEVICE_LIST: EventNameNative
EVENT_NAME_SELECTED_CASTING_DEVICE: EventNameNative
EVENT_NAME_RECEIVED_CASTING_CONNECTION_STATUS: EventNameNative
EVENT_NAME_VIEWED_CAST_CONTROL_WINDOW: EventNameNative
EVENT_NAME_MINIMISED_CAST_CONTROL: EventNameNative
EVENT_NAME_DISCONNECTED_CASTING: EventNameNative
EVENT_NAME_RECAPTCHA_ERROR: EventNameNative
EVENT_NAME_VIEWED_ENGAGEMENT_WIDGET: EventNameNative
EVENT_NAME_VIEWED_ENGAGEMENT_TAB: EventNameNative
EVENT_NAME_CLICKED_PLAY_NOW: EventNameNative
EVENT_NAME_VIEWED_SECTION: EventNameNative
EVENT_NAME_CLICKED_HINT: EventNameNative
EVENT_NAME_ENGAGED_SECTION: EventNameNative
EVENT_NAME_VIEWED_SECTION_RESULT: EventNameNative
EVENT_NAME_VIEWED_ENGAGEMENT_RESULT: EventNameNative
EVENT_NAME_PAYMENT_PAGE_LOAD_ERROR: EventNameNative
EVENT_NAME_ADS_RESOLVED: EventNameNative
EVENT_NAME_WATCH_PRELOAD: EventNameNative
EVENT_NAME_VIEWED_PAYMENT: EventNameNative
EVENT_NAME_VIEWED_REDEEM: EventNameNative
EVENT_NAME_REDEEM_COUPON_EVENT: EventNameNative
EVENT_NAME_REDEEM_USER_CONFIRMATION_EVENT: EventNameNative
EVENT_NAME_TOKEN_MISMATCHED: EventNameNative
EVENT_NAME_VIEWED_PAYMENT_HISTORY: EventNameNative
EVENT_NAME_PIN_VIEWED: EventNameNative
EVENT_NAME_PIN_CLICKED: EventNameNative
EVENT_NAME_VERIFIED_SNA_EVURL: EventNameNative
EVENT_NAME_VIEWED_REDEEM_COUPON: EventNameNative
EVENT_NAME_VIEWED_REDEEM_USER_CONFIRMATION_WIDGET: EventNameNative
EVENT_NAME_CLICKED_SHARE_ENGAGEMENT: EventNameNative
EVENT_NAME_VIEWED_CLAIM_REWARD: EventNameNative
EVENT_NAME_CLICKED_INFO_BUTTON: EventNameNative
EVENT_NAME_PAYMENT_METHOD_ACTION: EventNameNative
EVENT_NAME_VIEWED_PERMISSION_DIALOG: EventNameNative
EVENT_NAME_CLICKED_PERMISSION_DIALOG: EventNameNative
EVENT_NAME_UPDATED_APP_LANGUAGE: EventNameNative
EVENT_NAME_USP_VIEWED: EventNameNative
EVENT_NAME_SGAI_STITCH: EventNameNative
EVENT_NAME_SGAI_ERROR: EventNameNative
EVENT_NAME_PAGE_CONTENT_LOADED: EventNameNative
EVENT_NAME_FROZEN_FRAME: EventNameNative
EVENT_NAME_USER_INTERACTION_IN_PAUSE: EventNameNative
EVENT_NAME_SUBMITTED_COMMENT: EventNameNative
EVENT_NAME_CLICKED_MAXVIEW_MODE_SWITCHER: EventNameNative
EVENT_NAME_PRELOAD_JOURNEY: EventNameNative
EVENT_NAME_CACHE_WRITE: EventNameNative
EVENT_NAME_CACHE_HIT: EventNameNative
EVENT_NAME_CACHE_DELETE: EventNameNative
EVENT_NAME_CACHE_CLEAR: EventNameNative
EVENT_NAME_EVICTED_CONTENT_RATING_CARD: EventNameNative
EVENT_NAME_SURVEY_WIDGET_VIEWED: EventNameNative
EVENT_NAME_SUBMITTED_SURVEY: EventNameNative
EVENT_NAME_QUEUED_DOWNLOAD: EventNameNative
EVENT_NAME_START_API_PREFETCH: EventNameNative
EVENT_NAME_DOWNLOAD_CLEANUP_SUCCESS: EventNameNative
EVENT_NAME_DOWNLOAD_ATTEMPT: EventNameNative
EVENT_NAME_RETRY_DOWNLOAD: EventNameNative
EVENT_NAME_DOWNLOAD_ACTIVITY: EventNameNative
EVENT_NAME_NUDGE_VIEWED: EventNameNative
EVENT_NAME_TRAY_INTERACTED: EventNameNative
EVENT_NAME_TAB_INVOKED: EventNameNative
EVENT_NAME_BUFFER: EventNameNative
EVENT_NAME_PLAYBACK_BUFFER: EventNameNative
EVENT_NAME_TRACK_PREFETCH_API: EventNameNative
EVENT_NAME_ACTION_SHEET_CLOSED: EventNameNative
