from component.subs import paywall_type_pb2 as _paywall_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubsDisclaimerViewProperties(_message.Message):
    __slots__ = ("page_language", "pay_link_displayed", "paywall_type", "pack_id", "journey", "source")
    PAGE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PAY_LINK_DISPLAYED_FIELD_NUMBER: _ClassVar[int]
    PAYWALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    PACK_ID_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    page_language: str
    pay_link_displayed: str
    paywall_type: _paywall_type_pb2.PaywallType
    pack_id: str
    journey: str
    source: str
    def __init__(self, page_language: _Optional[str] = ..., pay_link_displayed: _Optional[str] = ..., paywall_type: _Optional[_Union[_paywall_type_pb2.PaywallType, str]] = ..., pack_id: _Optional[str] = ..., journey: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...
