from base import widget_commons_pb2 as _widget_commons_pb2
from widget import disclaimer_consent_pb2 as _disclaimer_consent_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsentContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("disclaimer_consent",)
        DISCLAIMER_CONSENT_FIELD_NUMBER: _ClassVar[int]
        disclaimer_consent: _disclaimer_consent_pb2.DisclaimerConsentWidget
        def __init__(self, disclaimer_consent: _Optional[_Union[_disclaimer_consent_pb2.DisclaimerConsentWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ConsentContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ConsentContainerWidget.Data, _Mapping]] = ...) -> None: ...
