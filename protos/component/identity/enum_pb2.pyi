from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class InputEnterMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INPUT_ENTER_MODE_UNSPECIFIED: _ClassVar[InputEnterMode]
    INPUT_ENTER_MODE_MANUAL: _ClassVar[InputEnterMode]
    INPUT_ENTER_MODE_AUTO: _ClassVar[InputEnterMode]

class LoginItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_ITEM_TYPE_UNSPECIFIED: _ClassVar[LoginItemType]
    LOGIN_ITEM_TYPE_GET_HELP_HYPERLINK: _ClassVar[LoginItemType]
    LOGIN_ITEM_TYPE_PHONE_NUMBER_TEXT_BOX: _ClassVar[LoginItemType]
    LOGIN_ITEM_TYPE_OTP_TEXT_BOX: _ClassVar[LoginItemType]

class LoginSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_SOURCE_UNSPECIFIED: _ClassVar[LoginSource]
    LOGIN_SOURCE_SKIPPABLE_LOGIN_PAGE: _ClassVar[LoginSource]

class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ITEM_TYPE_UNSPECIFIED: _ClassVar[ItemType]
    ITEM_TYPE_BUTTON: _ClassVar[ItemType]
    ITEM_TYPE_TEXT_BOX: _ClassVar[ItemType]
    ITEM_TYPE_HYPER_LINK: _ClassVar[ItemType]

class AppStoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_STORY_TYPE_UNSPECIFIED: _ClassVar[AppStoryType]
    APP_STORY_TYPE_PROFILE_EDUCATION: _ClassVar[AppStoryType]

class PermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERMISSION_TYPE_UNSPECIFIED: _ClassVar[PermissionType]
    PERMISSION_TYPE_APP_TRACKING: _ClassVar[PermissionType]

class PageSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAGE_SOURCE_UNSPECIFIED: _ClassVar[PageSource]
    PAGE_SOURCE_PROFILE_SELECTION: _ClassVar[PageSource]
    PAGE_SOURCE_MY_SPACE: _ClassVar[PageSource]
    PAGE_SOURCE_ONBOARDING: _ClassVar[PageSource]
    PAGE_SOURCE_EDIT_PROFILE: _ClassVar[PageSource]
    PAGE_SOURCE_ADD_PROFILE: _ClassVar[PageSource]
    PAGE_SOURCE_PRE_REGISTRATION: _ClassVar[PageSource]
    PAGE_SOURCE_RESET_PARENTAL_LOCK: _ClassVar[PageSource]
    PAGE_SOURCE_DELETED_ACCOUNT: _ClassVar[PageSource]
    PAGE_SOURCE_LOGIN: _ClassVar[PageSource]
    PAGE_SOURCE_SKIPPABLE_LOGIN: _ClassVar[PageSource]
    PAGE_SOURCE_TATA_SKY_SILENT_LOGIN: _ClassVar[PageSource]
    PAGE_SOURCE_MAGIC_LINK_SILENT_LOGIN: _ClassVar[PageSource]
    PAGE_SOURCE_DOWNLOAD: _ClassVar[PageSource]
    PAGE_SOURCE_WATCH_PAGE_SPORT_CONTENT: _ClassVar[PageSource]
    PAGE_SOURCE_WATCH_PAGE_LOGIN_EXP: _ClassVar[PageSource]
    PAGE_SOURCE_JIO_SILENT_LOGIN: _ClassVar[PageSource]
    PAGE_SOURCE_REPLAY: _ClassVar[PageSource]
    PAGE_SOURCE_TATA_SKY_MOBILE_SILENT_LOGIN: _ClassVar[PageSource]
    PAGE_SOURCE_DISH_TV_SILENT_LOGIN: _ClassVar[PageSource]

