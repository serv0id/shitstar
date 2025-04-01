from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.consent import consent_type_pb2 as _consent_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommsPreferenceSuccessWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("message", "consent_type")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        CONSENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        message: str
        consent_type: _consent_type_pb2.ConsentType
        def __init__(self, message: _Optional[str] = ..., consent_type: _Optional[_Union[_consent_type_pb2.ConsentType, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CommsPreferenceSuccessWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CommsPreferenceSuccessWidget.Data, _Mapping]] = ...) -> None: ...
