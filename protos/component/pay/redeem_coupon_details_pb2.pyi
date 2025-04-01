from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RedeemCouponDetails(_message.Message):
    __slots__ = ("prefilled_promo_code", "redeem_partner_name")
    PREFILLED_PROMO_CODE_FIELD_NUMBER: _ClassVar[int]
    REDEEM_PARTNER_NAME_FIELD_NUMBER: _ClassVar[int]
    prefilled_promo_code: str
    redeem_partner_name: str
    def __init__(self, prefilled_promo_code: _Optional[str] = ..., redeem_partner_name: _Optional[str] = ...) -> None: ...
