from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageTitleHeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "subtitle", "header")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        header: PageTitleHeaderWidget.Header
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., header: _Optional[_Union[PageTitleHeaderWidget.Header, _Mapping]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("regular_header", "decorated_header")
        REGULAR_HEADER_FIELD_NUMBER: _ClassVar[int]
        DECORATED_HEADER_FIELD_NUMBER: _ClassVar[int]
        regular_header: PageTitleHeaderWidget.RegularHeader
        decorated_header: PageTitleHeaderWidget.DecoratedHeader
        def __init__(self, regular_header: _Optional[_Union[PageTitleHeaderWidget.RegularHeader, _Mapping]] = ..., decorated_header: _Optional[_Union[PageTitleHeaderWidget.DecoratedHeader, _Mapping]] = ...) -> None: ...
    class RegularHeader(_message.Message):
        __slots__ = ("title", "subtitle")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ...) -> None: ...
    class DecoratedHeader(_message.Message):
        __slots__ = ("elements", "subtitle")
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[_callout_tag_pb2.CalloutTag]
        subtitle: str
        def __init__(self, elements: _Optional[_Iterable[_Union[_callout_tag_pb2.CalloutTag, _Mapping]]] = ..., subtitle: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PageTitleHeaderWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PageTitleHeaderWidget.Data, _Mapping]] = ...) -> None: ...
