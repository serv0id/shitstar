from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionDialogProperties(_message.Message):
    __slots__ = ("display_text", "permission_type")
    DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    display_text: str
    permission_type: _enum_pb2.PermissionType
    def __init__(self, display_text: _Optional[str] = ..., permission_type: _Optional[_Union[_enum_pb2.PermissionType, str]] = ...) -> None: ...
