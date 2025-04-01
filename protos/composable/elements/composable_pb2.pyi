from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Composable(_message.Message):
    __slots__ = ("type", "content")
    class ElementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEXT: _ClassVar[Composable.ElementType]
        BUTTON: _ClassVar[Composable.ElementType]
        IMAGE: _ClassVar[Composable.ElementType]
        COMPONENT: _ClassVar[Composable.ElementType]
        CONTAINER: _ClassVar[Composable.ElementType]
        BUTTON_TILE: _ClassVar[Composable.ElementType]
        BUTTON_TILE_WATCHLIST: _ClassVar[Composable.ElementType]
        BUTTON_TILE_DOWNLOAD: _ClassVar[Composable.ElementType]
        BUTTON_TILE_RATING: _ClassVar[Composable.ElementType]
        PLAYER_MINI: _ClassVar[Composable.ElementType]
        TAGS_FIXED: _ClassVar[Composable.ElementType]
        TAGS_SCROLLABLE: _ClassVar[Composable.ElementType]
        TIMER_MINI: _ClassVar[Composable.ElementType]
        MEDIA: _ClassVar[Composable.ElementType]
        BUTTON_TOGGLE: _ClassVar[Composable.ElementType]
        TEXT_EXPANDABLE: _ClassVar[Composable.ElementType]
        BUTTON_STACK: _ClassVar[Composable.ElementType]
        BUTTON_ICON: _ClassVar[Composable.ElementType]
    TEXT: Composable.ElementType
    BUTTON: Composable.ElementType
    IMAGE: Composable.ElementType
    COMPONENT: Composable.ElementType
    CONTAINER: Composable.ElementType
    BUTTON_TILE: Composable.ElementType
    BUTTON_TILE_WATCHLIST: Composable.ElementType
    BUTTON_TILE_DOWNLOAD: Composable.ElementType
    BUTTON_TILE_RATING: Composable.ElementType
    PLAYER_MINI: Composable.ElementType
    TAGS_FIXED: Composable.ElementType
    TAGS_SCROLLABLE: Composable.ElementType
    TIMER_MINI: Composable.ElementType
    MEDIA: Composable.ElementType
    BUTTON_TOGGLE: Composable.ElementType
    TEXT_EXPANDABLE: Composable.ElementType
    BUTTON_STACK: Composable.ElementType
    BUTTON_ICON: Composable.ElementType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: Composable.ElementType
    content: bytes
    def __init__(self, type: _Optional[_Union[Composable.ElementType, str]] = ..., content: _Optional[bytes] = ...) -> None: ...
