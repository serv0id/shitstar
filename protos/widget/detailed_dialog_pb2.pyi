from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetailedDialogWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "subtitle", "left_image", "info_text", "primary_btn", "right_image")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        LEFT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        INFO_TEXT_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BTN_FIELD_NUMBER: _ClassVar[int]
        RIGHT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        left_image: _image_pb2.Image
        info_text: str
        primary_btn: DetailedDialogWidget.Button
        right_image: _image_pb2.Image
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., left_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., info_text: _Optional[str] = ..., primary_btn: _Optional[_Union[DetailedDialogWidget.Button, _Mapping]] = ..., right_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
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
    data: DetailedDialogWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DetailedDialogWidget.Data, _Mapping]] = ...) -> None: ...
