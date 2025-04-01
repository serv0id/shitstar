from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrelaunchFooterWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "links", "info_msgs")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        INFO_MSGS_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        links: _containers.RepeatedCompositeFieldContainer[PrelaunchFooterWidget.Link]
        info_msgs: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., links: _Optional[_Iterable[_Union[PrelaunchFooterWidget.Link, _Mapping]]] = ..., info_msgs: _Optional[_Iterable[str]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PrelaunchFooterWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PrelaunchFooterWidget.Data, _Mapping]] = ...) -> None: ...
