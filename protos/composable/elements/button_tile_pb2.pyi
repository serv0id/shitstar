from composable.elements import text_pb2 as _text_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from base import actions_pb2 as _actions_pb2
from composable.elements import image_pb2 as _image_pb2
from composable.elements import icon_pb2 as _icon_pb2
from composable.elements import media_pb2 as _media_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonTileView(_message.Message):
    __slots__ = ("content", "label", "accessibility")
    class Content(_message.Message):
        __slots__ = ("icon", "image", "media")
        ICON_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        icon: _icon_pb2.Icon
        image: _image_pb2.Image
        media: _media_pb2.Media
        def __init__(self, icon: _Optional[_Union[_icon_pb2.Icon, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., media: _Optional[_Union[_media_pb2.Media, _Mapping]] = ...) -> None: ...
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    content: ButtonTileView.Content
    label: _text_pb2.Text
    accessibility: _accessibility_pb2.Accessibility
    def __init__(self, content: _Optional[_Union[ButtonTileView.Content, _Mapping]] = ..., label: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...

class ButtonTile(_message.Message):
    __slots__ = ("view", "composable_commons", "actions")
    VIEW_FIELD_NUMBER: _ClassVar[int]
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    view: ButtonTileView
    composable_commons: _commons_pb2.ComposableCommons
    actions: _actions_pb2.Actions
    def __init__(self, view: _Optional[_Union[ButtonTileView, _Mapping]] = ..., composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
