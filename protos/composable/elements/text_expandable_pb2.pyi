from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from composable.base import commons_pb2 as _commons_pb2
from composable.elements import text_pb2 as _text_pb2
from composable.elements import icon_pb2 as _icon_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextExpandable(_message.Message):
    __slots__ = ("composable_commons", "text", "noOfLines", "truncation", "accessibility", "actions")
    class Truncation(_message.Message):
        __slots__ = ("label", "icon")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        label: _text_pb2.Text
        icon: _icon_pb2.Icon
        def __init__(self, label: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., icon: _Optional[_Union[_icon_pb2.Icon, _Mapping]] = ...) -> None: ...
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NOOFLINES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    text: _text_pb2.Text
    noOfLines: int
    truncation: TextExpandable.Truncation
    accessibility: _accessibility_pb2.Accessibility
    actions: _actions_pb2.Actions
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., text: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., noOfLines: _Optional[int] = ..., truncation: _Optional[_Union[TextExpandable.Truncation, _Mapping]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
