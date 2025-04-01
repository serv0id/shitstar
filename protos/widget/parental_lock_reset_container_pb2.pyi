from base import widget_commons_pb2 as _widget_commons_pb2
from widget import parental_lock_setup_pb2 as _parental_lock_setup_pb2
from widget import reauthentication_pb2 as _reauthentication_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParentalLockResetContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("reauthentication", "pin_setup")
        REAUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
        PIN_SETUP_FIELD_NUMBER: _ClassVar[int]
        reauthentication: _reauthentication_pb2.ReAuthenticationWidget
        pin_setup: _parental_lock_setup_pb2.ParentalLockSetUpWidget
        def __init__(self, reauthentication: _Optional[_Union[_reauthentication_pb2.ReAuthenticationWidget, _Mapping]] = ..., pin_setup: _Optional[_Union[_parental_lock_setup_pb2.ParentalLockSetUpWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ParentalLockResetContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ParentalLockResetContainerWidget.Data, _Mapping]] = ...) -> None: ...
