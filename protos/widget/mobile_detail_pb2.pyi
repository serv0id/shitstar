from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MobileDetailWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("header", "mobile_number", "edit_button")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        EDIT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        header: str
        mobile_number: str
        edit_button: MobileDetailWidget.EditPhoneNumberButton
        def __init__(self, header: _Optional[str] = ..., mobile_number: _Optional[str] = ..., edit_button: _Optional[_Union[MobileDetailWidget.EditPhoneNumberButton, _Mapping]] = ...) -> None: ...
    class EditPhoneNumberButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MobileDetailWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MobileDetailWidget.Data, _Mapping]] = ...) -> None: ...
