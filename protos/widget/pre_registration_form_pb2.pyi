from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreRegistrationFormWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "full_name", "phone_number", "email", "consent", "disclaimer_rich_text", "help_rich_text", "loading_text")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        FULL_NAME_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        CONSENT_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_FIELD_NUMBER: _ClassVar[int]
        DISCLAIMER_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        LOADING_TEXT_FIELD_NUMBER: _ClassVar[int]
        title: str
        full_name: PreRegistrationFormWidget.Field
        phone_number: PreRegistrationFormWidget.FieldPhoneNumber
        email: PreRegistrationFormWidget.Field
        consent: PreRegistrationFormWidget.FieldConsent
        disclaimer_rich_text: PreRegistrationFormWidget.DisclaimerRichText
        help_rich_text: str
        loading_text: str
        def __init__(self, title: _Optional[str] = ..., full_name: _Optional[_Union[PreRegistrationFormWidget.Field, _Mapping]] = ..., phone_number: _Optional[_Union[PreRegistrationFormWidget.FieldPhoneNumber, _Mapping]] = ..., email: _Optional[_Union[PreRegistrationFormWidget.Field, _Mapping]] = ..., consent: _Optional[_Union[PreRegistrationFormWidget.FieldConsent, _Mapping]] = ..., disclaimer_rich_text: _Optional[_Union[PreRegistrationFormWidget.DisclaimerRichText, _Mapping]] = ..., help_rich_text: _Optional[str] = ..., loading_text: _Optional[str] = ..., **kwargs) -> None: ...
    class Field(_message.Message):
        __slots__ = ("label", "placeholder", "value", "regex", "regex_error_message", "error_message", "max_length")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        REGEX_FIELD_NUMBER: _ClassVar[int]
        REGEX_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
        label: str
        placeholder: str
        value: str
        regex: str
        regex_error_message: str
        error_message: str
        max_length: int
        def __init__(self, label: _Optional[str] = ..., placeholder: _Optional[str] = ..., value: _Optional[str] = ..., regex: _Optional[str] = ..., regex_error_message: _Optional[str] = ..., error_message: _Optional[str] = ..., max_length: _Optional[int] = ...) -> None: ...
    class FieldConsent(_message.Message):
        __slots__ = ("label", "consent_ids")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        CONSENT_IDS_FIELD_NUMBER: _ClassVar[int]
        label: str
        consent_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, label: _Optional[str] = ..., consent_ids: _Optional[_Iterable[int]] = ...) -> None: ...
    class FieldPhoneNumber(_message.Message):
        __slots__ = ("label", "placeholder", "value", "country_prefix", "regex", "regex_error_message", "max_length", "min_length", "error_message")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
        REGEX_FIELD_NUMBER: _ClassVar[int]
        REGEX_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
        MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        label: str
        placeholder: str
        value: str
        country_prefix: str
        regex: str
        regex_error_message: str
        max_length: int
        min_length: int
        error_message: str
        def __init__(self, label: _Optional[str] = ..., placeholder: _Optional[str] = ..., value: _Optional[str] = ..., country_prefix: _Optional[str] = ..., regex: _Optional[str] = ..., regex_error_message: _Optional[str] = ..., max_length: _Optional[int] = ..., min_length: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("title", "suffix_icon", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUFFIX_ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        suffix_icon: str
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., suffix_icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class DisclaimerRichText(_message.Message):
        __slots__ = ("text", "links")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        text: str
        links: _containers.RepeatedCompositeFieldContainer[PreRegistrationFormWidget.DisclaimerRichTextLink]
        def __init__(self, text: _Optional[str] = ..., links: _Optional[_Iterable[_Union[PreRegistrationFormWidget.DisclaimerRichTextLink, _Mapping]]] = ...) -> None: ...
    class DisclaimerRichTextLink(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PreRegistrationFormWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PreRegistrationFormWidget.Data, _Mapping]] = ...) -> None: ...
