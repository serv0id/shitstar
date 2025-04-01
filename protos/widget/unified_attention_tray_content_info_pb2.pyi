from base import widget_commons_pb2 as _widget_commons_pb2
from feature.tag import tag_pb2 as _tag_pb2
from widget import spotlight_info_pb2 as _spotlight_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnifiedAttentionTrayContentInfoWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("tags", "description", "wrapped_spotlight_info")
        TAGS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        WRAPPED_SPOTLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
        tags: _containers.RepeatedCompositeFieldContainer[_tag_pb2.Tag]
        description: str
        wrapped_spotlight_info: _spotlight_info_pb2.SpotlightInfoWidget
        def __init__(self, tags: _Optional[_Iterable[_Union[_tag_pb2.Tag, _Mapping]]] = ..., description: _Optional[str] = ..., wrapped_spotlight_info: _Optional[_Union[_spotlight_info_pb2.SpotlightInfoWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: UnifiedAttentionTrayContentInfoWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[UnifiedAttentionTrayContentInfoWidget.Data, _Mapping]] = ...) -> None: ...
