from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LayoutFill(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILL: _ClassVar[LayoutFill]

class LayoutHug(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HUG: _ClassVar[LayoutHug]

class LayoutHugFill(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Hug: _ClassVar[LayoutHugFill]
    Fill: _ClassVar[LayoutHugFill]
FILL: LayoutFill
HUG: LayoutHug
Hug: LayoutHugFill
Fill: LayoutHugFill

class Layout(_message.Message):
    __slots__ = ("trait", "fixed")
    TRAIT_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    trait: LayoutHugFill
    fixed: int
    def __init__(self, trait: _Optional[_Union[LayoutHugFill, str]] = ..., fixed: _Optional[int] = ...) -> None: ...

class LayoutFillFixed(_message.Message):
    __slots__ = ("trait", "fixed")
    TRAIT_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    trait: LayoutFill
    fixed: int
    def __init__(self, trait: _Optional[_Union[LayoutFill, str]] = ..., fixed: _Optional[int] = ...) -> None: ...

class LayoutHugFixed(_message.Message):
    __slots__ = ("trait", "fixed")
    TRAIT_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    trait: LayoutHug
    fixed: int
    def __init__(self, trait: _Optional[_Union[LayoutHug, str]] = ..., fixed: _Optional[int] = ...) -> None: ...
