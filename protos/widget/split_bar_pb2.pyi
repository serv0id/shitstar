from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SplitBarWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("left_stack", "right_stack")
        LEFT_STACK_FIELD_NUMBER: _ClassVar[int]
        RIGHT_STACK_FIELD_NUMBER: _ClassVar[int]
        left_stack: _containers.RepeatedCompositeFieldContainer[SplitBarWidget.SplitBarItem]
        right_stack: _containers.RepeatedCompositeFieldContainer[SplitBarWidget.SplitBarItem]
        def __init__(self, left_stack: _Optional[_Iterable[_Union[SplitBarWidget.SplitBarItem, _Mapping]]] = ..., right_stack: _Optional[_Iterable[_Union[SplitBarWidget.SplitBarItem, _Mapping]]] = ...) -> None: ...
    class SplitBarItem(_message.Message):
        __slots__ = ("watch_hint", "indicator")
        WATCH_HINT_FIELD_NUMBER: _ClassVar[int]
        INDICATOR_FIELD_NUMBER: _ClassVar[int]
        watch_hint: SplitBarWidget.WatchHintCTA
        indicator: SplitBarWidget.PageIndicator
        def __init__(self, watch_hint: _Optional[_Union[SplitBarWidget.WatchHintCTA, _Mapping]] = ..., indicator: _Optional[_Union[SplitBarWidget.PageIndicator, _Mapping]] = ...) -> None: ...
    class WatchHintCTA(_message.Message):
        __slots__ = ("title", "subtitle", "icon_name", "content_id", "action")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        icon_name: str
        content_id: str
        action: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., icon_name: _Optional[str] = ..., content_id: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PageIndicator(_message.Message):
        __slots__ = ("current_page_pos", "total_page_count")
        CURRENT_PAGE_POS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
        current_page_pos: int
        total_page_count: int
        def __init__(self, current_page_pos: _Optional[int] = ..., total_page_count: _Optional[int] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SplitBarWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SplitBarWidget.Data, _Mapping]] = ...) -> None: ...
