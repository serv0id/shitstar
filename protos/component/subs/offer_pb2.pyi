from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Offer(_message.Message):
    __slots__ = ("offer_name", "supported_plans")
    OFFER_NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PLANS_FIELD_NUMBER: _ClassVar[int]
    offer_name: str
    supported_plans: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, offer_name: _Optional[str] = ..., supported_plans: _Optional[_Iterable[str]] = ...) -> None: ...
