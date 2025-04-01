from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Restore(_message.Message):
    __slots__ = ("commercial_pack_id", "message")
    class MessageOnRestore(_message.Message):
        __slots__ = ("success_msg", "invalid_msg", "loading_msg")
        SUCCESS_MSG_FIELD_NUMBER: _ClassVar[int]
        INVALID_MSG_FIELD_NUMBER: _ClassVar[int]
        LOADING_MSG_FIELD_NUMBER: _ClassVar[int]
        success_msg: str
        invalid_msg: str
        loading_msg: str
        def __init__(self, success_msg: _Optional[str] = ..., invalid_msg: _Optional[str] = ..., loading_msg: _Optional[str] = ...) -> None: ...
    COMMERCIAL_PACK_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    commercial_pack_id: str
    message: Restore.MessageOnRestore
    def __init__(self, commercial_pack_id: _Optional[str] = ..., message: _Optional[_Union[Restore.MessageOnRestore, _Mapping]] = ...) -> None: ...
