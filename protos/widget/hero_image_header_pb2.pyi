from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroImageHeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "image_btn", "backdrop_img", "title_cutout")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_BTN_FIELD_NUMBER: _ClassVar[int]
        BACKDROP_IMG_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        title: str
        image_btn: HeroImageHeaderWidget.ImageButton
        backdrop_img: _image_pb2.Image
        title_cutout: _image_pb2.Image
        def __init__(self, title: _Optional[str] = ..., image_btn: _Optional[_Union[HeroImageHeaderWidget.ImageButton, _Mapping]] = ..., backdrop_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class ImageButton(_message.Message):
        __slots__ = ("icon_name", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HeroImageHeaderWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HeroImageHeaderWidget.Data, _Mapping]] = ...) -> None: ...
