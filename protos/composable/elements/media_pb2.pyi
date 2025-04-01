from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from composable.base import commons_pb2 as _commons_pb2
from composable.elements import composable_pb2 as _composable_pb2
from base import actions_pb2 as _actions_pb2
from composable.base import layout_traits_pb2 as _layout_traits_pb2
from composable.base import corner_radius_pb2 as _corner_radius_pb2
from composable.elements import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Media(_message.Message):
    __slots__ = ("src", "accessibility", "aspect_ratio", "media_height", "media_width", "height", "width", "placeholder", "corner_radius", "composable_commons", "actions")
    class Source(_message.Message):
        __slots__ = ("fallbackImageUrl", "url", "name")
        FALLBACKIMAGEURL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        fallbackImageUrl: str
        url: str
        name: str
        def __init__(self, fallbackImageUrl: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    SRC_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
    MEDIA_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    CORNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    src: Media.Source
    accessibility: _accessibility_pb2.Accessibility
    aspect_ratio: _image_pb2.AspectRatio
    media_height: _layout_traits_pb2.Layout
    media_width: _layout_traits_pb2.LayoutFillFixed
    height: _image_pb2.Height
    width: _image_pb2.Width
    placeholder: _composable_pb2.Composable
    corner_radius: _corner_radius_pb2.CornerRadius
    composable_commons: _commons_pb2.ComposableCommons
    actions: _actions_pb2.Actions
    def __init__(self, src: _Optional[_Union[Media.Source, _Mapping]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., aspect_ratio: _Optional[_Union[_image_pb2.AspectRatio, str]] = ..., media_height: _Optional[_Union[_layout_traits_pb2.Layout, _Mapping]] = ..., media_width: _Optional[_Union[_layout_traits_pb2.LayoutFillFixed, _Mapping]] = ..., height: _Optional[_Union[_image_pb2.Height, _Mapping]] = ..., width: _Optional[_Union[_image_pb2.Width, _Mapping]] = ..., placeholder: _Optional[_Union[_composable_pb2.Composable, _Mapping]] = ..., corner_radius: _Optional[_Union[_corner_radius_pb2.CornerRadius, _Mapping]] = ..., composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
