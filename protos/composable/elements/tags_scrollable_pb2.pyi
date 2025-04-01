from composable.elements import tags_fixed_pb2 as _tags_fixed_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagsScrollable(_message.Message):
    __slots__ = ("composable_commons", "view")
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    view: _tags_fixed_pb2.TagsView
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., view: _Optional[_Union[_tags_fixed_pb2.TagsView, _Mapping]] = ...) -> None: ...
