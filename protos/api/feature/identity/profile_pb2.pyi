from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Profile(_message.Message):
    __slots__ = ("p_id", "type", "maturity_rating")
    class ProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROFILE_TYPE_UNSPECIFIED: _ClassVar[Profile.ProfileType]
        PROFILE_TYPE_ADULT: _ClassVar[Profile.ProfileType]
        PROFILE_TYPE_KIDS: _ClassVar[Profile.ProfileType]
    PROFILE_TYPE_UNSPECIFIED: Profile.ProfileType
    PROFILE_TYPE_ADULT: Profile.ProfileType
    PROFILE_TYPE_KIDS: Profile.ProfileType
    class ProfileIdentifier(_message.Message):
        __slots__ = ("id", "dw_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        DW_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        dw_id: str
        def __init__(self, id: _Optional[str] = ..., dw_id: _Optional[str] = ...) -> None: ...
    P_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MATURITY_RATING_FIELD_NUMBER: _ClassVar[int]
    p_id: Profile.ProfileIdentifier
    type: Profile.ProfileType
    maturity_rating: str
    def __init__(self, p_id: _Optional[_Union[Profile.ProfileIdentifier, _Mapping]] = ..., type: _Optional[_Union[Profile.ProfileType, str]] = ..., maturity_rating: _Optional[str] = ...) -> None: ...
