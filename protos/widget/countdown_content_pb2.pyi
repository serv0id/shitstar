from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.cw import cw_info_pb2 as _cw_info_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from feature.image import image_pb2 as _image_pb2
from feature.color import color_pb2 as _color_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CountdownContentWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "countdown", "footer", "actions", "play", "cw_info")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        PLAY_FIELD_NUMBER: _ClassVar[int]
        CW_INFO_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        countdown: int
        footer: CountdownContentWidget.Footer
        actions: _actions_pb2.Actions
        play: _illustration_pb2.Illustration
        cw_info: _cw_info_pb2.CwInfo
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., countdown: _Optional[int] = ..., footer: _Optional[_Union[CountdownContentWidget.Footer, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., play: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., cw_info: _Optional[_Union[_cw_info_pb2.CwInfo, _Mapping]] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("title", "sub_title", "title_color", "sub_title_color")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_COLOR_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_COLOR_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        title_color: _color_pb2.Color
        sub_title_color: _color_pb2.Color
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., title_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., sub_title_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CountdownContentWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CountdownContentWidget.Data, _Mapping]] = ...) -> None: ...
