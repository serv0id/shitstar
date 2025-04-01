from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaClarityComparatorOverlay(_message.Message):
    __slots__ = ("low_media_title", "higher_media_title", "actions")
    LOW_MEDIA_TITLE_FIELD_NUMBER: _ClassVar[int]
    HIGHER_MEDIA_TITLE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    low_media_title: str
    higher_media_title: str
    actions: _actions_pb2.Actions
    def __init__(self, low_media_title: _Optional[str] = ..., higher_media_title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
