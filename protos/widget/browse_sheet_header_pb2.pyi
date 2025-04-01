from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from widget import hero_gec_pb2 as _hero_gec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BrowseSheetHeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "title", "title_cutout", "superscript_tags")
    class Tag(_message.Message):
        __slots__ = ("type", "value", "actions")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        type: str
        value: str
        actions: _actions_pb2.Actions
        def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
    SUPERSCRIPT_TAGS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    title: str
    title_cutout: _image_pb2.Image
    superscript_tags: _containers.RepeatedCompositeFieldContainer[BrowseSheetHeaderWidget.Tag]
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., superscript_tags: _Optional[_Iterable[_Union[BrowseSheetHeaderWidget.Tag, _Mapping]]] = ...) -> None: ...
