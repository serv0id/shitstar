from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaywallClickProperties(_message.Message):
    __slots__ = ("paytm_checkbox",)
    PAYTM_CHECKBOX_FIELD_NUMBER: _ClassVar[int]
    paytm_checkbox: bool
    def __init__(self, paytm_checkbox: bool = ...) -> None: ...
