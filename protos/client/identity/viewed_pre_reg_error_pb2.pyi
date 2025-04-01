from component.identity import pre_reg_properties_pb2 as _pre_reg_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedPreRegError(_message.Message):
    __slots__ = ("pre_reg_properties",)
    PRE_REG_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    pre_reg_properties: _pre_reg_properties_pb2.PreRegProperties
    def __init__(self, pre_reg_properties: _Optional[_Union[_pre_reg_properties_pb2.PreRegProperties, _Mapping]] = ...) -> None: ...
