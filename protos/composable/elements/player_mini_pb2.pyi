from composable.base import commons_pb2 as _commons_pb2
from composable.elements import composable_pb2 as _composable_pb2
from feature.autoplay import autoplay_info_pb2 as _autoplay_info_pb2
from composable.base import corner_radius_pb2 as _corner_radius_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerMini(_message.Message):
    __slots__ = ("composable_commons", "autoplay_info", "placeholder", "corner_radius")
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    AUTOPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    CORNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    autoplay_info: _autoplay_info_pb2.AutoplayInfo
    placeholder: _composable_pb2.Composable
    corner_radius: _corner_radius_pb2.CornerRadius
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., autoplay_info: _Optional[_Union[_autoplay_info_pb2.AutoplayInfo, _Mapping]] = ..., placeholder: _Optional[_Union[_composable_pb2.Composable, _Mapping]] = ..., corner_radius: _Optional[_Union[_corner_radius_pb2.CornerRadius, _Mapping]] = ...) -> None: ...
