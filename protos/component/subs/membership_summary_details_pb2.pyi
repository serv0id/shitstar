from component.subs import purchase_nudge_details_pb2 as _purchase_nudge_details_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipSummaryDetails(_message.Message):
    __slots__ = ("plan_name", "coupon_code", "item_type", "nudge_type", "offer_animation")
    class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ITEM_TYPE_UNSPECIFIED: _ClassVar[MembershipSummaryDetails.ItemType]
        ITEM_TYPE_PURCHASE_NUDGE: _ClassVar[MembershipSummaryDetails.ItemType]
        ITEM_TYPE_ACTIVE_PLAN: _ClassVar[MembershipSummaryDetails.ItemType]
    ITEM_TYPE_UNSPECIFIED: MembershipSummaryDetails.ItemType
    ITEM_TYPE_PURCHASE_NUDGE: MembershipSummaryDetails.ItemType
    ITEM_TYPE_ACTIVE_PLAN: MembershipSummaryDetails.ItemType
    class OfferAnimation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFFER_ANIMATION_UNSPECIFIED: _ClassVar[MembershipSummaryDetails.OfferAnimation]
        OFFER_ANIMATION_ELIGIBLE_HIDDEN: _ClassVar[MembershipSummaryDetails.OfferAnimation]
        OFFER_ANIMATION_ELIGIBLE_VISIBLE: _ClassVar[MembershipSummaryDetails.OfferAnimation]
    OFFER_ANIMATION_UNSPECIFIED: MembershipSummaryDetails.OfferAnimation
    OFFER_ANIMATION_ELIGIBLE_HIDDEN: MembershipSummaryDetails.OfferAnimation
    OFFER_ANIMATION_ELIGIBLE_VISIBLE: MembershipSummaryDetails.OfferAnimation
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    COUPON_CODE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFER_ANIMATION_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    coupon_code: str
    item_type: MembershipSummaryDetails.ItemType
    nudge_type: _purchase_nudge_details_pb2.PurchaseNudgeDetails.NudgeType
    offer_animation: MembershipSummaryDetails.OfferAnimation
    def __init__(self, plan_name: _Optional[str] = ..., coupon_code: _Optional[str] = ..., item_type: _Optional[_Union[MembershipSummaryDetails.ItemType, str]] = ..., nudge_type: _Optional[_Union[_purchase_nudge_details_pb2.PurchaseNudgeDetails.NudgeType, str]] = ..., offer_animation: _Optional[_Union[MembershipSummaryDetails.OfferAnimation, str]] = ...) -> None: ...
