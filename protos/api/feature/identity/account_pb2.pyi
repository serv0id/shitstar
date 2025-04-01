from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ("account_id", "type")
    class AccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCOUNT_TYPE_UNSPECIFIED: _ClassVar[Account.AccountType]
        ACCOUNT_TYPE_GUEST: _ClassVar[Account.AccountType]
        ACCOUNT_TYPE_PHONE: _ClassVar[Account.AccountType]
        ACCOUNT_TYPE_EMAIL: _ClassVar[Account.AccountType]
        ACCOUNT_TYPE_DEVICE: _ClassVar[Account.AccountType]
    ACCOUNT_TYPE_UNSPECIFIED: Account.AccountType
    ACCOUNT_TYPE_GUEST: Account.AccountType
    ACCOUNT_TYPE_PHONE: Account.AccountType
    ACCOUNT_TYPE_EMAIL: Account.AccountType
    ACCOUNT_TYPE_DEVICE: Account.AccountType
    class AccountIdentifier(_message.Message):
        __slots__ = ("id", "dw_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        DW_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        dw_id: str
        def __init__(self, id: _Optional[str] = ..., dw_id: _Optional[str] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: Account.AccountIdentifier
    type: Account.AccountType
    def __init__(self, account_id: _Optional[_Union[Account.AccountIdentifier, _Mapping]] = ..., type: _Optional[_Union[Account.AccountType, str]] = ...) -> None: ...
