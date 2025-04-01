from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaContentInfoLargeWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title_cutout", "call_out_tags", "limit_tags", "description", "kebab")
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        CALL_OUT_TAGS_FIELD_NUMBER: _ClassVar[int]
        LIMIT_TAGS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        KEBAB_FIELD_NUMBER: _ClassVar[int]
        title_cutout: _image_pb2.Image
        call_out_tags: _containers.RepeatedCompositeFieldContainer[_callout_tag_pb2.CalloutTag]
        limit_tags: _containers.RepeatedCompositeFieldContainer[_callout_tag_pb2.CalloutTag]
        description: str
        kebab: _button_pb2.Button
        def __init__(self, title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., call_out_tags: _Optional[_Iterable[_Union[_callout_tag_pb2.CalloutTag, _Mapping]]] = ..., limit_tags: _Optional[_Iterable[_Union[_callout_tag_pb2.CalloutTag, _Mapping]]] = ..., description: _Optional[str] = ..., kebab: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MediaContentInfoLargeWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MediaContentInfoLargeWidget.Data, _Mapping]] = ...) -> None: ...
