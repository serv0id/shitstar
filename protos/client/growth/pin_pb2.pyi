from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PinProperties(_message.Message):
    __slots__ = ("pin_type",)
    class PinType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PIN_TYPE_UNSPECIFIED: _ClassVar[PinProperties.PinType]
        PIN_TYPE_HIDDEN: _ClassVar[PinProperties.PinType]
        PIN_TYPE_PINNED: _ClassVar[PinProperties.PinType]
        PIN_TYPE_UNPINNED: _ClassVar[PinProperties.PinType]
    PIN_TYPE_UNSPECIFIED: PinProperties.PinType
    PIN_TYPE_HIDDEN: PinProperties.PinType
    PIN_TYPE_PINNED: PinProperties.PinType
    PIN_TYPE_UNPINNED: PinProperties.PinType
    PIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    pin_type: PinProperties.PinType
    def __init__(self, pin_type: _Optional[_Union[PinProperties.PinType, str]] = ...) -> None: ...
