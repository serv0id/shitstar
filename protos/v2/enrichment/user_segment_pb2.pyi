from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserSegment(_message.Message):
    __slots__ = ("ssai", "location", "user_segment", "status")
    class DataStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DATA_STATUS: _ClassVar[UserSegment.DataStatus]
        UPDATED: _ClassVar[UserSegment.DataStatus]
        STALE: _ClassVar[UserSegment.DataStatus]
        OVERSIZE: _ClassVar[UserSegment.DataStatus]
        FAILED: _ClassVar[UserSegment.DataStatus]
    UNKNOWN_DATA_STATUS: UserSegment.DataStatus
    UPDATED: UserSegment.DataStatus
    STALE: UserSegment.DataStatus
    OVERSIZE: UserSegment.DataStatus
    FAILED: UserSegment.DataStatus
    class Location(_message.Message):
        __slots__ = ("country", "pin_code", "state", "city")
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        PIN_CODE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        country: str
        pin_code: int
        state: str
        city: str
        def __init__(self, country: _Optional[str] = ..., pin_code: _Optional[int] = ..., state: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
    SSAI_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    USER_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ssai: str
    location: UserSegment.Location
    user_segment: str
    status: UserSegment.DataStatus
    def __init__(self, ssai: _Optional[str] = ..., location: _Optional[_Union[UserSegment.Location, _Mapping]] = ..., user_segment: _Optional[str] = ..., status: _Optional[_Union[UserSegment.DataStatus, str]] = ...) -> None: ...
