from client.ads import ad_format_pb2 as _ad_format_pb2
from client.ads import ad_slot_pb2 as _ad_slot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Common(_message.Message):
    __slots__ = ("ad_type", "ad_slot_id_list", "ad_request_id", "ad_placement", "screen_mode", "ad_request_protocol", "ad_slots", "ad_placement_type", "ad_format")
    class AdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AD_TYPE_UNSPECIFIED: _ClassVar[Common.AdType]
        AD_TYPE_DISPLAY: _ClassVar[Common.AdType]
        AD_TYPE_VIDEO: _ClassVar[Common.AdType]
    AD_TYPE_UNSPECIFIED: Common.AdType
    AD_TYPE_DISPLAY: Common.AdType
    AD_TYPE_VIDEO: Common.AdType
    class AdPlacement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AD_PLACEMENT_UNSPECIFIED: _ClassVar[Common.AdPlacement]
        AD_PLACEMENT_ATF: _ClassVar[Common.AdPlacement]
        AD_PLACEMENT_BTF: _ClassVar[Common.AdPlacement]
        AD_PLACEMENT_PRE_ROLL: _ClassVar[Common.AdPlacement]
        AD_PLACEMENT_MID_ROLL: _ClassVar[Common.AdPlacement]
        AD_PLACEMENT_LIVE_MID_ROLL: _ClassVar[Common.AdPlacement]
    AD_PLACEMENT_UNSPECIFIED: Common.AdPlacement
    AD_PLACEMENT_ATF: Common.AdPlacement
    AD_PLACEMENT_BTF: Common.AdPlacement
    AD_PLACEMENT_PRE_ROLL: Common.AdPlacement
    AD_PLACEMENT_MID_ROLL: Common.AdPlacement
    AD_PLACEMENT_LIVE_MID_ROLL: Common.AdPlacement
    class ScreenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCREEN_MODE_UNSPECIFIED: _ClassVar[Common.ScreenMode]
        SCREEN_MODE_PORTRAIT: _ClassVar[Common.ScreenMode]
        SCREEN_MODE_LANDSCAPE: _ClassVar[Common.ScreenMode]
    SCREEN_MODE_UNSPECIFIED: Common.ScreenMode
    SCREEN_MODE_PORTRAIT: Common.ScreenMode
    SCREEN_MODE_LANDSCAPE: Common.ScreenMode
    class AdProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AD_PROTOCOL_UNSPECIFIED: _ClassVar[Common.AdProtocol]
        AD_PROTOCOL_NATIVE: _ClassVar[Common.AdProtocol]
        AD_PROTOCOL_VAST: _ClassVar[Common.AdProtocol]
        AD_PROTOCOL_VMAP: _ClassVar[Common.AdProtocol]
    AD_PROTOCOL_UNSPECIFIED: Common.AdProtocol
    AD_PROTOCOL_NATIVE: Common.AdProtocol
    AD_PROTOCOL_VAST: Common.AdProtocol
    AD_PROTOCOL_VMAP: Common.AdProtocol
    AD_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_SLOT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    AD_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    AD_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    SCREEN_MODE_FIELD_NUMBER: _ClassVar[int]
    AD_REQUEST_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    AD_SLOTS_FIELD_NUMBER: _ClassVar[int]
    AD_PLACEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ad_type: Common.AdType
    ad_slot_id_list: str
    ad_request_id: str
    ad_placement: Common.AdPlacement
    screen_mode: Common.ScreenMode
    ad_request_protocol: Common.AdProtocol
    ad_slots: _containers.RepeatedCompositeFieldContainer[_ad_slot_pb2.AdSlot]
    ad_placement_type: str
    ad_format: _ad_format_pb2.AdFormat
    def __init__(self, ad_type: _Optional[_Union[Common.AdType, str]] = ..., ad_slot_id_list: _Optional[str] = ..., ad_request_id: _Optional[str] = ..., ad_placement: _Optional[_Union[Common.AdPlacement, str]] = ..., screen_mode: _Optional[_Union[Common.ScreenMode, str]] = ..., ad_request_protocol: _Optional[_Union[Common.AdProtocol, str]] = ..., ad_slots: _Optional[_Iterable[_Union[_ad_slot_pb2.AdSlot, _Mapping]]] = ..., ad_placement_type: _Optional[str] = ..., ad_format: _Optional[_Union[_ad_format_pb2.AdFormat, str]] = ...) -> None: ...
