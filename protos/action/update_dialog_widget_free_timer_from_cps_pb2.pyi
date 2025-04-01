from feature.text import text_pb2 as _text_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateDialogWidgetFreeTimerFromCPSAction(_message.Message):
    __slots__ = ("placeholder_timer_text",)
    PLACEHOLDER_TIMER_TEXT_FIELD_NUMBER: _ClassVar[int]
    placeholder_timer_text: _text_pb2.Text
    def __init__(self, placeholder_timer_text: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