class PageReferrer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAGE_REFERRER_UNSPECIFIED: _ClassVar[PageReferrer]
    PAGE_REFERRER_MY_SPACE: _ClassVar[PageReferrer]
    PAGE_REFERRER_ONBOARDING: _ClassVar[PageReferrer]
    PAGE_REFERRER_WATCH: _ClassVar[PageReferrer]
    PAGE_REFERRER_PAYWALL: _ClassVar[PageReferrer]
    PAGE_REFERRER_CONSENT: _ClassVar[PageReferrer]
    PAGE_REFERRER_ONBOARDING_MANAGE: _ClassVar[PageReferrer]

class UtilityActionSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UTILITY_ACTION_SOURCE_UNSPECIFIED: _ClassVar[UtilityActionSource]
    UTILITY_ACTION_SOURCE_DELETED_ACCOUNT: _ClassVar[UtilityActionSource]

class PreReg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRE_REG_UNSPECIFIED: _ClassVar[PreReg]
    PRE_REG_JOURNEY: _ClassVar[PreReg]
    PRE_REG_ENTER_YOUR_DETAILS_JOURNEY: _ClassVar[PreReg]
    PRE_REG_VERIFY_PHONE_NUMBER_JOURNEY: _ClassVar[PreReg]
    PRE_REG_USER_REG_SUCCESS_JOURNEY: _ClassVar[PreReg]
    PRE_REG_ERROR_JOURNEY: _ClassVar[PreReg]

class VerificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERIFICATION_TYPE_UNSPECIFIED: _ClassVar[VerificationType]
    VERIFICATION_TYPE_SMS: _ClassVar[VerificationType]
    VERIFICATION_TYPE_CALL: _ClassVar[VerificationType]

class SettingsState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SETTINGS_STATE_UNSPECIFIED: _ClassVar[SettingsState]
    SETTINGS_STATE_ON: _ClassVar[SettingsState]
    SETTINGS_STATE_OFF: _ClassVar[SettingsState]

class LogoutTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGOUT_TRIGGER_UNSPECIFIED: _ClassVar[LogoutTrigger]
    LOGOUT_TRIGGER_USER: _ClassVar[LogoutTrigger]
    LOGOUT_TRIGGER_SYSTEM: _ClassVar[LogoutTrigger]
    LOGOUT_TRIGGER_AUTHENTICATION_ERROR: _ClassVar[LogoutTrigger]

class ResponseMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPONSE_MESSAGE_UNSPECIFIED: _ClassVar[ResponseMessage]
    RESPONSE_MESSAGE_SUCCESS: _ClassVar[ResponseMessage]
    RESPONSE_MESSAGE_INCORRECT_PARENTAL_LOCK_PIN: _ClassVar[ResponseMessage]

class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_TYPE_UNSPECIFIED: _ClassVar[UserType]
    USER_TYPE_NEW: _ClassVar[UserType]
    USER_TYPE_OLD: _ClassVar[UserType]

class LogoutMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGOUT_MODE_UNSPECIFIED: _ClassVar[LogoutMode]
    LOGOUT_MODE_MANUAL: _ClassVar[LogoutMode]
    LOGOUT_MODE_AUTO: _ClassVar[LogoutMode]

class LanguagePopupActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANGUAGE_POPUP_ACTION_TYPE_UNSPECIFIED: _ClassVar[LanguagePopupActionType]
    LANGUAGE_POPUP_ACTION_TYPE_CROSS_ICON_TAPPED: _ClassVar[LanguagePopupActionType]
    LANGUAGE_POPUP_ACTION_TYPE_DISMISS_VIEW_TOUCH_OUTSIDE: _ClassVar[LanguagePopupActionType]
    LANGUAGE_POPUP_ACTION_TYPE_SETTINGS_CTA_TAPPED: _ClassVar[LanguagePopupActionType]
    LANGUAGE_POPUP_ACTION_TYPE_LANGUAGE_SELECTED: _ClassVar[LanguagePopupActionType]

class LoginMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_METHOD_UNSPECIFIED: _ClassVar[LoginMethod]
    LOGIN_METHOD_MAGIC_LINK_SILENT_LOGIN: _ClassVar[LoginMethod]
    LOGIN_METHOD_TATA_SKY_SILENT_LOGIN: _ClassVar[LoginMethod]
    LOGIN_METHOD_SMS_OTP: _ClassVar[LoginMethod]
    LOGIN_METHOD_SMS_IVR: _ClassVar[LoginMethod]
    LOGIN_METHOD_TWILIO_SNA: _ClassVar[LoginMethod]
    LOGIN_METHOD_JIO_SILENT_LOGIN: _ClassVar[LoginMethod]
    LOGIN_METHOD_PREVIOUS_LOGIN: _ClassVar[LoginMethod]
    LOGIN_METHOD_PHONE_NUMBER_ENTER: _ClassVar[LoginMethod]
    LOGIN_METHOD_ENTER_EMAIL_ADDRESS: _ClassVar[LoginMethod]
    LOGIN_METHOD_QR_CODE: _ClassVar[LoginMethod]
    LOGIN_METHOD_TATA_SKY_MOBILE_SILENT_LOGIN: _ClassVar[LoginMethod]
    LOGIN_METHOD_DISH_TV_SILENT_LOGIN: _ClassVar[LoginMethod]

class InitiateBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INITIATE_BY_UNSPECIFIED: _ClassVar[InitiateBy]
    INITIATE_BY_PHONE_IVR: _ClassVar[InitiateBy]
    INITIATE_BY_PHONE_SNA: _ClassVar[InitiateBy]
    INITIATE_BY_EMAIL_OTP: _ClassVar[InitiateBy]

class SnaVendorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SNA_VENDOR_TYPE_UNSPECIFIED: _ClassVar[SnaVendorType]
    SNA_VENDOR_TYPE_TWILIO: _ClassVar[SnaVendorType]

class LoginMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_MODE_UNSPECIFIED: _ClassVar[LoginMode]
    LOGIN_MODE_PHONE_NUMBER_ENTER: _ClassVar[LoginMode]
    LOGIN_MODE_PREVIOUS_LOGIN: _ClassVar[LoginMode]
    LOGIN_MODE_EMAIL_ADDRESS_ENTER: _ClassVar[LoginMode]
    LOGIN_MODE_QR_CODE: _ClassVar[LoginMode]

class LoginTemplate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_TEMPLATE_UNSPECIFIED: _ClassVar[LoginTemplate]
    LOGIN_TEMPLATE_QR_CODE: _ClassVar[LoginTemplate]
    LOGIN_TEMPLATE_PREVIOUS_LOGIN: _ClassVar[LoginTemplate]

class OnboardingIngressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONBOARDING_INGRESS_TYPE_UNSPECIFIED: _ClassVar[OnboardingIngressType]
    ONBOARDING_INGRESS_TYPE_INLINE_ONBOARDING: _ClassVar[OnboardingIngressType]
    ONBOARDING_INGRESS_TYPE_INLINE_END_SHEET: _ClassVar[OnboardingIngressType]
    ONBOARDING_INGRESS_TYPE_INLINE_BANNER: _ClassVar[OnboardingIngressType]
    ONBOARDING_INGRESS_TYPE_INLINE_HOME_BACK: _ClassVar[OnboardingIngressType]

class LoginResiliencyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN_RESILIENCY_MODE_UNSPECIFIED: _ClassVar[LoginResiliencyMode]
    LOGIN_RESILIENCY_MODE_ENABLED: _ClassVar[LoginResiliencyMode]
    LOGIN_RESILIENCY_MODE_DISABLED: _ClassVar[LoginResiliencyMode]
