from feature.motion_system import dynamic_visual_asset_name_pb2 as _dynamic_visual_asset_name_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DynamicVisualAssetConfig(_message.Message):
    __slots__ = ["name", "is_immediate", "remove_when_paused", "is_infinite", "priority_order", "category"]
    class DynamicVisaualAssetPriorityOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNSPECIFIED_PRIORITY_ORDER: _ClassVar[DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder]
        P_ONE: _ClassVar[DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder]
        P_TWO: _ClassVar[DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder]
        P_THREE: _ClassVar[DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder]
        P_FOUR: _ClassVar[DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder]
        P_FIVE: _ClassVar[DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder]
    UNSPECIFIED_PRIORITY_ORDER: DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder
    P_ONE: DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder
    P_TWO: DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder
    P_THREE: DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder
    P_FOUR: DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder
    P_FIVE: DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder
    class DynamicVisualAssetCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNSPECIFIED_CATEGORY: _ClassVar[DynamicVisualAssetConfig.DynamicVisualAssetCategory]
        HEAVY: _ClassVar[DynamicVisualAssetConfig.DynamicVisualAssetCategory]
        MEDIUM: _ClassVar[DynamicVisualAssetConfig.DynamicVisualAssetCategory]
        LIGHT: _ClassVar[DynamicVisualAssetConfig.DynamicVisualAssetCategory]
    UNSPECIFIED_CATEGORY: DynamicVisualAssetConfig.DynamicVisualAssetCategory
    HEAVY: DynamicVisualAssetConfig.DynamicVisualAssetCategory
    MEDIUM: DynamicVisualAssetConfig.DynamicVisualAssetCategory
    LIGHT: DynamicVisualAssetConfig.DynamicVisualAssetCategory
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IMMEDIATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_WHEN_PAUSED_FIELD_NUMBER: _ClassVar[int]
    IS_INFINITE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_ORDER_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    name: _dynamic_visual_asset_name_pb2.DynamicVisualAssetName
    is_immediate: bool
    remove_when_paused: bool
    is_infinite: bool
    priority_order: DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder
    category: DynamicVisualAssetConfig.DynamicVisualAssetCategory
    def __init__(self, name: _Optional[_Union[_dynamic_visual_asset_name_pb2.DynamicVisualAssetName, str]] = ..., is_immediate: bool = ..., remove_when_paused: bool = ..., is_infinite: bool = ..., priority_order: _Optional[_Union[DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder, str]] = ..., category: _Optional[_Union[DynamicVisualAssetConfig.DynamicVisualAssetCategory, str]] = ...) -> None: ...
