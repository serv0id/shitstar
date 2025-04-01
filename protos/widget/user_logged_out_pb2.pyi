from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserLoggedOutWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("img", "title", "description", "button", "icon_name", "is_cancelable")
        IMG_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_CANCELABLE_FIELD_NUMBER: _ClassVar[int]
        img: _image_pb2.Image
        title: str
        description: str
        button: UserLoggedOutWidget.Button
        icon_name: str
        is_cancelable: bool
        def __init__(self, img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., button: _Optional[_Union[UserLoggedOutWidget.Button, _Mapping]] = ..., icon_name: _Optional[str] = ..., is_cancelable: bool = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: UserLoggedOutWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[UserLoggedOutWidget.Data, _Mapping]] = ...) -> None: ...
