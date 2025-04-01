from v2.commons import user_id_type_pb2 as _user_id_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendVerificationCodeRequest(_message.Message):
    __slots__ = ("purpose", "channel", "recaptcha_token", "user_id_type", "email_address", "phone_number")
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    purpose: str
    channel: str
    recaptcha_token: str
    user_id_type: _user_id_type_pb2.UserIdType
    email_address: str
    phone_number: str
    def __init__(self, purpose: _Optional[str] = ..., channel: _Optional[str] = ..., recaptcha_token: _Optional[str] = ..., user_id_type: _Optional[_Union[_user_id_type_pb2.UserIdType, str]] = ..., email_address: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...

class VerifyVerificationCodeRequest(_message.Message):
    __slots__ = ("purpose", "user_id_type", "verification_code", "email_address", "phone_number")
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    purpose: str
    user_id_type: _user_id_type_pb2.UserIdType
    verification_code: str
    email_address: str
    phone_number: str
    def __init__(self, purpose: _Optional[str] = ..., user_id_type: _Optional[_Union[_user_id_type_pb2.UserIdType, str]] = ..., verification_code: _Optional[str] = ..., email_address: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...
