from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TitleBarHeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "image_btn", "trailing_image_button", "header_parallax_disabled")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_BTN_FIELD_NUMBER: _ClassVar[int]
        TRAILING_IMAGE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        HEADER_PARALLAX_DISABLED_FIELD_NUMBER: _ClassVar[int]
        title: str
        image_btn: TitleBarHeaderWidget.ImageButton
        trailing_image_button: TitleBarHeaderWidget.ImageButton
        header_parallax_disabled: bool
        def __init__(self, title: _Optional[str] = ..., image_btn: _Optional[_Union[TitleBarHeaderWidget.ImageButton, _Mapping]] = ..., trailing_image_button: _Optional[_Union[TitleBarHeaderWidget.ImageButton, _Mapping]] = ..., header_parallax_disabled: bool = ...) -> None: ...
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
    data: TitleBarHeaderWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TitleBarHeaderWidget.Data, _Mapping]] = ...) -> None: ...
