from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.atom import button_pb2 as _button_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListItemV2Widget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("default_state", "edit_state")
        DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
        EDIT_STATE_FIELD_NUMBER: _ClassVar[int]
        default_state: ListItemV2Widget.Item
        edit_state: ListItemV2Widget.Item
        def __init__(self, default_state: _Optional[_Union[ListItemV2Widget.Item, _Mapping]] = ..., edit_state: _Optional[_Union[ListItemV2Widget.Item, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("title", "sub_title", "leading_section", "trailing_section", "actions")
        class Section(_message.Message):
            __slots__ = ("icon", "image", "button")
            ICON_FIELD_NUMBER: _ClassVar[int]
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            BUTTON_FIELD_NUMBER: _ClassVar[int]
            icon: str
            image: _image_pb2.Image
            button: _button_pb2.Button
            def __init__(self, icon: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        LEADING_SECTION_FIELD_NUMBER: _ClassVar[int]
        TRAILING_SECTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        leading_section: ListItemV2Widget.Item.Section
        trailing_section: ListItemV2Widget.Item.Section
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., leading_section: _Optional[_Union[ListItemV2Widget.Item.Section, _Mapping]] = ..., trailing_section: _Optional[_Union[ListItemV2Widget.Item.Section, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ListItemV2Widget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ListItemV2Widget.Data, _Mapping]] = ...) -> None: ...
