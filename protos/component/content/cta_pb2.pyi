from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CtaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CTA_TYPE_UNSPECIFIED: _ClassVar[CtaType]
    CTA_TYPE_PRIMARY: _ClassVar[CtaType]
    CTA_TYPE_SECONDARY: _ClassVar[CtaType]
CTA_TYPE_UNSPECIFIED: CtaType
CTA_TYPE_PRIMARY: CtaType
CTA_TYPE_SECONDARY: CtaType

class Cta(_message.Message):
    __slots__ = ("cta_name", "cta_type")
    CTA_NAME_FIELD_NUMBER: _ClassVar[int]
    CTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    cta_name: str
    cta_type: CtaType
    def __init__(self, cta_name: _Optional[str] = ..., cta_type: _Optional[_Union[CtaType, str]] = ...) -> None: ...
