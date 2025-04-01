from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerReportMenuWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "report_options")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        REPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        report_options: _containers.RepeatedCompositeFieldContainer[PlayerReportMenuWidget.PlayerReportMenuItem]
        def __init__(self, title: _Optional[str] = ..., report_options: _Optional[_Iterable[_Union[PlayerReportMenuWidget.PlayerReportMenuItem, _Mapping]]] = ...) -> None: ...
    class PlayerReportMenuItem(_message.Message):
        __slots__ = ("icon_name", "title", "description", "result", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        title: str
        description: str
        result: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., result: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerReportMenuWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerReportMenuWidget.Data, _Mapping]] = ...) -> None: ...
