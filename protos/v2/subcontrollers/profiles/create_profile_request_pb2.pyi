from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProfileRequest(_message.Message):
    __slots__ = ("name", "avatar_id", "maturity_rating_id", "subscribed_to_updates", "parental_lock_pin", "subscribe_to_updates", "age", "gender_key", "gender_id")
    class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CreateProfileRequest.Gender]
        MALE: _ClassVar[CreateProfileRequest.Gender]
        FEMALE: _ClassVar[CreateProfileRequest.Gender]
        OTHER: _ClassVar[CreateProfileRequest.Gender]
        PREFER_NOT_TO_SAY: _ClassVar[CreateProfileRequest.Gender]
    UNKNOWN: CreateProfileRequest.Gender
    MALE: CreateProfileRequest.Gender
    FEMALE: CreateProfileRequest.Gender
    OTHER: CreateProfileRequest.Gender
    PREFER_NOT_TO_SAY: CreateProfileRequest.Gender
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    MATURITY_RATING_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_TO_UPDATES_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_LOCK_PIN_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_TO_UPDATES_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_KEY_FIELD_NUMBER: _ClassVar[int]
    GENDER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    avatar_id: str
    maturity_rating_id: str
    subscribed_to_updates: str
    parental_lock_pin: str
    subscribe_to_updates: bool
    age: int
    gender_key: str
    gender_id: CreateProfileRequest.Gender
    def __init__(self, name: _Optional[str] = ..., avatar_id: _Optional[str] = ..., maturity_rating_id: _Optional[str] = ..., subscribed_to_updates: _Optional[str] = ..., parental_lock_pin: _Optional[str] = ..., subscribe_to_updates: bool = ..., age: _Optional[int] = ..., gender_key: _Optional[str] = ..., gender_id: _Optional[_Union[CreateProfileRequest.Gender, str]] = ...) -> None: ...
