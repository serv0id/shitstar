from component.identity import login_item_data_pb2 as _login_item_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginItemClicked(_message.Message):
    __slots__ = ("login_item_data",)
    LOGIN_ITEM_DATA_FIELD_NUMBER: _ClassVar[int]
    login_item_data: _login_item_data_pb2.LoginItemData
    def __init__(self, login_item_data: _Optional[_Union[_login_item_data_pb2.LoginItemData, _Mapping]] = ...) -> None: ...
