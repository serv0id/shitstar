from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.error import error_info_pb2 as _error_info_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadErrorWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETRY: _ClassVar[DownloadErrorWidget.ActionType]
        CANCEL: _ClassVar[DownloadErrorWidget.ActionType]
    RETRY: DownloadErrorWidget.ActionType
    CANCEL: DownloadErrorWidget.ActionType
    class Data(_message.Message):
        __slots__ = ("error_info", "primary", "secondary")
        ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_FIELD_NUMBER: _ClassVar[int]
        error_info: _error_info_pb2.ErrorInfo
        primary: DownloadErrorWidget.CTAButton
        secondary: DownloadErrorWidget.CTAButton
        def __init__(self, error_info: _Optional[_Union[_error_info_pb2.ErrorInfo, _Mapping]] = ..., primary: _Optional[_Union[DownloadErrorWidget.CTAButton, _Mapping]] = ..., secondary: _Optional[_Union[DownloadErrorWidget.CTAButton, _Mapping]] = ...) -> None: ...
    class CTAButton(_message.Message):
        __slots__ = ("label", "actions", "type")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        label: str
        actions: _actions_pb2.Actions
        type: DownloadErrorWidget.ActionType
        def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., type: _Optional[_Union[DownloadErrorWidget.ActionType, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DownloadErrorWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DownloadErrorWidget.Data, _Mapping]] = ...) -> None: ...
