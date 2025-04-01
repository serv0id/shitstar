from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from composable.base import commons_pb2 as _commons_pb2
from composable.elements import composable_pb2 as _composable_pb2
from composable.elements import icon_pb2 as _icon_pb2
from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagsFixed(_message.Message):
    __slots__ = ("composable_commons", "view", "prefix")
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    view: TagsView
    prefix: _composable_pb2.Composable
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., view: _Optional[_Union[TagsView, _Mapping]] = ..., prefix: _Optional[_Union[_composable_pb2.Composable, _Mapping]] = ...) -> None: ...

class TagsView(_message.Message):
    __slots__ = ("items", "separator", "spacing", "accessibility")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SEPARATOR_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_composable_pb2.Composable]
    separator: _icon_pb2.Icon
    spacing: _dls_tokens_pb2.DLSSpacings
    accessibility: _accessibility_pb2.Accessibility
    def __init__(self, items: _Optional[_Iterable[_Union[_composable_pb2.Composable, _Mapping]]] = ..., separator: _Optional[_Union[_icon_pb2.Icon, _Mapping]] = ..., spacing: _Optional[_Union[_dls_tokens_pb2.DLSSpacings, str]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
