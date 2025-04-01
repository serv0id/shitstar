from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReminderInfo(_message.Message):
    __slots__ = ("content_id", "is_reminder_set", "release_meta", "actions", "alt_add", "alt_remove")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REMINDER_SET_FIELD_NUMBER: _ClassVar[int]
    RELEASE_META_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ALT_ADD_FIELD_NUMBER: _ClassVar[int]
    ALT_REMOVE_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    is_reminder_set: bool
    release_meta: str
    actions: _actions_pb2.Actions
    alt_add: _accessibility_pb2.Accessibility
    alt_remove: _accessibility_pb2.Accessibility
    def __init__(self, content_id: _Optional[str] = ..., is_reminder_set: bool = ..., release_meta: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt_add: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alt_remove: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
