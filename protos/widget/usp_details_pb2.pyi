from base import widget_commons_pb2 as _widget_commons_pb2
from widget import image_banner_pb2 as _image_banner_pb2
from feature.branding import brand_pb2 as _brand_pb2
from widget import grid_pb2 as _grid_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class USPDetailsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "subtitle", "background", "item")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        background: str
        item: USPDetailsWidget.Item
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., background: _Optional[str] = ..., item: _Optional[_Union[USPDetailsWidget.Item, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("image_banner", "grid")
        IMAGE_BANNER_FIELD_NUMBER: _ClassVar[int]
        GRID_FIELD_NUMBER: _ClassVar[int]
        image_banner: _image_banner_pb2.ImageBannerWidget
        grid: _grid_pb2.GridWidget
        def __init__(self, image_banner: _Optional[_Union[_image_banner_pb2.ImageBannerWidget, _Mapping]] = ..., grid: _Optional[_Union[_grid_pb2.GridWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: USPDetailsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[USPDetailsWidget.Data, _Mapping]] = ...) -> None: ...
