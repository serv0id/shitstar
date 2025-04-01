from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleMessageErrorWidget(_message.Message):
    __slots__ = ("widget_commons", "message", "visibility_duration", "before_actions", "after_actions")
    class Duration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LONG: _ClassVar[SimpleMessageErrorWidget.Duration]
        SHORT: _ClassVar[SimpleMessageErrorWidget.Duration]
    LONG: SimpleMessageErrorWidget.Duration
    SHORT: SimpleMessageErrorWidget.Duration
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_DURATION_FIELD_NUMBER: _ClassVar[int]
    BEFORE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    AFTER_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    message: str
    visibility_duration: SimpleMessageErrorWidget.Duration
    before_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    after_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., message: _Optional[str] = ..., visibility_duration: _Optional[_Union[SimpleMessageErrorWidget.Duration, str]] = ..., before_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., after_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
