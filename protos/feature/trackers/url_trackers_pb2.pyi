from feature.trackers import tracker_pb2 as _tracker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UrlTrackers(_message.Message):
    __slots__ = ("click", "impressions", "interaction")
    CLICK_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_FIELD_NUMBER: _ClassVar[int]
    click: _tracker_pb2.Tracker
    impressions: _tracker_pb2.Tracker
    interaction: _tracker_pb2.Tracker
    def __init__(self, click: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ..., impressions: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ..., interaction: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ...) -> None: ...
