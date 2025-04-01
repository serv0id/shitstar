from feature.atom import button_pb2 as _button_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoryHeaderConfig(_message.Message):
    __slots__ = ("number_of_stories", "duration_of_stories_in_ms", "mute_button", "trailing_button", "switch_on_tap", "switch_on_swipe", "automatic_switch")
    NUMBER_OF_STORIES_FIELD_NUMBER: _ClassVar[int]
    DURATION_OF_STORIES_IN_MS_FIELD_NUMBER: _ClassVar[int]
    MUTE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TRAILING_BUTTON_FIELD_NUMBER: _ClassVar[int]
    SWITCH_ON_TAP_FIELD_NUMBER: _ClassVar[int]
    SWITCH_ON_SWIPE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_SWITCH_FIELD_NUMBER: _ClassVar[int]
    number_of_stories: int
    duration_of_stories_in_ms: _containers.RepeatedScalarFieldContainer[int]
    mute_button: _button_pb2.Button
    trailing_button: _button_pb2.Button
    switch_on_tap: bool
    switch_on_swipe: bool
    automatic_switch: bool
    def __init__(self, number_of_stories: _Optional[int] = ..., duration_of_stories_in_ms: _Optional[_Iterable[int]] = ..., mute_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., trailing_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., switch_on_tap: bool = ..., switch_on_swipe: bool = ..., automatic_switch: bool = ...) -> None: ...