INPUT_ENTER_MODE_UNSPECIFIED: InputEnterMode
INPUT_ENTER_MODE_MANUAL: InputEnterMode
INPUT_ENTER_MODE_AUTO: InputEnterMode
LOGIN_ITEM_TYPE_UNSPECIFIED: LoginItemType
LOGIN_ITEM_TYPE_GET_HELP_HYPERLINK: LoginItemType
LOGIN_ITEM_TYPE_PHONE_NUMBER_TEXT_BOX: LoginItemType
LOGIN_ITEM_TYPE_OTP_TEXT_BOX: LoginItemType
LOGIN_SOURCE_UNSPECIFIED: LoginSource
LOGIN_SOURCE_SKIPPABLE_LOGIN_PAGE: LoginSource
ITEM_TYPE_UNSPECIFIED: ItemType
ITEM_TYPE_BUTTON: ItemType
ITEM_TYPE_TEXT_BOX: ItemType
ITEM_TYPE_HYPER_LINK: ItemType
APP_STORY_TYPE_UNSPECIFIED: AppStoryType
APP_STORY_TYPE_PROFILE_EDUCATION: AppStoryType
PERMISSION_TYPE_UNSPECIFIED: PermissionType
PERMISSION_TYPE_APP_TRACKING: PermissionType
PAGE_SOURCE_UNSPECIFIED: PageSource
PAGE_SOURCE_PROFILE_SELECTION: PageSource
PAGE_SOURCE_MY_SPACE: PageSource
PAGE_SOURCE_ONBOARDING: PageSource
PAGE_SOURCE_EDIT_PROFILE: PageSource
PAGE_SOURCE_ADD_PROFILE: PageSource
PAGE_SOURCE_PRE_REGISTRATION: PageSource
PAGE_SOURCE_RESET_PARENTAL_LOCK: PageSource
PAGE_SOURCE_DELETED_ACCOUNT: PageSource
PAGE_SOURCE_LOGIN: PageSource
PAGE_SOURCE_SKIPPABLE_LOGIN: PageSource
PAGE_SOURCE_TATA_SKY_SILENT_LOGIN: PageSource
PAGE_SOURCE_MAGIC_LINK_SILENT_LOGIN: PageSource
PAGE_SOURCE_DOWNLOAD: PageSource
PAGE_SOURCE_WATCH_PAGE_SPORT_CONTENT: PageSource
PAGE_SOURCE_WATCH_PAGE_LOGIN_EXP: PageSource
PAGE_SOURCE_JIO_SILENT_LOGIN: PageSource
PAGE_SOURCE_REPLAY: PageSource
PAGE_SOURCE_TATA_SKY_MOBILE_SILENT_LOGIN: PageSource
PAGE_SOURCE_DISH_TV_SILENT_LOGIN: PageSource
PAGE_REFERRER_UNSPECIFIED: PageReferrer
PAGE_REFERRER_MY_SPACE: PageReferrer
PAGE_REFERRER_ONBOARDING: PageReferrer
PAGE_REFERRER_WATCH: PageReferrer
PAGE_REFERRER_PAYWALL: PageReferrer
PAGE_REFERRER_CONSENT: PageReferrer
PAGE_REFERRER_ONBOARDING_MANAGE: PageReferrer
UTILITY_ACTION_SOURCE_UNSPECIFIED: UtilityActionSource
UTILITY_ACTION_SOURCE_DELETED_ACCOUNT: UtilityActionSource
PRE_REG_UNSPECIFIED: PreReg
PRE_REG_JOURNEY: PreReg
PRE_REG_ENTER_YOUR_DETAILS_JOURNEY: PreReg
PRE_REG_VERIFY_PHONE_NUMBER_JOURNEY: PreReg
PRE_REG_USER_REG_SUCCESS_JOURNEY: PreReg
PRE_REG_ERROR_JOURNEY: PreReg
VERIFICATION_TYPE_UNSPECIFIED: VerificationType
VERIFICATION_TYPE_SMS: VerificationType
VERIFICATION_TYPE_CALL: VerificationType
SETTINGS_STATE_UNSPECIFIED: SettingsState
SETTINGS_STATE_ON: SettingsState
SETTINGS_STATE_OFF: SettingsState
LOGOUT_TRIGGER_UNSPECIFIED: LogoutTrigger
LOGOUT_TRIGGER_USER: LogoutTrigger
LOGOUT_TRIGGER_SYSTEM: LogoutTrigger
LOGOUT_TRIGGER_AUTHENTICATION_ERROR: LogoutTrigger
RESPONSE_MESSAGE_UNSPECIFIED: ResponseMessage
RESPONSE_MESSAGE_SUCCESS: ResponseMessage
RESPONSE_MESSAGE_INCORRECT_PARENTAL_LOCK_PIN: ResponseMessage
USER_TYPE_UNSPECIFIED: UserType
USER_TYPE_NEW: UserType
USER_TYPE_OLD: UserType
LOGOUT_MODE_UNSPECIFIED: LogoutMode
LOGOUT_MODE_MANUAL: LogoutMode
LOGOUT_MODE_AUTO: LogoutMode
LANGUAGE_POPUP_ACTION_TYPE_UNSPECIFIED: LanguagePopupActionType
LANGUAGE_POPUP_ACTION_TYPE_CROSS_ICON_TAPPED: LanguagePopupActionType
LANGUAGE_POPUP_ACTION_TYPE_DISMISS_VIEW_TOUCH_OUTSIDE: LanguagePopupActionType
LANGUAGE_POPUP_ACTION_TYPE_SETTINGS_CTA_TAPPED: LanguagePopupActionType
LANGUAGE_POPUP_ACTION_TYPE_LANGUAGE_SELECTED: LanguagePopupActionType
LOGIN_METHOD_UNSPECIFIED: LoginMethod
LOGIN_METHOD_MAGIC_LINK_SILENT_LOGIN: LoginMethod
LOGIN_METHOD_TATA_SKY_SILENT_LOGIN: LoginMethod
LOGIN_METHOD_SMS_OTP: LoginMethod
LOGIN_METHOD_SMS_IVR: LoginMethod
LOGIN_METHOD_TWILIO_SNA: LoginMethod
LOGIN_METHOD_JIO_SILENT_LOGIN: LoginMethod
LOGIN_METHOD_PREVIOUS_LOGIN: LoginMethod
LOGIN_METHOD_PHONE_NUMBER_ENTER: LoginMethod
LOGIN_METHOD_ENTER_EMAIL_ADDRESS: LoginMethod
LOGIN_METHOD_QR_CODE: LoginMethod
LOGIN_METHOD_TATA_SKY_MOBILE_SILENT_LOGIN: LoginMethod
LOGIN_METHOD_DISH_TV_SILENT_LOGIN: LoginMethod
INITIATE_BY_UNSPECIFIED: InitiateBy
INITIATE_BY_PHONE_IVR: InitiateBy
INITIATE_BY_PHONE_SNA: InitiateBy
INITIATE_BY_EMAIL_OTP: InitiateBy
SNA_VENDOR_TYPE_UNSPECIFIED: SnaVendorType
SNA_VENDOR_TYPE_TWILIO: SnaVendorType
LOGIN_MODE_UNSPECIFIED: LoginMode
LOGIN_MODE_PHONE_NUMBER_ENTER: LoginMode
LOGIN_MODE_PREVIOUS_LOGIN: LoginMode
LOGIN_MODE_EMAIL_ADDRESS_ENTER: LoginMode
LOGIN_MODE_QR_CODE: LoginMode
LOGIN_TEMPLATE_UNSPECIFIED: LoginTemplate
LOGIN_TEMPLATE_QR_CODE: LoginTemplate
LOGIN_TEMPLATE_PREVIOUS_LOGIN: LoginTemplate
ONBOARDING_INGRESS_TYPE_UNSPECIFIED: OnboardingIngressType
ONBOARDING_INGRESS_TYPE_INLINE_ONBOARDING: OnboardingIngressType
ONBOARDING_INGRESS_TYPE_INLINE_END_SHEET: OnboardingIngressType
ONBOARDING_INGRESS_TYPE_INLINE_BANNER: OnboardingIngressType
ONBOARDING_INGRESS_TYPE_INLINE_HOME_BACK: OnboardingIngressType
LOGIN_RESILIENCY_MODE_UNSPECIFIED: LoginResiliencyMode
LOGIN_RESILIENCY_MODE_ENABLED: LoginResiliencyMode
LOGIN_RESILIENCY_MODE_DISABLED: LoginResiliencyMode
