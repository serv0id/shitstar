from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.login_method import login_method_pb2 as _login_method_pb2
from widget import divider_pb2 as _divider_pb2
from widget import list_pb2 as _list_pb2
from widget import list_v2_pb2 as _list_v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginWithPhoneWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "title", "input_label", "placeholder", "send_otp_button", "disclaimer_rich_text", "country_prefix", "phone_regex", "regex_error_message", "help_rich_text", "min_input_length", "max_input_length", "is_error", "error_message", "serviceable_countries", "prefix_error_message", "country_prefix_max_length", "regex_error_placeholder_message", "country_prefix_maximum_length", "country_selector_title", "is_input_field_auto_selected", "sms_confirmation_text", "back_button", "skip_button", "login_button", "login_data", "subwidget", "recaptcha_v2_enabled", "recaptcha_v2_error_message")
        class ServiceableCountriesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: LoginWithPhoneWidget.PhoneValidationRules
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[LoginWithPhoneWidget.PhoneValidationRules, _Mapping]] = ...) -> None: ...
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        INPUT_LABEL_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        SEND_OTP_BUTTON_FIELD_NUMBER: _ClassVar[int]
        DISCLAIMER_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
        PHONE_REGEX_FIELD_NUMBER: _ClassVar[int]
        REGEX_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        MIN_INPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
        MAX_INPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
        IS_ERROR_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        SERVICEABLE_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        PREFIX_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_PREFIX_MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
        REGEX_ERROR_PLACEHOLDER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_PREFIX_MAXIMUM_LENGTH_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_SELECTOR_TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_INPUT_FIELD_AUTO_SELECTED_FIELD_NUMBER: _ClassVar[int]
        SMS_CONFIRMATION_TEXT_FIELD_NUMBER: _ClassVar[int]
        BACK_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SKIP_BUTTON_FIELD_NUMBER: _ClassVar[int]
        LOGIN_BUTTON_FIELD_NUMBER: _ClassVar[int]
        LOGIN_DATA_FIELD_NUMBER: _ClassVar[int]
        SUBWIDGET_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_V2_ENABLED_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_V2_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        title: str
        input_label: str
        placeholder: str
        send_otp_button: LoginWithPhoneWidget.SendOtpButton
        disclaimer_rich_text: str
        country_prefix: str
        phone_regex: str
        regex_error_message: str
        help_rich_text: str
        min_input_length: int
        max_input_length: int
        is_error: bool
        error_message: str
        serviceable_countries: _containers.MessageMap[str, LoginWithPhoneWidget.PhoneValidationRules]
        prefix_error_message: str
        country_prefix_max_length: str
        regex_error_placeholder_message: str
        country_prefix_maximum_length: int
        country_selector_title: str
        is_input_field_auto_selected: bool
        sms_confirmation_text: str
        back_button: LoginWithPhoneWidget.BackButton
        skip_button: LoginWithPhoneWidget.SkipCTA
        login_button: _button_pb2.Button
        login_data: LoginWithPhoneWidget.LoginData
        subwidget: _containers.RepeatedCompositeFieldContainer[LoginWithPhoneWidget.ListSubWidget]
        recaptcha_v2_enabled: bool
        recaptcha_v2_error_message: str
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title: _Optional[str] = ..., input_label: _Optional[str] = ..., placeholder: _Optional[str] = ..., send_otp_button: _Optional[_Union[LoginWithPhoneWidget.SendOtpButton, _Mapping]] = ..., disclaimer_rich_text: _Optional[str] = ..., country_prefix: _Optional[str] = ..., phone_regex: _Optional[str] = ..., regex_error_message: _Optional[str] = ..., help_rich_text: _Optional[str] = ..., min_input_length: _Optional[int] = ..., max_input_length: _Optional[int] = ..., is_error: bool = ..., error_message: _Optional[str] = ..., serviceable_countries: _Optional[_Mapping[str, LoginWithPhoneWidget.PhoneValidationRules]] = ..., prefix_error_message: _Optional[str] = ..., country_prefix_max_length: _Optional[str] = ..., regex_error_placeholder_message: _Optional[str] = ..., country_prefix_maximum_length: _Optional[int] = ..., country_selector_title: _Optional[str] = ..., is_input_field_auto_selected: bool = ..., sms_confirmation_text: _Optional[str] = ..., back_button: _Optional[_Union[LoginWithPhoneWidget.BackButton, _Mapping]] = ..., skip_button: _Optional[_Union[LoginWithPhoneWidget.SkipCTA, _Mapping]] = ..., login_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., login_data: _Optional[_Union[LoginWithPhoneWidget.LoginData, _Mapping]] = ..., subwidget: _Optional[_Iterable[_Union[LoginWithPhoneWidget.ListSubWidget, _Mapping]]] = ..., recaptcha_v2_enabled: bool = ..., recaptcha_v2_error_message: _Optional[str] = ...) -> None: ...
    class ListSubWidget(_message.Message):
        __slots__ = ("list_widget", "divider_widget", "list_widget_v2")
        LIST_WIDGET_FIELD_NUMBER: _ClassVar[int]
        DIVIDER_WIDGET_FIELD_NUMBER: _ClassVar[int]
        LIST_WIDGET_V2_FIELD_NUMBER: _ClassVar[int]
        list_widget: _list_pb2.ListWidget
        divider_widget: _divider_pb2.DividerWidget
        list_widget_v2: _list_v2_pb2.ListV2Widget
        def __init__(self, list_widget: _Optional[_Union[_list_pb2.ListWidget, _Mapping]] = ..., divider_widget: _Optional[_Union[_divider_pb2.DividerWidget, _Mapping]] = ..., list_widget_v2: _Optional[_Union[_list_v2_pb2.ListV2Widget, _Mapping]] = ...) -> None: ...
    class SendOtpButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class BackButton(_message.Message):
        __slots__ = ("icon", "actions")
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon: str
        actions: _actions_pb2.Actions
        def __init__(self, icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class SkipCTA(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PhoneValidationRules(_message.Message):
        __slots__ = ("phone_regex", "min_input_length", "max_input_length", "country_name", "minimum_input_length", "maximum_input_length", "country_code")
        PHONE_REGEX_FIELD_NUMBER: _ClassVar[int]
        MIN_INPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
        MAX_INPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_INPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_INPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        phone_regex: str
        min_input_length: str
        max_input_length: str
        country_name: str
        minimum_input_length: int
        maximum_input_length: int
        country_code: str
        def __init__(self, phone_regex: _Optional[str] = ..., min_input_length: _Optional[str] = ..., max_input_length: _Optional[str] = ..., country_name: _Optional[str] = ..., minimum_input_length: _Optional[int] = ..., maximum_input_length: _Optional[int] = ..., country_code: _Optional[str] = ...) -> None: ...
    class LoginData(_message.Message):
        __slots__ = ("login_method", "animation_data")
        LOGIN_METHOD_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_DATA_FIELD_NUMBER: _ClassVar[int]
        login_method: _login_method_pb2.LoginMethod
        animation_data: LoginWithPhoneWidget.AnimationData
        def __init__(self, login_method: _Optional[_Union[_login_method_pb2.LoginMethod, str]] = ..., animation_data: _Optional[_Union[LoginWithPhoneWidget.AnimationData, _Mapping]] = ...) -> None: ...
    class AnimationData(_message.Message):
        __slots__ = ("login_initiation_message", "login_verification_message", "login_completion_message")
        LOGIN_INITIATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        LOGIN_VERIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        LOGIN_COMPLETION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        login_initiation_message: str
        login_verification_message: str
        login_completion_message: str
        def __init__(self, login_initiation_message: _Optional[str] = ..., login_verification_message: _Optional[str] = ..., login_completion_message: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LoginWithPhoneWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LoginWithPhoneWidget.Data, _Mapping]] = ...) -> None: ...
