from v2 import space_pb2 as _space_pb2
from v2 import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceResponse(_message.Message):
    __slots__ = ("success", "error")
    class Success(_message.Message):
        __slots__ = ("space",)
        SPACE_FIELD_NUMBER: _ClassVar[int]
        space: _space_pb2.Space
        def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SpaceResponse.Success
    error: _error_pb2.Error
    def __init__(self, success: _Optional[_Union[SpaceResponse.Success, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
