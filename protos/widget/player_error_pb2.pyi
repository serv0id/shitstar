from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[LocalActionType]
    RETRY: _ClassVar[LocalActionType]
    GET_HELP: _ClassVar[LocalActionType]
    REPORT_ISSUE: _ClassVar[LocalActionType]
    CONTINUE: _ClassVar[LocalActionType]
    GO_BACK: _ClassVar[LocalActionType]

class PlayerErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OTHER: _ClassVar[PlayerErrorType]
    PSP: _ClassVar[PlayerErrorType]
    CONCURRENCY: _ClassVar[PlayerErrorType]
    MATURITY_WARNING: _ClassVar[PlayerErrorType]
    MATURITY_KID: _ClassVar[PlayerErrorType]
    TRAVELING_NOT_AVAILABLE: _ClassVar[PlayerErrorType]
    TRAVELING_GRACE_OVER: _ClassVar[PlayerErrorType]
    GENERAL: _ClassVar[PlayerErrorType]
    LOGIN_NUDGE: _ClassVar[PlayerErrorType]
    CONSENT_WARNING: _ClassVar[PlayerErrorType]
UNKNOWN: LocalActionType
RETRY: LocalActionType
GET_HELP: LocalActionType
REPORT_ISSUE: LocalActionType
CONTINUE: LocalActionType
GO_BACK: LocalActionType
OTHER: PlayerErrorType
PSP: PlayerErrorType
CONCURRENCY: PlayerErrorType
MATURITY_WARNING: PlayerErrorType
MATURITY_KID: PlayerErrorType
TRAVELING_NOT_AVAILABLE: PlayerErrorType
TRAVELING_GRACE_OVER: PlayerErrorType
GENERAL: PlayerErrorType
LOGIN_NUDGE: PlayerErrorType
CONSENT_WARNING: PlayerErrorType

class PlayerErrorWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("error_title", "error_message", "primary", "secondary", "error_image", "bottom_button", "error_info", "error_type", "error_code", "auto_retry", "consent_info")
    ERROR_TITLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_FIELD_NUMBER: _ClassVar[int]
    ERROR_IMAGE_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_BUTTON_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    AUTO_RETRY_FIELD_NUMBER: _ClassVar[int]
    CONSENT_INFO_FIELD_NUMBER: _ClassVar[int]
    error_title: str
    error_message: str
    primary: ErrorHandleButton
    secondary: ErrorHandleButton
    error_image: str
    bottom_button: ErrorHandleButton
    error_info: ErrorInfo
    error_type: PlayerErrorType
    error_code: str
    auto_retry: bool
    consent_info: ConsentInfo
    def __init__(self, error_title: _Optional[str] = ..., error_message: _Optional[str] = ..., primary: _Optional[_Union[ErrorHandleButton, _Mapping]] = ..., secondary: _Optional[_Union[ErrorHandleButton, _Mapping]] = ..., error_image: _Optional[str] = ..., bottom_button: _Optional[_Union[ErrorHandleButton, _Mapping]] = ..., error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ..., error_type: _Optional[_Union[PlayerErrorType, str]] = ..., error_code: _Optional[str] = ..., auto_retry: bool = ..., consent_info: _Optional[_Union[ConsentInfo, _Mapping]] = ...) -> None: ...

class ConsentInfo(_message.Message):
    __slots__ = ("consent_id", "identifier_type", "consent_type", "consent_version", "write_consent_url", "identifier", "consent_for")
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONSENT_URL_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FOR_FIELD_NUMBER: _ClassVar[int]
    consent_id: str
    identifier_type: str
    consent_type: str
    consent_version: int
    write_consent_url: str
    identifier: str
    consent_for: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, consent_id: _Optional[str] = ..., identifier_type: _Optional[str] = ..., consent_type: _Optional[str] = ..., consent_version: _Optional[int] = ..., write_consent_url: _Optional[str] = ..., identifier: _Optional[str] = ..., consent_for: _Optional[_Iterable[str]] = ...) -> None: ...

class ErrorInfo(_message.Message):
    __slots__ = ("title", "message", "image", "description")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    message: str
    image: _image_pb2.Image
    description: str
    def __init__(self, title: _Optional[str] = ..., message: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class GeneralActionButton(_message.Message):
    __slots__ = ("icon", "label", "error_handle_action", "action_auto_executed", "cta_name")
    ICON_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ERROR_HANDLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_AUTO_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    CTA_NAME_FIELD_NUMBER: _ClassVar[int]
    icon: str
    label: str
    error_handle_action: _actions_pb2.Actions
    action_auto_executed: bool
    cta_name: str
    def __init__(self, icon: _Optional[str] = ..., label: _Optional[str] = ..., error_handle_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., action_auto_executed: bool = ..., cta_name: _Optional[str] = ...) -> None: ...

class LocalActionButton(_message.Message):
    __slots__ = ("icon", "label", "type", "cta_name")
    ICON_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CTA_NAME_FIELD_NUMBER: _ClassVar[int]
    icon: str
    label: str
    type: LocalActionType
    cta_name: str
    def __init__(self, icon: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[_Union[LocalActionType, str]] = ..., cta_name: _Optional[str] = ...) -> None: ...

class ErrorHandleButton(_message.Message):
    __slots__ = ("general_action_button", "local_action_button")
    GENERAL_ACTION_BUTTON_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ACTION_BUTTON_FIELD_NUMBER: _ClassVar[int]
    general_action_button: GeneralActionButton
    local_action_button: LocalActionButton
    def __init__(self, general_action_button: _Optional[_Union[GeneralActionButton, _Mapping]] = ..., local_action_button: _Optional[_Union[LocalActionButton, _Mapping]] = ...) -> None: ...
