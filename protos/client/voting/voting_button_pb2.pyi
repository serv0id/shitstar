from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VotingButtonProperties(_message.Message):
    __slots__ = ("cta_type",)
    class CtaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CTA_TYPE_UNSPECIFIED: _ClassVar[VotingButtonProperties.CtaType]
        CTA_TYPE_PRIMARY: _ClassVar[VotingButtonProperties.CtaType]
        CTA_TYPE_SECONDARY: _ClassVar[VotingButtonProperties.CtaType]
    CTA_TYPE_UNSPECIFIED: VotingButtonProperties.CtaType
    CTA_TYPE_PRIMARY: VotingButtonProperties.CtaType
    CTA_TYPE_SECONDARY: VotingButtonProperties.CtaType
    CTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    cta_type: VotingButtonProperties.CtaType
    def __init__(self, cta_type: _Optional[_Union[VotingButtonProperties.CtaType, str]] = ...) -> None: ...
