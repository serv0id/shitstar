from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BadgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[BadgeType]
    LIVE: _ClassVar[BadgeType]
    NUMBER: _ClassVar[BadgeType]
NONE: BadgeType
LIVE: BadgeType
NUMBER: BadgeType

class Badge(_message.Message):
    __slots__ = ("badge_type", "badge_text")
    BADGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BADGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    badge_type: BadgeType
    badge_text: str
    def __init__(self, badge_type: _Optional[_Union[BadgeType, str]] = ..., badge_text: _Optional[str] = ...) -> None: ...
