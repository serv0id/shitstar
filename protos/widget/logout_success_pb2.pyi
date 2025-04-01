from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogoutSuccessWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("message", "on_complete_actions", "redirect_deeplink")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ON_COMPLETE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        REDIRECT_DEEPLINK_FIELD_NUMBER: _ClassVar[int]
        message: str
        on_complete_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        redirect_deeplink: str
        def __init__(self, message: _Optional[str] = ..., on_complete_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., redirect_deeplink: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LogoutSuccessWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LogoutSuccessWidget.Data, _Mapping]] = ...) -> None: ...
