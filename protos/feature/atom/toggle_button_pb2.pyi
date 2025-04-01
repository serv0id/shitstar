from feature.atom import button_pb2 as _button_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToggleButton(_message.Message):
    __slots__ = ("toggle_off_button", "toggle_on_button", "is_toggled_on")
    TOGGLE_OFF_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_ON_BUTTON_FIELD_NUMBER: _ClassVar[int]
    IS_TOGGLED_ON_FIELD_NUMBER: _ClassVar[int]
    toggle_off_button: _button_pb2.Button
    toggle_on_button: _button_pb2.Button
    is_toggled_on: bool
    def __init__(self, toggle_off_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., toggle_on_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., is_toggled_on: bool = ...) -> None: ...
