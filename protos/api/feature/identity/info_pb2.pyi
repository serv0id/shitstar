from options import opts_pb2 as _opts_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserInfo(_message.Message):
    __slots__ = ("phone_number", "name", "email", "current_country_code", "is_email_verified", "is_phone_verified", "user_status", "ssai_tag", "subs_pack_name", "home_country", "is_user_logged_in")
    class PhoneNumber(_message.Message):
        __slots__ = ("phone_number",)
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        phone_number: int
        def __init__(self, phone_number: _Optional[int] = ...) -> None: ...
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    IS_EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    USER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SSAI_TAG_FIELD_NUMBER: _ClassVar[int]
    SUBS_PACK_NAME_FIELD_NUMBER: _ClassVar[int]
    HOME_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    IS_USER_LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
    phone_number: UserInfo.PhoneNumber
    name: str
    email: str
    current_country_code: str
    is_email_verified: bool
    is_phone_verified: bool
    user_status: str
    ssai_tag: str
    subs_pack_name: str
    home_country: str
    is_user_logged_in: bool
    def __init__(self, phone_number: _Optional[_Union[UserInfo.PhoneNumber, _Mapping]] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., current_country_code: _Optional[str] = ..., is_email_verified: bool = ..., is_phone_verified: bool = ..., user_status: _Optional[str] = ..., ssai_tag: _Optional[str] = ..., subs_pack_name: _Optional[str] = ..., home_country: _Optional[str] = ..., is_user_logged_in: bool = ...) -> None: ...
