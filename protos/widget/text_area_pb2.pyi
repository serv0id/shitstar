from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextAreaWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLLAPSED: _ClassVar[TextAreaWidget.Status]
        EXPANDED: _ClassVar[TextAreaWidget.Status]
    COLLAPSED: TextAreaWidget.Status
    EXPANDED: TextAreaWidget.Status
    class Data(_message.Message):
        __slots__ = ("hint", "max_lines", "char_limit", "status", "action")
        HINT_FIELD_NUMBER: _ClassVar[int]
        MAX_LINES_FIELD_NUMBER: _ClassVar[int]
        CHAR_LIMIT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        hint: str
        max_lines: int
        char_limit: int
        status: TextAreaWidget.Status
        action: _actions_pb2.Actions
        def __init__(self, hint: _Optional[str] = ..., max_lines: _Optional[int] = ..., char_limit: _Optional[int] = ..., status: _Optional[_Union[TextAreaWidget.Status, str]] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TextAreaWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TextAreaWidget.Data, _Mapping]] = ...) -> None: ...
