from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from widget import text_list_pb2 as _text_list_pb2
from feature.text import text_pb2 as _text_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DialogWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Align(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED: _ClassVar[DialogWidget.Align]
        LEFT: _ClassVar[DialogWidget.Align]
        RIGHT: _ClassVar[DialogWidget.Align]
        CENTER: _ClassVar[DialogWidget.Align]
    UNDEFINED: DialogWidget.Align
    LEFT: DialogWidget.Align
    RIGHT: DialogWidget.Align
    CENTER: DialogWidget.Align
    class Data(_message.Message):
        __slots__ = ("img", "title", "description", "primary_button", "secondary_button", "icon_name", "over_sheet_lottie_name", "should_animate_content", "hide_close_icon", "widget_alignment", "text_list", "timer_text", "illustration", "image", "icon", "lottie")
        IMG_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        OVER_SHEET_LOTTIE_NAME_FIELD_NUMBER: _ClassVar[int]
        SHOULD_ANIMATE_CONTENT_FIELD_NUMBER: _ClassVar[int]
        HIDE_CLOSE_ICON_FIELD_NUMBER: _ClassVar[int]
        WIDGET_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
        TIMER_TEXT_FIELD_NUMBER: _ClassVar[int]
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_FIELD_NUMBER: _ClassVar[int]
        img: _image_pb2.Image
        title: str
        description: str
        primary_button: DialogWidget.Button
        secondary_button: DialogWidget.Button
        icon_name: str
        over_sheet_lottie_name: str
        should_animate_content: bool
        hide_close_icon: bool
        widget_alignment: DialogWidget.Align
        text_list: _text_list_pb2.TextListWidget
        timer_text: _text_pb2.Text
        illustration: _illustration_pb2.Illustration
        image: _image_pb2.Image
        icon: str
        lottie: str
        def __init__(self, img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., primary_button: _Optional[_Union[DialogWidget.Button, _Mapping]] = ..., secondary_button: _Optional[_Union[DialogWidget.Button, _Mapping]] = ..., icon_name: _Optional[str] = ..., over_sheet_lottie_name: _Optional[str] = ..., should_animate_content: bool = ..., hide_close_icon: bool = ..., widget_alignment: _Optional[_Union[DialogWidget.Align, str]] = ..., text_list: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., timer_text: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., illustration: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., icon: _Optional[str] = ..., lottie: _Optional[str] = ...) -> None: ...
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
    data: DialogWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DialogWidget.Data, _Mapping]] = ...) -> None: ...
