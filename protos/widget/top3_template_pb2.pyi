from base import widget_commons_pb2 as _widget_commons_pb2
from widget import media_ranking_pb2 as _media_ranking_pb2
from widget import text_prompt_pb2 as _text_prompt_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Top3TemplateWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("titles", "items")
        TITLES_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        titles: _text_prompt_pb2.TextPromptWidget
        items: _media_ranking_pb2.MediaRankingWidget
        def __init__(self, titles: _Optional[_Union[_text_prompt_pb2.TextPromptWidget, _Mapping]] = ..., items: _Optional[_Union[_media_ranking_pb2.MediaRankingWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: Top3TemplateWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[Top3TemplateWidget.Data, _Mapping]] = ...) -> None: ...
