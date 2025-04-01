from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityInfo(_message.Message):
    __slots__ = ("id", "user_status", "timestamp")
    class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[CommunityInfo.UserStatus]
        JOINED: _ClassVar[CommunityInfo.UserStatus]
        NOT_JOINED: _ClassVar[CommunityInfo.UserStatus]
        BLOCKED: _ClassVar[CommunityInfo.UserStatus]
        RESTRICTED: _ClassVar[CommunityInfo.UserStatus]
    DEFAULT: CommunityInfo.UserStatus
    JOINED: CommunityInfo.UserStatus
    NOT_JOINED: CommunityInfo.UserStatus
    BLOCKED: CommunityInfo.UserStatus
    RESTRICTED: CommunityInfo.UserStatus
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_status: CommunityInfo.UserStatus
    timestamp: int
    def __init__(self, id: _Optional[str] = ..., user_status: _Optional[_Union[CommunityInfo.UserStatus, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...
