from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurchaseNudgeDetails(_message.Message):
    __slots__ = ("nudge_type", "nudge_layout", "device_count", "feature_type")
    class NudgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NUDGE_TYPE_UNSPECIFIED: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_SUBSCRIBE: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_UPGRADE: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_RENEW: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_DR: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_PLAYER: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_FREE_TRIAL: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_PLAYER_VOD: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_PARTNER_OFFER: _ClassVar[PurchaseNudgeDetails.NudgeType]
        NUDGE_TYPE_MIGRATION_SUBS_CALLOUT: _ClassVar[PurchaseNudgeDetails.NudgeType]
    NUDGE_TYPE_UNSPECIFIED: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_SUBSCRIBE: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_UPGRADE: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_RENEW: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_DR: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_PLAYER: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_FREE_TRIAL: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_PLAYER_VOD: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_PARTNER_OFFER: PurchaseNudgeDetails.NudgeType
    NUDGE_TYPE_MIGRATION_SUBS_CALLOUT: PurchaseNudgeDetails.NudgeType
    class NudgeLayout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NUDGE_LAYOUT_UNSPECIFIED: _ClassVar[PurchaseNudgeDetails.NudgeLayout]
        NUDGE_LAYOUT_DECOUPLED: _ClassVar[PurchaseNudgeDetails.NudgeLayout]
        NUDGE_LAYOUT_NESTED: _ClassVar[PurchaseNudgeDetails.NudgeLayout]
    NUDGE_LAYOUT_UNSPECIFIED: PurchaseNudgeDetails.NudgeLayout
    NUDGE_LAYOUT_DECOUPLED: PurchaseNudgeDetails.NudgeLayout
    NUDGE_LAYOUT_NESTED: PurchaseNudgeDetails.NudgeLayout
    class FeatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_TYPE_UNSPECIFIED: _ClassVar[PurchaseNudgeDetails.FeatureType]
        FEATURE_TYPE_FREE_PREVIEW: _ClassVar[PurchaseNudgeDetails.FeatureType]
    FEATURE_TYPE_UNSPECIFIED: PurchaseNudgeDetails.FeatureType
    FEATURE_TYPE_FREE_PREVIEW: PurchaseNudgeDetails.FeatureType
    NUDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUDGE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    nudge_type: PurchaseNudgeDetails.NudgeType
    nudge_layout: PurchaseNudgeDetails.NudgeLayout
    device_count: int
    feature_type: PurchaseNudgeDetails.FeatureType
    def __init__(self, nudge_type: _Optional[_Union[PurchaseNudgeDetails.NudgeType, str]] = ..., nudge_layout: _Optional[_Union[PurchaseNudgeDetails.NudgeLayout, str]] = ..., device_count: _Optional[int] = ..., feature_type: _Optional[_Union[PurchaseNudgeDetails.FeatureType, str]] = ...) -> None: ...
