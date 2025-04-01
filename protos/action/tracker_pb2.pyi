from feature.trackers import tracker_pb2 as _tracker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrackerAction(_message.Message):
    __slots__ = ("tracker",)
    TRACKER_FIELD_NUMBER: _ClassVar[int]
    tracker: _tracker_pb2.Tracker
    def __init__(self, tracker: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ...) -> None: ...
